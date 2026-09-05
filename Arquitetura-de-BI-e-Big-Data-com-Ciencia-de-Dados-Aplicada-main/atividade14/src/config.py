import os

ES_HOST = os.getenv("ES_HOST", "http://localhost:9200")
ES_INDEX_PRODUTOS = os.getenv("ES_INDEX_PRODUTOS", "ecommerce_produtos")

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092,localhost:9093,localhost:9094")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "ecommerce_transacoes")

SPARK_MASTER = os.getenv("SPARK_MASTER", "local[*]")

PROMETHEUS_PORT_PRODUCER = int(os.getenv("PROMETHEUS_PORT_PRODUCER", "8001"))
PROMETHEUS_PORT_API = int(os.getenv("PROMETHEUS_PORT_API", "8002"))
PROMETHEUS_PORT_SPARK = int(os.getenv("PROMETHEUS_PORT_SPARK", "8003"))

DATA_DIR = os.getenv("DATA_DIR", "data")
RECOMMENDATION_STATE_DIR = os.getenv("RECOMMENDATION_STATE_DIR", "data/recomendacoes")
CHECKPOINT_DIR = os.getenv("CHECKPOINT_DIR", "data/checkpoints/spark_transacoes")
