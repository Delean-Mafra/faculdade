import random
import time

from elasticsearch import Elasticsearch, helpers
from faker import Faker

import config

fake = Faker("pt_BR")
es = Elasticsearch(config.ES_HOST, request_timeout=30)


def aguardar_elasticsearch(tentativas=30):
    for tentativa in range(1, tentativas + 1):
        if es.ping():
            return
        print(f"Aguardando Elasticsearch... tentativa {tentativa}/{tentativas}")
        time.sleep(2)
    raise RuntimeError("Elasticsearch indisponivel. Verifique se o Docker Compose esta ativo.")


def criar_indice():
    mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "integer"},
                "nome": {"type": "text"},
                "categoria": {"type": "keyword"},
                "preco": {"type": "float"},
                "avaliacoes": {
                    "type": "nested",
                    "properties": {
                        "nota": {"type": "integer"},
                        "comentario": {"type": "text"},
                    },
                },
                "media_notas": {"type": "float"},
            }
        }
    }

    if es.indices.exists(index=config.ES_INDEX_PRODUTOS):
        es.indices.delete(index=config.ES_INDEX_PRODUTOS)
    es.indices.create(index=config.ES_INDEX_PRODUTOS, body=mapping)
    print(f"Indice '{config.ES_INDEX_PRODUTOS}' criado com sucesso.")


def gerar_produtos(qtd=1000):
    categorias = ["Eletronicos", "Casa", "Moda", "Livros", "Beleza"]
    actions = []

    for i in range(1, qtd + 1):
        num_avaliacoes = random.randint(0, 5)
        avaliacoes = []
        soma_notas = 0

        for _ in range(num_avaliacoes):
            nota = random.randint(1, 5)
            soma_notas += nota
            avaliacoes.append({"nota": nota, "comentario": fake.sentence()})

        media = soma_notas / num_avaliacoes if num_avaliacoes else 0
        doc = {
            "id": i,
            "nome": f"{fake.word().capitalize()} {fake.word().capitalize()}",
            "categoria": random.choice(categorias),
            "preco": round(random.uniform(10.0, 2000.0), 2),
            "avaliacoes": avaliacoes,
            "media_notas": round(media, 2),
        }

        actions.append({"_index": config.ES_INDEX_PRODUTOS, "_id": i, "_source": doc})

    helpers.bulk(es, actions)
    es.indices.refresh(index=config.ES_INDEX_PRODUTOS)
    print(f"{qtd} produtos indexados para a simulacao academica.")


if __name__ == "__main__":
    aguardar_elasticsearch()
    criar_indice()
    gerar_produtos(1000)
