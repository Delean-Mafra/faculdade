# Atividade Pratica 14 - Distribuida e Bancos de Dados em Big Data

## Objetivo

Implementar um cenario de Big Data para e-commerce com banco NoSQL, busca distribuida, processamento de eventos em tempo real, recomendacoes personalizadas, monitoramento e demonstracao de disponibilidade por replicacao.

## Arquitetura implementada

```text
Gerador Python
   -> Kafka com 3 brokers
   -> Spark master + workers
   -> estado analitico em data/recomendacoes
   -> motor de recomendacao
   -> Elasticsearch com 3 nos
   -> produtos recomendados
   -> Prometheus/Grafana
```

Componentes:

- **Elasticsearch:** catalogo NoSQL orientado a documentos com 3 nos, 3 shards e 1 replica para o indice de produtos.
- **Kafka:** cluster com 3 brokers, fator de replicacao 3 e `min.insync.replicas=2`.
- **Spark:** master e 2 workers no Docker Compose. O script tambem pode rodar em modo local para facilitar testes.
- **Recomendacao:** baseada em historico e coocorrencia produzidos pelo Spark a partir das transacoes reais do Kafka.
- **Prometheus/Grafana:** metricas e dashboard para geracao, processamento, buscas, recomendacoes e erros.

## Observacao sobre ambiente local

O projeto agora inclui uma demonstracao distribuida real via Docker Compose: Elasticsearch com multiplos nos, Kafka com multiplos brokers e Spark com master/workers.

Ainda assim, por estar tudo em uma unica maquina, a disponibilidade e limitada pelo host fisico. Em producao, esses nos ficariam em maquinas ou zonas diferentes, com volumes persistentes, politicas de reinicio, orquestracao e observabilidade mais robusta.

## Como a recomendacao funciona

O arquivo `src/3_spark_streaming.py` consome transacoes reais do Kafka. A cada micro-batch, ele atualiza:

- `data/recomendacoes/cliente_produtos.json`: produtos comprados por cliente.
- `data/recomendacoes/coocorrencia.json`: produtos que aparecem no historico do mesmo cliente.
- `data/recomendacoes/top_produtos.json`: volume total vendido por produto.

O arquivo `src/4_busca_recomendacao.py` le esse estado processado pelo Spark, calcula os produtos relacionados ao historico real do cliente e consulta o Elasticsearch para obter ID, nome, categoria, preco e media das avaliacoes.

## Como executar

### 1. Subir a infraestrutura distribuida

```bash
docker compose up -d
```

Servicos principais:

- Elasticsearch: `http://localhost:9200`
- Kafka brokers externos: `localhost:9092,localhost:9093,localhost:9094`
- Spark master UI: `http://localhost:8080`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`

### 2. Instalar dependencias Python no host

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

No Linux/macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Indexar o catalogo no Elasticsearch

```bash
python src/1_setup_elasticsearch.py
```

O indice e criado com 3 shards e 1 replica, permitindo distribuicao e copia dos dados entre os nos Elasticsearch.

### 4. Iniciar o Spark Streaming no cluster Docker

Execute o job a partir do container `spark-master`, usando os enderecos internos da rede Docker:

```bash
docker compose exec spark-master bash -lc "pip install prometheus-client && SPARK_MASTER=spark://spark-master:7077 KAFKA_BROKER=kafka1:29092,kafka2:29092,kafka3:29092 ES_HOST=http://es01:9200 spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 /app/src/3_spark_streaming.py"
```

Esse processo deve ficar ativo. Ele consome o Kafka continuamente, imprime agregacoes no console e grava os arquivos em `data/recomendacoes`.

Modo alternativo para teste local, sem usar os workers Docker:

```bash
python src/3_spark_streaming.py
```

### 5. Gerar transacoes reais no Kafka

Em outro terminal:

```bash
python src/2_gerador_eventos_kafka.py
```

O producer usa os tres brokers configurados em `config.py` e confirma mensagens com `acks=all`.

### 6. Executar buscas e recomendacoes

Em outro terminal:

```bash
python src/4_busca_recomendacao.py
```

Sem argumento, o script escolhe um cliente que ja tenha historico processado pelo Spark. Para consultar um cliente especifico:

```bash
python src/4_busca_recomendacao.py 42
```

## Monitoramento

Metricas principais:

- `ecommerce_transacoes_geradas_total`
- `ecommerce_transacoes_processadas_total`
- `ecommerce_buscas_realizadas_total`
- `ecommerce_recomendacoes_total`
- `ecommerce_spark_erros_total`
- `ecommerce_api_erros_total`
- `ecommerce_tempo_busca_segundos`
- `ecommerce_spark_tempo_batch_segundos`

O Prometheus coleta:

- Producer Python na porta `8001`.
- API/recomendacao na porta `8002`.
- Spark streaming na porta `8003`.

O Grafana provisiona automaticamente o dashboard `E-Commerce Big Data Monitoring`.

## Auditoria tecnica por requisito

| Requisito | Implementacao | Atendido? |
| :--- | :--- | :--- |
| Banco de dados NoSQL | Elasticsearch armazena produtos, categorias, precos, avaliacoes e media de notas. | Sim |
| Arquiteturas NoSQL | README explica uso de documentos e contextualiza alternativas como chave-valor/colunar para producao. | Sim |
| Busca distribuida | Elasticsearch roda com 3 nos; indice criado com 3 shards e 1 replica. | Sim |
| Busca por preco/categoria/texto | `src/4_busca_recomendacao.py` usa `multi_match`, `range` e `term`. | Sim |
| Apache Spark/Flink | Spark Structured Streaming implementado. | Sim |
| Pipeline em tempo real | Kafka recebe eventos continuamente e Spark consome via `readStream`. | Sim |
| Processamento distribuido | Docker Compose inclui Spark master e 2 workers; README mostra execucao via `spark-submit` no cluster. | Sim |
| Recomendacoes personalizadas | Baseadas em historico/coocorrencia produzidos pelo Spark a partir de transacoes reais. | Sim |
| Integracao com catalogo | Recomendacao consulta Elasticsearch para enriquecer os produtos recomendados. | Sim |
| Prometheus | Producer, Spark e API expoem metricas. | Sim |
| Grafana | Dashboard provisionado. | Sim |
| Alta disponibilidade | Kafka tem 3 brokers e replicacao 3; Elasticsearch tem 3 nos e replica. | Sim, em demonstracao local |

## Auditoria por etapa do enunciado

| Etapa | O que foi implementado | Arquivos | Status | Limitacao |
| :--- | :--- | :--- | :--- | :--- |
| 1. Arquiteturas NoSQL | Elasticsearch distribuido como banco de documentos; alternativas NoSQL discutidas. | `docker-compose.yml`, `src/1_setup_elasticsearch.py`, `README.md` | Sim | Cluster roda em uma unica maquina local. |
| 2. Busca distribuida | Busca em Elasticsearch com 3 nos, shards e replica. | `docker-compose.yml`, `src/1_setup_elasticsearch.py`, `src/4_busca_recomendacao.py` | Sim | Demonstracao local, nao multi-host. |
| 3. Pipeline de analise em tempo real | Gerador envia transacoes ao Kafka; Spark consome continuamente e atualiza agregacoes/historico. | `src/2_gerador_eventos_kafka.py`, `src/3_spark_streaming.py` | Sim | Workers Docker compartilham o mesmo host fisico. |
| 4. Integracao com e-commerce | Motor de recomendacao usa dados processados pelo Spark e busca metadados no Elasticsearch. | `src/3_spark_streaming.py`, `src/4_busca_recomendacao.py` | Sim | Persistencia analitica simples em JSON local. |
| 5. Monitoramento e alta disponibilidade | Prometheus/Grafana monitoram; Kafka e Elasticsearch possuem replicacao no Compose. | `docker-compose.yml`, `prometheus/prometheus.yml`, `grafana/dashboards/ecommerce_dashboard.json` | Sim, em demonstracao local | HA real de producao exigiria hosts/zonas diferentes e volumes persistentes. |

## Fluxo validado logicamente

1. Um evento de compra e criado em `src/2_gerador_eventos_kafka.py`.
2. O evento e enviado ao topico Kafka `ecommerce_transacoes` no cluster de 3 brokers.
3. `src/3_spark_streaming.py` consome o topico com Spark Structured Streaming.
4. O Spark calcula agregacoes de vendas e atualiza historico/coocorrencia.
5. Os resultados ficam disponiveis em `data/recomendacoes`.
6. `src/4_busca_recomendacao.py` identifica produtos relacionados ao historico real do cliente.
7. O Elasticsearch fornece os dados completos dos produtos recomendados a partir do catalogo replicado.
8. Prometheus coleta metricas do producer, Spark e API.
9. Grafana apresenta essas metricas no dashboard provisionado.
