# Python:
from __future__ import annotations

import pendulum
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator, get_current_context 
from airflow.operators.bash import BashOperator 
from airflow.operators.empty import EmptyOperator 
from airflow.providers.postgres.hooks.postgres import PostgresHook 
from airflow.utils.trigger_rule import TriggerRule 

# -----------------------------
# Parâmetros e configurações
# -----------------------------
CONN_ID_POSTGRES = "atividade_pratica_postgres"
DAG_ID = "atividade_pratica_dag_v1"
FUSO = "America/Sao_Paulo"

# -----------------------------
# Funções (callables) para tasks
# -----------------------------
def imprimir_mensagem():
    print("Execução da task Python: operação simples concluída.")

def consultar_postgres_e_retornar_contagem() -> int:
    hook = PostgresHook(postgres_conn_id=CONN_ID_POSTGRES)
    resultado = hook.get_first("SELECT COUNT(*) FROM usuarios;")
    contagem = int(resultado[0]) if resultado and resultado[0] is not None else 0
    print(f"Contagem de registros na tabela usuarios: {contagem}")
    return contagem

def decidir_ramificacao() -> str:
    context = get_current_context()
    ti = context["ti"]
    contagem_usuarios = ti.xcom_pull(task_ids="consultar_postgres", key="return_value")
    if contagem_usuarios is None:
        contagem_usuarios = 0

    print(f"Valor recebido via XCom (consultar_postgres): {contagem_usuarios}")

    if contagem_usuarios > 5:
        return "branch_muitos_usuarios"
    else:
        return "branch_poucos_usuarios"

# -----------------------------
# Definição do DAG
# -----------------------------
with DAG(
    dag_id=DAG_ID,
    description="DAG de prática: operadores, hooks, XCom e ramificação",
    start_date=pendulum.datetime(2025, 1, 1, tz=FUSO),
    schedule=None,  
    catchup=False,
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    tags=["atividade_pratica", "airflow", "exemplo"],
) as dag:

    inicio = EmptyOperator(
        task_id="inicio",
        doc_md="Task inicial que marca o começo do fluxo."
    )

    tarefa_imprimir = PythonOperator(
        task_id="imprimir_mensagem_python",
        python_callable=imprimir_mensagem,
        doc_md="Executa uma função Python simples que imprime uma mensagem."
    )

    tarefa_listar_arquivos = BashOperator(
        task_id="listar_arquivos_bash",
        bash_command='echo "Listando arquivos na pasta dags:" && ls -l',
        doc_md="Executa um comando Bash para listar arquivos (ajuste necessário no Windows)."
    )

    consultar_postgres = PythonOperator(
        task_id="consultar_postgres",
        python_callable=consultar_postgres_e_retornar_contagem,
        doc_md="Consulta o banco PostgreSQL via PostgresHook e retorna a contagem de registros."
    )

    decidir_branch = BranchPythonOperator(
        task_id="decidir_branch_com_base_no_xcom",
        python_callable=decidir_ramificacao,
        doc_md="Decide o fluxo com base no valor retornado pela task 'consultar_postgres'."
    )

    branch_muitos_usuarios = BashOperator(
        task_id="branch_muitos_usuarios",
        bash_command='echo "O número de usuários é maior que 5. Executando fluxo para muitos usuários."',
        doc_md="Caminho executado quando há muitos usuários (>5)."
    )

    branch_poucos_usuarios = BashOperator(
        task_id="branch_poucos_usuarios",
        bash_command='echo "O número de usuários é 5 ou menos. Executando fluxo alternativo."',
        doc_md="Caminho executado quando há poucos usuários (<=5)."
    )

    fim = EmptyOperator(
        task_id="fim",
        trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS,
        doc_md="Task final que marca o término do fluxo."
    )


    inicio >> [tarefa_imprimir, tarefa_listar_arquivos] >> consultar_postgres
    consultar_postgres >> decidir_branch >> [branch_muitos_usuarios, branch_poucos_usuarios] >> fim
