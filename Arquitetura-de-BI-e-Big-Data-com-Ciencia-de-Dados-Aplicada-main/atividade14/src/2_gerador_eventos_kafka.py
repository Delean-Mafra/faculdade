import json
import random
import time

from confluent_kafka import Producer
from prometheus_client import Counter, start_http_server

import config

METRICA_TRANSACOES = Counter(
    "ecommerce_transacoes_geradas_total",
    "Total de transacoes enviadas ao Kafka",
)


def acked(err, msg):
    if err is not None:
        print(f"Falha ao entregar mensagem: {err}")
        return
    METRICA_TRANSACOES.inc()


def iniciar_stream():
    start_http_server(config.PROMETHEUS_PORT_PRODUCER)
    print(f"Servidor Prometheus do producer na porta {config.PROMETHEUS_PORT_PRODUCER}")

    producer = Producer(
        {
            "bootstrap.servers": config.KAFKA_BROKER,
            "acks": "all",
            "enable.idempotence": True,
        }
    )
    print("Gerando transacoes em tempo real. Pressione Ctrl+C para parar.")

    try:
        transacao_id = 1
        while True:
            evento = {
                "id_transacao": transacao_id,
                "id_cliente": random.randint(1, 100),
                "id_produto": random.randint(1, 1000),
                "quantidade": random.randint(1, 3),
                "timestamp": int(time.time() * 1000),
            }
            producer.produce(
                config.KAFKA_TOPIC,
                key=str(evento["id_cliente"]),
                value=json.dumps(evento),
                callback=acked,
            )
            producer.poll(0)
            transacao_id += 1
            time.sleep(random.uniform(0.1, 0.5))
    except KeyboardInterrupt:
        print("Encerrando gerador.")
    finally:
        producer.flush()


if __name__ == "__main__":
    iniciar_stream()
