import time
import json
import sys
from pathlib import Path

from elasticsearch import Elasticsearch
from prometheus_client import Counter, Summary, start_http_server

import config

es = Elasticsearch(config.ES_HOST, request_timeout=30)
BASE_DIR = Path(__file__).resolve().parent.parent
STATE_DIR = BASE_DIR / config.RECOMMENDATION_STATE_DIR

METRICA_BUSCAS = Counter("ecommerce_buscas_realizadas_total", "Total de buscas no Elasticsearch")
METRICA_RECOMENDACOES = Counter(
    "ecommerce_recomendacoes_total",
    "Total de recomendacoes geradas",
)
TEMPO_BUSCA = Summary(
    "ecommerce_tempo_busca_segundos",
    "Tempo de processamento das buscas",
)
METRICA_ERROS = Counter("ecommerce_api_erros_total", "Total de erros na API de busca e recomendacao")
TEMPO_RECOMENDACAO = Summary(
    "ecommerce_tempo_recomendacao_segundos",
    "Tempo de processamento das recomendacoes",
)


def _ler_estado(nome_arquivo):
    caminho = STATE_DIR / nome_arquivo
    if not caminho.exists():
        return {}
    with caminho.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def escolher_cliente_com_historico():
    cliente_produtos = _ler_estado("cliente_produtos.json")
    if not cliente_produtos:
        return None
    return int(max(cliente_produtos.items(), key=lambda item: sum(item[1].values()))[0])


@TEMPO_BUSCA.time()
def buscar_produtos(termo, max_preco=None, categoria=None):
    METRICA_BUSCAS.inc()
    must_clauses = [{"multi_match": {"query": termo, "fields": ["nome", "categoria"]}}]

    if max_preco is not None:
        must_clauses.append({"range": {"preco": {"lte": max_preco}}})
    if categoria:
        must_clauses.append({"term": {"categoria": categoria}})

    query = {"query": {"bool": {"must": must_clauses}}, "size": 5}
    res = es.search(index=config.ES_INDEX_PRODUTOS, body=query)

    print(f"\n--- Resultados para '{termo}' ---")
    for hit in res["hits"]["hits"]:
        p = hit["_source"]
        print(
            f"ID: {p['id']} | {p['nome']} | {p['categoria']} | "
            f"R$ {p['preco']} | Nota: {p['media_notas']}"
        )


@TEMPO_RECOMENDACAO.time()
def gerar_recomendacao(id_cliente):
    cliente_produtos = _ler_estado("cliente_produtos.json")
    coocorrencia = _ler_estado("coocorrencia.json")
    historico = cliente_produtos.get(str(id_cliente), {})

    if not historico:
        print(
            "Cliente sem historico processado. Gere transacoes no Kafka e mantenha "
            "o Spark Streaming ativo antes de solicitar recomendacoes."
        )
        return

    pontuacao = {}
    produtos_comprados = set(historico.keys())
    for id_produto, quantidade_comprada in historico.items():
        for id_relacionado, peso in coocorrencia.get(id_produto, {}).items():
            if id_relacionado in produtos_comprados:
                continue
            pontuacao[id_relacionado] = pontuacao.get(id_relacionado, 0) + (
                int(peso) * int(quantidade_comprada)
            )

    if not pontuacao:
        print(
            "Ainda nao ha coocorrencia suficiente para recomendar produtos a este cliente. "
            "Continue gerando transacoes reais."
        )
        return

    recomendacoes_ids = [
        int(id_produto)
        for id_produto, _ in sorted(pontuacao.items(), key=lambda item: item[1], reverse=True)[:5]
    ]

    query = {
        "query": {"terms": {"id": recomendacoes_ids}},
        "size": len(recomendacoes_ids),
    }
    res = es.search(index=config.ES_INDEX_PRODUTOS, body=query)
    METRICA_RECOMENDACOES.inc()

    print(f"\n--- Recomendacoes personalizadas para cliente {id_cliente} ---")
    for hit in res["hits"]["hits"]:
        p = hit["_source"]
        print(
            f"Recomendado -> ID {p['id']} | {p['nome']} | {p['categoria']} | "
            f"R$ {p['preco']} | Nota: {p['media_notas']}"
        )


if __name__ == "__main__":
    start_http_server(config.PROMETHEUS_PORT_API)
    print(f"Servidor Prometheus da API na porta {config.PROMETHEUS_PORT_API}")

    time.sleep(2)
    try:
        buscar_produtos("Moda")
        buscar_produtos("Livros", max_preco=100.0)
        id_cliente = int(sys.argv[1]) if len(sys.argv) > 1 else escolher_cliente_com_historico()
        if id_cliente is None:
            print("\nNenhum cliente processado pelo Spark ainda.")
        else:
            gerar_recomendacao(id_cliente)
    except Exception as erro:
        METRICA_ERROS.inc()
        raise erro

    print("\nAPI rodando. Pressione Ctrl+C para encerrar o monitoramento.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
