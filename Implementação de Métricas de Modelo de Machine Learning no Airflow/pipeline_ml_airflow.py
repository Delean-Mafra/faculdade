from __future__ import annotations

import os
import logging
from pathlib import Path
from typing import Dict, Any

import joblib
import pandas as pd
from pendulum import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split

from airflow import DAG
from airflow.decorators import task
from airflow.models import Variable
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

# ==========================
# Configurações e constantes
# ==========================
# Diretório para artefatos intermediários (certifique-se que existe e é persistente/compartilhado entre workers)
BASE_DIR = Path(os.getenv("ML_BASE_DIR", "/opt/airflow/data/ml_pipeline"))
BASE_DIR.mkdir(parents=True, exist_ok=True)

# Caminho do dataset de entrada (CSV)
ARQUIVO_DADOS = Path(Variable.get("ML_INPUT_CSV_PATH", default_var=os.getenv("ML_INPUT_CSV_PATH", "train.csv")))

# Artefatos locais gerados
ARQUIVO_MODELO = BASE_DIR / "modelo.pkl"
ARQUIVO_METRICAS = BASE_DIR / "metricas.txt"

# Configuração S3
S3_BUCKET = Variable.get("ML_S3_BUCKET", default_var=os.getenv("ML_S3_BUCKET", ""))
S3_PREFIX = Variable.get("ML_S3_PREFIX", default_var=os.getenv("ML_S3_PREFIX", "models/")).strip("/")
AWS_CONN_ID = Variable.get("ML_AWS_CONN_ID", default_var=os.getenv("ML_AWS_CONN_ID", "aws_default"))

# Colunas e alvo
COLUNAS_CATEGORICAS_ESPERADAS = ["Escolaridade", "Genero", "FicouReserva", "Cidade"]
TARGET = "VaiSair"

# ==========================
# Definição da DAG
# ==========================
with DAG(
    dag_id="pipeline_ml_airflow",
    start_date=datetime(2023, 1, 1, tz="UTC"),
    schedule=None,  # substitui schedule_interval=None
    catchup=False,
    default_args={"owner": "Delean-Mafra"},
    tags=["ml", "metrics", "s3", "example"],
) as dag:

    def _colunas_categoricas_presentes(df: pd.DataFrame) -> list[str]:
        return [c for c in COLUNAS_CATEGORICAS_ESPERADAS if c in df.columns]

    @task()
    def preprocessar_dados() -> Dict[str, str]:
        if not ARQUIVO_DADOS.exists():
            raise FileNotFoundError(f"Arquivo de dados não encontrado: {ARQUIVO_DADOS.resolve()}")

        df = pd.read_csv(ARQUIVO_DADOS)

        if TARGET not in df.columns:
            raise KeyError(f"Coluna alvo '{TARGET}' não encontrada no dataset. Colunas: {list(df.columns)}")

        cols_cat = _colunas_categoricas_presentes(df)
        if cols_cat:
            df = pd.get_dummies(df, columns=cols_cat, drop_first=True)

        X = df.drop(columns=TARGET)
        y = df[TARGET]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.3,
            random_state=42,
            stratify=y if y.nunique() > 1 else None,
        )

        # Persistência em CSV para evitar XComs grandes
        X_train_path = BASE_DIR / "X_train.csv"
        X_test_path = BASE_DIR / "X_test.csv"
        y_train_path = BASE_DIR / "y_train.csv"
        y_test_path = BASE_DIR / "y_test.csv"

        X_train.to_csv(X_train_path, index=False)
        X_test.to_csv(X_test_path, index=False)
        pd.DataFrame({TARGET: y_train}).to_csv(y_train_path, index=False)
        pd.DataFrame({TARGET: y_test}).to_csv(y_test_path, index=False)

        logging.info("Pré-processamento concluído.")
        return {
            "X_train": str(X_train_path),
            "X_test": str(X_test_path),
            "y_train": str(y_train_path),
            "y_test": str(y_test_path),
        }

    @task()
    def treinar_modelo(paths: Dict[str, str]) -> str:
        X_train = pd.read_csv(paths["X_train"])
        y_train = pd.read_csv(paths["y_train"])[TARGET].squeeze()

        modelo = LogisticRegression(max_iter=1000)  # ajuste solver/class_weight conforme necessidade
        modelo.fit(X_train, y_train.to_numpy().ravel())

        joblib.dump(modelo, ARQUIVO_MODELO)
        logging.info(f"Modelo treinado e salvo em {ARQUIVO_MODELO}")
        return str(ARQUIVO_MODELO)

    @task()
    def validar_metricas(paths: Dict[str, str], modelo_path: str) -> Dict[str, Any]:
        X_test = pd.read_csv(paths["X_test"])
        y_test = pd.read_csv(paths["y_test"])[TARGET].squeeze()

        modelo = joblib.load(modelo_path)
        y_pred = modelo.predict(X_test)

        acuracia = accuracy_score(y_test, y_pred)

        # AUC-ROC com probabilidades; trata caso de classe única no teste
        try:
            if hasattr(modelo, "predict_proba"):
                y_score = modelo.predict_proba(X_test)[:, 1]
            elif hasattr(modelo, "decision_function"):
                y_score = modelo.decision_function(X_test)
            else:
                y_score = y_pred  # fallback (não ideal)

            if pd.Series(y_test).nunique() < 2:
                auc = float("nan")
                logging.warning("AUC-ROC não calculada: conjunto de teste com apenas uma classe.")
            else:
                auc = roc_auc_score(y_test, y_score)
        except Exception as e:
            auc = float("nan")
            logging.exception(f"Falha ao calcular AUC-ROC: {e}")

        with open(ARQUIVO_METRICAS, "w", encoding="utf-8") as f:
            f.write(f"Acurácia: {acuracia:.4f}\n")
            f.write(f"AUC-ROC: {auc if pd.notna(auc) else 'NaN'}\n")

        logging.info(f"Métricas salvas em {ARQUIVO_METRICAS}")
        return {
            "accuracy": float(acuracia),
            "roc_auc": None if pd.isna(auc) else float(auc),
            "metrics_path": str(ARQUIVO_METRICAS),
        }

    @task()
    def selecionar_modelo(metricas: Dict[str, Any], modelo_path: str) -> Dict[str, str]:
        # Seleção de modelo baseada em métricas.
        # Aqui há apenas um candidato; em cenários reais, comparar múltiplos candidatos.
        # Opcionalmente, você pode impor um threshold (ex.: AUC >= 0.6) para aprovar o modelo.

        # Exemplo de threshold opcional (comente/descomente conforme necessidade):
        # if metricas["roc_auc"] is not None and metricas["roc_auc"] < 0.6:
        #     raise ValueError(f"Modelo reprovado: AUC {metricas['roc_auc']:.4f} < 0.60")

        logging.info(
            f"Modelo selecionado com métricas: "
            f"accuracy={metricas.get('accuracy')}, roc_auc={metricas.get('roc_auc')}"
        )
        return {
            "model_path": modelo_path,
            "metrics_path": metricas["metrics_path"],
        }

    @task()
    def publicar_modelo(selection: Dict[str, str]) -> str:
        # Publica o modelo e o arquivo de métricas no S3.
        # Requer:
        #   - Conn Id AWS configurado (padrão: aws_default)
        #   - Variable ML_S3_BUCKET (ou env ML_S3_BUCKET) com o nome do bucket

        if not S3_BUCKET:
            raise ValueError(
                "Bucket S3 não configurado. Defina a Airflow Variable 'ML_S3_BUCKET' "
                "ou a variável de ambiente 'ML_S3_BUCKET'."
            )

        hook = S3Hook(aws_conn_id=AWS_CONN_ID)
        ts = datetime.now(tz="UTC").format("YYYYMMDDTHHmmss")

        model_key = f"{S3_PREFIX}/modelos/modelo_{ts}.pkl" if S3_PREFIX else f"modelos/modelo_{ts}.pkl"
        metrics_key = f"{S3_PREFIX}/modelos/metricas_{ts}.txt" if S3_PREFIX else f"modelos/metricas_{ts}.txt"

        hook.load_file(filename=selection["model_path"], key=model_key, bucket_name=S3_BUCKET, replace=True)
        hook.load_file(filename=selection["metrics_path"], key=metrics_key, bucket_name=S3_BUCKET, replace=True)

        model_uri = f"s3://{S3_BUCKET}/{model_key}"
        metrics_uri = f"s3://{S3_BUCKET}/{metrics_key}"
        logging.info(f"Modelo publicado em {model_uri}")
        logging.info(f"Métricas publicadas em {metrics_uri}")
        return model_uri
