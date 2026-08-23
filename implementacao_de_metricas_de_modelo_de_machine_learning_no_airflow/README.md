# Pipeline ML no Airflow (Treino, Métricas e Publicação no S3)

## Arquivos
- `dags/pipeline_ml_airflow.py`: DAG com tarefas de preprocessamento, treino, validação de métricas, seleção e publicação no S3.
- `data/train.csv`: dataset de treino (UTF-8).
- `data/ml_pipeline/`: será criado automaticamente para artefatos (modelo e métricas).
- `requirements.txt`: dependências.

## Pré-requisitos
- Airflow 2.x já instalado e em execução.
- Conexão AWS configurada no Airflow (`aws_default`) ou defina outra e referencie na variável `ML_AWS_CONN_ID`.
- Bucket S3 existente e permissões de escrita.

## Configuração (Airflow Variables ou variáveis de ambiente)
- `ML_INPUT_CSV_PATH` (opcional): caminho do CSV de treino. Padrão: `data/train.csv`.
- `ML_BASE_DIR` (opcional): diretório para artefatos. Padrão: `data/ml_pipeline`.
- `ML_S3_BUCKET` (obrigatória para publicar): nome do bucket S3.
- `ML_S3_PREFIX` (opcional): prefixo no bucket (padrão: `models/`).
- `ML_AWS_CONN_ID` (opcional): id da conexão AWS (padrão: `aws_default`).

## Execução
1. Coloque `train.csv` em `data/train.csv` (já incluso neste projeto).
2. Garanta que as Variáveis do Airflow estejam configuradas (principalmente `ML_S3_BUCKET`).
3. Ative e execute a DAG `pipeline_ml_airflow` pela UI do Airflow.
4. Ao finalizar:
   - Modelo salvo localmente em `data/ml_pipeline/modelo.pkl`.
   - Métricas salvas em `data/ml_pipeline/metricas.txt`.
   - Artefatos enviados ao S3 em `s3://<bucket>/<prefix>/modelos/`.

## Observações
- O cálculo de AUC-ROC utiliza `predict_proba` e trata o caso de classe única no conjunto de teste retornando `NaN`.
- Para seleção de modelo, há apenas um candidato; você pode habilitar um threshold comentado na task `selecionar_modelo`.
