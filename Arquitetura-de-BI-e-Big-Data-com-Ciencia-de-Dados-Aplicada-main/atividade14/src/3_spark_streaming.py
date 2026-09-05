import os
import json
from collections import Counter, defaultdict
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, from_json, window
from pyspark.sql.types import IntegerType, LongType, StructField, StructType
from prometheus_client import Counter as PrometheusCounter
from prometheus_client import Gauge, Summary, start_http_server

import config

os.environ["PYSPARK_SUBMIT_ARGS"] = (
    "--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 pyspark-shell"
)

BASE_DIR = Path(__file__).resolve().parent.parent
STATE_DIR = BASE_DIR / config.RECOMMENDATION_STATE_DIR
CHECKPOINT_DIR = BASE_DIR / config.CHECKPOINT_DIR

METRICA_PROCESSADAS = PrometheusCounter(
    "ecommerce_transacoes_processadas_total",
    "Total de transacoes processadas pelo Spark",
)
METRICA_ERROS = PrometheusCounter(
    "ecommerce_spark_erros_total",
    "Total de erros no processamento Spark",
)
METRICA_BATCHES = PrometheusCounter(
    "ecommerce_spark_batches_total",
    "Total de micro-batches processados pelo Spark",
)
GAUGE_CLIENTES = Gauge(
    "ecommerce_clientes_com_historico",
    "Quantidade de clientes com historico processado",
)
GAUGE_RELACOES = Gauge(
    "ecommerce_relacoes_coocorrencia",
    "Quantidade de relacoes de coocorrencia calculadas",
)
TEMPO_BATCH = Summary(
    "ecommerce_spark_tempo_batch_segundos",
    "Tempo de processamento de cada micro-batch Spark",
)


def _ler_json(nome_arquivo, padrao):
    caminho = STATE_DIR / nome_arquivo
    if not caminho.exists():
        return padrao
    with caminho.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def _salvar_json(nome_arquivo, dados):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    caminho = STATE_DIR / nome_arquivo
    temporario = caminho.with_suffix(".tmp")
    with temporario.open("w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2, sort_keys=True)
    temporario.replace(caminho)


@TEMPO_BATCH.time()
def persistir_estado_recomendacao(batch_df, batch_id):
    try:
        transacoes = batch_df.select("id_cliente", "id_produto", "quantidade").collect()
        if not transacoes:
            return

        cliente_produtos = _ler_json("cliente_produtos.json", {})
        coocorrencia = _ler_json("coocorrencia.json", {})
        top_produtos = _ler_json("top_produtos.json", {})

        compras_por_cliente_no_batch = defaultdict(list)
        for linha in transacoes:
            id_cliente = str(linha["id_cliente"])
            id_produto = str(linha["id_produto"])
            quantidade = int(linha["quantidade"] or 0)

            historico_cliente = cliente_produtos.setdefault(id_cliente, {})
            historico_cliente[id_produto] = historico_cliente.get(id_produto, 0) + quantidade
            top_produtos[id_produto] = top_produtos.get(id_produto, 0) + quantidade
            compras_por_cliente_no_batch[id_cliente].append(id_produto)

        for id_cliente, produtos_novos in compras_por_cliente_no_batch.items():
            historico = set(cliente_produtos[id_cliente].keys())
            for produto_novo in produtos_novos:
                relacionados = historico - {produto_novo}
                if not relacionados:
                    continue
                mapa_produto = coocorrencia.setdefault(produto_novo, {})
                for produto_relacionado in relacionados:
                    mapa_produto[produto_relacionado] = mapa_produto.get(produto_relacionado, 0) + 1
                    mapa_inverso = coocorrencia.setdefault(produto_relacionado, {})
                    mapa_inverso[produto_novo] = mapa_inverso.get(produto_novo, 0) + 1

        _salvar_json("cliente_produtos.json", cliente_produtos)
        _salvar_json("coocorrencia.json", coocorrencia)
        _salvar_json("top_produtos.json", top_produtos)

        total_relacoes = sum(len(relacionados) for relacionados in coocorrencia.values())
        METRICA_PROCESSADAS.inc(len(transacoes))
        METRICA_BATCHES.inc()
        GAUGE_CLIENTES.set(len(cliente_produtos))
        GAUGE_RELACOES.set(total_relacoes)

        print(f"Batch {batch_id}: {len(transacoes)} transacoes persistidas para recomendacao.")
    except Exception:
        METRICA_ERROS.inc()
        raise


def processar_streaming():
    start_http_server(config.PROMETHEUS_PORT_SPARK)
    print(f"Servidor Prometheus do Spark na porta {config.PROMETHEUS_PORT_SPARK}")

    spark = (
        SparkSession.builder.appName("EcommerceRealTimeAnalytics")
        .master("local[*]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    schema_transacao = StructType(
        [
            StructField("id_transacao", IntegerType(), True),
            StructField("id_cliente", IntegerType(), True),
            StructField("id_produto", IntegerType(), True),
            StructField("quantidade", IntegerType(), True),
            StructField("timestamp", LongType(), True),
        ]
    )

    print("Conectando ao Kafka para streaming de transacoes...")
    df_stream = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", config.KAFKA_BROKER)
        .option("subscribe", config.KAFKA_TOPIC)
        .option("startingOffsets", "latest")
        .load()
    )

    df_parsed = (
        df_stream.selectExpr("CAST(value AS STRING)")
        .select(from_json(col("value"), schema_transacao).alias("data"))
        .select("data.*")
        .withColumn("timestamp_processamento", current_timestamp())
    )

    top_produtos_console = (
        df_parsed.withWatermark("timestamp_processamento", "1 minute")
        .groupBy(window(col("timestamp_processamento"), "1 minute"), "id_produto")
        .sum("quantidade")
        .withColumnRenamed("sum(quantidade)", "total_vendido")
    )

    query_console = (
        top_produtos_console.writeStream.outputMode("complete")
        .format("console")
        .option("truncate", "false")
        .trigger(processingTime="10 seconds")
        .start()
    )

    query_estado = (
        df_parsed.writeStream.outputMode("append")
        .foreachBatch(persistir_estado_recomendacao)
        .option("checkpointLocation", str(CHECKPOINT_DIR))
        .trigger(processingTime="10 seconds")
        .start()
    )

    spark.streams.awaitAnyTermination()


if __name__ == "__main__":
    processar_streaming()
