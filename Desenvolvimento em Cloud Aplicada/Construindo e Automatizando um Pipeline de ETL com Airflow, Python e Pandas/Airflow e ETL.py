from __future__ import annotations

import json
import logging
import os
import shutil
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional

import pandas as pd
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator  
from airflow.providers.amazon.aws.hooks.s3 import S3Hook 
from airflow.providers.postgres.hooks.postgres import PostgresHook 
from airflow.utils.trigger_rule import TriggerRule 
from airflow.exceptions import AirflowException

# Configurações Gerais
S3_CONN_ID = "s3_default"
POSTGRES_CONN_ID = "postgres_default"
BUCKET_NAME = "meu-bucket-de-dados"
BASE_DATA_DIR = "/tmp/airflow_data"
FINAL_CSV_NAME = "dados_consolidados.csv"
TARGET_TABLE = "minha_tabela_final"

# Configurações de validação
MAX_FILE_SIZE_MB = 500
REQUIRED_CSV_COLUMNS = ["id", "timestamp", "value"] 
MAX_EMPTY_FILES = 2

# --- Funções Auxiliares ---

def get_unique_paths(run_id: str) -> Dict[str, str]:
    # Gera caminhos únicos baseados no run_id da execução.
    data_dir = f"{BASE_DATA_DIR}_{run_id}"
    return {
        'data_dir': data_dir,
        'raw_path': os.path.join(data_dir, "raw"),
        'processed_path': os.path.join(data_dir, "processed")
    }

def validate_file_size(file_path: str) -> bool:
    # Valida se o arquivo não excede o tamanho máximo permitido.
    if not os.path.exists(file_path):
        return False
    
    size_mb = os.path.getsize(file_path) / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        logging.warning(f"Arquivo {file_path} excede {MAX_FILE_SIZE_MB}MB: {size_mb:.2f}MB")
        return False
    
    return size_mb > 0  # Arquivo não pode estar vazio

def validate_csv_structure(df: pd.DataFrame, file_path: str) -> bool:
    # Valida se o CSV tem a estrutura esperada.
    if df.empty:
        logging.warning(f"DataFrame vazio para o arquivo: {file_path}")
        return False
    
    missing_columns = set(REQUIRED_CSV_COLUMNS) - set(df.columns)
    if missing_columns:
        logging.error(f"Colunas obrigatórias ausentes em {file_path}: {missing_columns}")
        return False
    
    # Validar tipos de dados básicos
    try:
        if 'timestamp' in df.columns:
            pd.to_datetime(df['timestamp'].dropna().head(), errors='raise')
        if 'value' in df.columns:
            pd.to_numeric(df['value'].dropna().head(), errors='raise')
    except (ValueError, TypeError) as e:
        logging.error(f"Erro de formato de dados em {file_path}: {str(e)}")
        return False
    
    return True

# --- Funções do Pipeline ---

def _validate_connections(**kwargs):
    # Valida se todas as conexões necessárias estão funcionais.
    try:
        logging.info("Iniciando validação de conexões...")
        
        # Testar conexão S3
        s3_hook = S3Hook(aws_conn_id=S3_CONN_ID)
        s3_conn = s3_hook.get_conn()
        
        # Testar se o bucket existe
        if not s3_hook.check_for_bucket(BUCKET_NAME):
            raise AirflowException(f"Bucket {BUCKET_NAME} não encontrado")
        
        # Testar conexão PostgreSQL
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        pg_conn = pg_hook.get_conn()
        
        # Verificar se a tabela de destino existe
        table_exists_query = f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = '{TARGET_TABLE}'
        );
        """
        result = pg_hook.get_first(table_exists_query)
        if not result or not result[0]:
            logging.warning(f"Tabela {TARGET_TABLE} não existe. Será necessário criá-la.")
        
        logging.info("Todas as conexões validadas com sucesso")
        return True
        
    except Exception as e:
        logging.error(f"Erro na validação de conexões: {str(e)}")
        raise AirflowException(f"Falha na validação de conexões: {str(e)}")

def _setup_folders(**kwargs):
    # Cria os diretórios temporários únicos para a execução do DAG.
    try:
        run_id = kwargs['run_id'].replace(':', '_').replace('+', '_')
        paths = get_unique_paths(run_id)
        
        # Limpar diretório se existir
        if os.path.exists(paths['data_dir']):
            shutil.rmtree(paths['data_dir'])
        
        # Criar novos diretórios
        os.makedirs(paths['raw_path'], exist_ok=True)
        os.makedirs(paths['processed_path'], exist_ok=True)
        
        logging.info(f"Diretórios criados: {paths['data_dir']}")
        return paths
        
    except Exception as e:
        logging.error(f"Erro na criação de diretórios: {str(e)}")
        raise AirflowException(f"Falha na criação de diretórios: {str(e)}")

def _extract_data(**kwargs):
    # Extrai arquivos CSV e JSON do S3 com validação e tratamento de erros.
    try:
        ds = kwargs["ds"]
        ti = kwargs["ti"]
        paths = ti.xcom_pull(task_ids="setup_folders_task")
        
        if not paths:
            raise AirflowException("Caminhos de diretório não encontrados")
        
        s3_hook = S3Hook(aws_conn_id=S3_CONN_ID)
        
        # Definir prefixos para busca
        prefix_csv = f"dados_diarios/{ds}/"
        prefix_json = f"metadados/{ds}/"
        
        logging.info(f"Buscando arquivos para a data: {ds}")
        
        # Buscar arquivos
        csv_files = s3_hook.list_keys(bucket_name=BUCKET_NAME, prefix=prefix_csv) or []
        json_files = s3_hook.list_keys(bucket_name=BUCKET_NAME, prefix=prefix_json) or []
        
        # Filtrar apenas arquivos (não diretórios)
        csv_files = [f for f in csv_files if f.endswith('.csv')]
        json_files = [f for f in json_files if f.endswith('.json')]
        
        if not csv_files:
            raise AirflowException(f"Nenhum arquivo CSV encontrado para a data {ds} no prefixo {prefix_csv}")
        
        logging.info(f"Encontrados {len(csv_files)} CSVs e {len(json_files)} JSONs")
        
        downloaded_files = {"csv": [], "json": [], "failed": []}
        
        # Download dos CSVs
        for key in csv_files:
            try:
                filename = os.path.basename(key)
                local_path = os.path.join(paths['raw_path'], filename)
                
                logging.info(f"Baixando CSV: {key}")
                s3_hook.download_file(key=key, bucket_name=BUCKET_NAME, local_path=local_path)
                
                # Validar arquivo baixado
                if validate_file_size(local_path):
                    downloaded_files["csv"].append(local_path)
                    logging.info(f"CSV baixado com sucesso: {filename}")
                else:
                    downloaded_files["failed"].append(key)
                    logging.error(f"Arquivo CSV inválido: {key}")
                    
            except Exception as e:
                downloaded_files["failed"].append(key)
                logging.error(f"Erro ao baixar CSV {key}: {str(e)}")
        
        # Download dos JSONs
        for key in json_files:
            try:
                filename = os.path.basename(key)
                local_path = os.path.join(paths['raw_path'], filename)
                
                logging.info(f"Baixando JSON: {key}")
                s3_hook.download_file(key=key, bucket_name=BUCKET_NAME, local_path=local_path)
                
                # Validar arquivo baixado
                if validate_file_size(local_path):
                    # Testar se é um JSON válido
                    try:
                        with open(local_path, 'r') as f:
                            json.load(f)
                        downloaded_files["json"].append(local_path)
                        logging.info(f"JSON baixado com sucesso: {filename}")
                    except json.JSONDecodeError:
                        downloaded_files["failed"].append(key)
                        logging.error(f"JSON inválido: {key}")
                else:
                    downloaded_files["failed"].append(key)
                    logging.error(f"Arquivo JSON inválido: {key}")
                    
            except Exception as e:
                downloaded_files["failed"].append(key)
                logging.error(f"Erro ao baixar JSON {key}: {str(e)}")
        
        # Verificar se há arquivos suficientes
        if not downloaded_files["csv"]:
            raise AirflowException("Nenhum arquivo CSV válido foi baixado")
        
        if downloaded_files["failed"]:
            logging.warning(f"Arquivos que falharam no download: {downloaded_files['failed']}")
        
        logging.info(f"Extração concluída: {len(downloaded_files['csv'])} CSVs e {len(downloaded_files['json'])} JSONs válidos")
        
        # Adicionar paths para próximas tarefas
        downloaded_files["paths"] = paths
        return downloaded_files
        
    except Exception as e:
        logging.error(f"Erro na extração de dados: {str(e)}")
        raise AirflowException(f"Falha na extração: {str(e)}")

def _transform_data(**kwargs):
    # Transforma e consolida os dados extraídos com validação robusta.
    try:
        ti = kwargs["ti"]
        downloaded_files = ti.xcom_pull(task_ids="extract_data_task")
        
        if not downloaded_files or not downloaded_files.get("csv"):
            raise AirflowException("Nenhum arquivo CSV disponível para transformação")
        
        paths = downloaded_files["paths"]
        csv_files = downloaded_files["csv"]
        json_files = downloaded_files.get("json", [])
        
        logging.info(f"Iniciando transformação de {len(csv_files)} arquivos CSV")
        
        df_list = []
        empty_files = 0
        
        # Processar CSVs
        for csv_file in csv_files:
            try:
                logging.info(f"Processando CSV: {os.path.basename(csv_file)}")
                
                # Ler CSV com tratamento de erro
                df = pd.read_csv(csv_file, encoding='utf-8')
                
                if df.empty:
                    empty_files += 1
                    logging.warning(f"Arquivo vazio: {csv_file}")
                    if empty_files > MAX_EMPTY_FILES:
                        raise AirflowException(f"Muitos arquivos vazios encontrados (>{MAX_EMPTY_FILES})")
                    continue
                
                # Validar estrutura
                if not validate_csv_structure(df, csv_file):
                    logging.error(f"Estrutura inválida no arquivo: {csv_file}")
                    continue
                
                # Limpeza básica dos dados
                df = df.dropna(subset=['id'])  # Remove linhas sem ID
                df = df.drop_duplicates(subset=['id'], keep='last')  # Remove duplicatas
                
                # Padronizar timestamp se existir
                if 'timestamp' in df.columns:
                    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
                    df = df.dropna(subset=['timestamp'])
                
                # Adicionar metadados do arquivo
                df['source_file'] = os.path.basename(csv_file)
                df['processed_at'] = datetime.utcnow()
                
                df_list.append(df)
                logging.info(f"CSV processado: {len(df)} registros válidos")
                
            except Exception as e:
                logging.error(f"Erro ao processar CSV {csv_file}: {str(e)}")
                # Decidir se continua ou falha baseado na criticidade
                continue
        
        if not df_list:
            raise AirflowException("Nenhum CSV válido foi processado")
        
        # Consolidar todos os DataFrames
        logging.info("Consolidando DataFrames...")
        df_consolidado = pd.concat(df_list, ignore_index=True)
        
        # Processar JSONs para enriquecimento (opcional)
        metadata_df = None
        for json_file in json_files:
            try:
                logging.info(f"Processando JSON: {os.path.basename(json_file)}")
                
                with open(json_file, 'r') as f:
                    json_data = json.load(f)
                
                # Converter JSON para DataFrame
                if isinstance(json_data, list):
                    temp_df = pd.DataFrame(json_data)
                elif isinstance(json_data, dict):
                    temp_df = pd.DataFrame([json_data])
                else:
                    logging.warning(f"Formato JSON não suportado: {json_file}")
                    continue
                
                if 'id' in temp_df.columns:
                    if metadata_df is None:
                        metadata_df = temp_df
                    else:
                        metadata_df = pd.concat([metadata_df, temp_df], ignore_index=True)
                
            except Exception as e:
                logging.error(f"Erro ao processar JSON {json_file}: {str(e)}")
                continue
        
        # Fazer join com metadados se disponível
        if metadata_df is not None and 'id' in df_consolidado.columns:
            try:
                logging.info("Fazendo join com metadados...")
                initial_count = len(df_consolidado)
                df_consolidado = pd.merge(
                    df_consolidado, 
                    metadata_df, 
                    on='id', 
                    how='left', 
                    suffixes=('', '_meta')
                )
                logging.info(f"Join concluído. Registros: {initial_count} -> {len(df_consolidado)}")
                
            except Exception as e:
                logging.error(f"Erro no join com metadados: {str(e)}")
                # Continuar sem os metadados
        
        # Validações finais
        if df_consolidado.empty:
            raise AirflowException("DataFrame final está vazio")
        
        # Ordenar por timestamp se disponível
        if 'timestamp' in df_consolidado.columns:
            df_consolidado = df_consolidado.sort_values('timestamp')
        
        # Salvar arquivo consolidado
        final_csv_path = os.path.join(paths['processed_path'], FINAL_CSV_NAME)
        df_consolidado.to_csv(final_csv_path, index=False, encoding='utf-8')
        
        # Validar arquivo salvo
        if not validate_file_size(final_csv_path):
            raise AirflowException("Arquivo consolidado não foi salvo corretamente")
        
        logging.info(f"Transformação concluída: {len(df_consolidado)} registros salvos em {final_csv_path}")
        
        return {
            "final_csv_path": final_csv_path,
            "total_records": len(df_consolidado),
            "columns": list(df_consolidado.columns),
            "paths": paths
        }
        
    except Exception as e:
        logging.error(f"Erro na transformação de dados: {str(e)}")
        raise AirflowException(f"Falha na transformação: {str(e)}")

def _load_data(**kwargs):
    # Carrega os dados transformados para o PostgreSQL com verificações.
    try:
        ti = kwargs["ti"]
        transform_result = ti.xcom_pull(task_ids="transform_data_task")
        
        if not transform_result or not transform_result.get("final_csv_path"):
            raise AirflowException("Caminho do arquivo consolidado não encontrado")
        
        final_csv_path = transform_result["final_csv_path"]
        total_records = transform_result["total_records"]
        
        if not os.path.exists(final_csv_path):
            raise AirflowException(f"Arquivo consolidado não encontrado: {final_csv_path}")
        
        logging.info(f"Iniciando carga de {total_records} registros no PostgreSQL")
        
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        
        # Verificar se a tabela existe e criar se necessário
        table_exists_query = f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = '{TARGET_TABLE}'
        );
        """
        
        if not pg_hook.get_first(table_exists_query)[0]:
            logging.info(f"Criando tabela {TARGET_TABLE}...")
            
            # Script de criação da tabela (ajustar conforme estrutura dos dados)
            create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {TARGET_TABLE} (
                id VARCHAR(100) PRIMARY KEY,
                timestamp TIMESTAMP,
                value NUMERIC,
                source_file VARCHAR(255),
                processed_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            pg_hook.run(create_table_sql)
            logging.info(f"Tabela {TARGET_TABLE} criada com sucesso")
        
        # Backup da tabela atual (opcional)
        backup_table = f"{TARGET_TABLE}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        backup_sql = f"CREATE TABLE {backup_table} AS SELECT * FROM {TARGET_TABLE};"
        
        try:
            pg_hook.run(backup_sql)
            logging.info(f"Backup criado: {backup_table}")
        except Exception as e:
            logging.warning(f"Não foi possível criar backup: {str(e)}")
        
        # Truncar tabela se necessário (ajustar conforme estratégia)
        # pg_hook.run(f"TRUNCATE TABLE {TARGET_TABLE};")
        
        # Carga dos dados usando COPY para performance
        copy_sql = f"COPY {TARGET_TABLE} FROM STDIN WITH CSV HEADER DELIMITER ','"
        
        with open(final_csv_path, 'r') as f:
            pg_hook.copy_expert(sql=copy_sql, filename=final_csv_path)
        
        # Verificar se a carga foi bem-sucedida
        count_query = f"SELECT COUNT(*) FROM {TARGET_TABLE};"
        loaded_records = pg_hook.get_first(count_query)[0]
        
        logging.info(f"Carga concluída: {loaded_records} registros na tabela {TARGET_TABLE}")
        
        # Executar análises básicas de qualidade
        quality_checks = {
            "total_records": loaded_records,
            "null_ids": pg_hook.get_first(f"SELECT COUNT(*) FROM {TARGET_TABLE} WHERE id IS NULL;")[0],
            "duplicate_ids": pg_hook.get_first(f"SELECT COUNT(*) - COUNT(DISTINCT id) FROM {TARGET_TABLE};")[0]
        }
        
        logging.info(f"Verificações de qualidade: {quality_checks}")
        
        if quality_checks["null_ids"] > 0:
            logging.warning(f"Encontrados {quality_checks['null_ids']} registros com ID nulo")
        
        if quality_checks["duplicate_ids"] > 0:
            logging.warning(f"Encontrados {quality_checks['duplicate_ids']} IDs duplicados")
        
        return quality_checks
        
    except Exception as e:
        logging.error(f"Erro na carga de dados: {str(e)}")
        raise AirflowException(f"Falha na carga: {str(e)}")

def _cleanup_folders(**kwargs):
    # Remove os diretórios temporários com verificação de segurança.
    try:
        ti = kwargs["ti"]
        
        # Tentar obter paths de diferentes tarefas
        paths = None
        for task_id in ["setup_folders_task", "extract_data_task", "transform_data_task"]:
            try:
                result = ti.xcom_pull(task_ids=task_id)
                if result and isinstance(result, dict):
                    if "paths" in result:
                        paths = result["paths"]
                    elif "data_dir" in result:
                        paths = result
                    break
            except:
                continue
        
        if paths and "data_dir" in paths:
            data_dir = paths["data_dir"]
            
            # Verificação de segurança: não remover diretórios fora do esperado
            if BASE_DATA_DIR in data_dir and os.path.exists(data_dir):
                shutil.rmtree(data_dir)
                logging.info(f"Diretório temporário removido: {data_dir}")
            else:
                logging.warning(f"Diretório não removido por segurança: {data_dir}")
        else:
            logging.warning("Caminhos de diretório não encontrados para limpeza")
            
    except Exception as e:
        logging.error(f"Erro na limpeza de diretórios: {str(e)}")
        # Não falhar o DAG por erro de limpeza

def _notify_completion(**kwargs):
    # Notifica a conclusão do pipeline com estatísticas.
    try:
        ti = kwargs["ti"]
        
        # Coletar resultados de todas as tarefas
        extract_result = ti.xcom_pull(task_ids="extract_data_task")
        transform_result = ti.xcom_pull(task_ids="transform_data_task")
        load_result = ti.xcom_pull(task_ids="load_data_task")
        
        summary = {
            "dag_run_id": kwargs["run_id"],
            "execution_date": kwargs["ds"],
            "extracted_files": {
                "csv": len(extract_result.get("csv", [])) if extract_result else 0,
                "json": len(extract_result.get("json", [])) if extract_result else 0,
                "failed": len(extract_result.get("failed", [])) if extract_result else 0
            },
            "transformed_records": transform_result.get("total_records", 0) if transform_result else 0,
            "loaded_records": load_result.get("total_records", 0) if load_result else 0,
            "quality_issues": {
                "null_ids": load_result.get("null_ids", 0) if load_result else 0,
                "duplicate_ids": load_result.get("duplicate_ids", 0) if load_result else 0
            } if load_result else {}
        }
        
        logging.info(f"Pipeline ETL concluído com sucesso: {json.dumps(summary, indent=2)}")
        
        return summary
        
    except Exception as e:
        logging.error(f"Erro na notificação: {str(e)}")
        return {"status": "completed_with_notification_error"}

# --- Definição da DAG ---

default_args = {
    "owner": "Delean-Mafra",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(hours=2),
}

with DAG(
    dag_id="pipeline_etl_robusto_v2",
    default_args=default_args,
    description="Pipeline ETL robusto com tratamento de erros e validações",
    schedule_interval=None,  # Execução manual
    start_date=datetime(2025, 1, 1),
    catchup=False,
    max_active_runs=1,  # Evitar execuções concorrentes
    tags=["etl", "produção", "robusto"],
    doc_md="""
    # Pipeline ETL Robusto
    
    Este DAG implementa um pipeline ETL completo com:
    - Validação de conexões
    - Tratamento robusto de erros
    - Validação de dados
    - Verificações de qualidade
    - Limpeza automática de recursos
    
    ## Estrutura:
    1. **validate_connections**: Testa todas as conexões necessárias
    2. **setup_folders**: Cria diretórios temporários únicos
    3. **extract_data**: Extrai dados do S3 com validação
    4. **transform_data**: Transforma e consolida dados
    5. **load_data**: Carrega dados no PostgreSQL
    6. **notify_completion**: Gera relatório de execução
    7. **cleanup_folders**: Remove arquivos temporários
    """
) as dag:

    validate_connections_task = PythonOperator(
        task_id="validate_connections_task",
        python_callable=_validate_connections,
        doc_md="Valida se todas as conexões (S3, PostgreSQL) estão funcionais"
    )

    setup_folders_task = PythonOperator(
        task_id="setup_folders_task",
        python_callable=_setup_folders,
        doc_md="Cria diretórios temporários únicos para esta execução"
    )

    extract_data_task = PythonOperator(
        task_id="extract_data_task",
        python_callable=_extract_data,
        doc_md="Extrai arquivos CSV e JSON do S3 com validação de integridade"
    )

    transform_data_task = PythonOperator(
        task_id="transform_data_task",
        python_callable=_transform_data,
        doc_md="Transforma, limpa e consolida os dados extraídos"
    )

    load_data_task = PythonOperator(
        task_id="load_data_task",
        python_callable=_load_data,
        doc_md="Carrega dados consolidados no PostgreSQL com verificações"
    )

    notify_completion_task = PythonOperator(
        task_id="notify_completion_task",
        python_callable=_notify_completion,
        trigger_rule=TriggerRule.ALL_SUCCESS,
        doc_md="Gera relatório final da execução do pipeline"
    )

    cleanup_folders_task = PythonOperator(
        task_id="cleanup_folders_task",
        python_callable=_cleanup_folders,
        trigger_rule=TriggerRule.ALL_DONE,  # Executa sempre, mesmo com falhas
        doc_md="Remove diretórios temporários (executa sempre)"
    )

    # Definindo as dependências
    (
        validate_connections_task 
        >> setup_folders_task 
        >> extract_data_task 
        >> transform_data_task 
        >> load_data_task 
        >> notify_completion_task
        >> cleanup_folders_task
    )

    # Task de limpeza também executa se houver falhas nas tarefas principais
    [extract_data_task, transform_data_task, load_data_task] >> cleanup_folders_task
