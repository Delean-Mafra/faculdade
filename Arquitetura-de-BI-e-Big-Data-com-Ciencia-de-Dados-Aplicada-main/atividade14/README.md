# Atividade Pratica 14 - Distribuida e Bancos de Dados em Big Data

## Objetivo

Implementar um cenario de Big Data para e-commerce com banco NoSQL, busca, processamento de eventos em tempo real, recomendacoes personalizadas e monitoramento.

## Demonstracao local x arquitetura distribuida de producao

Este projeto e uma demonstracao academica local. Ele usa tecnologias comuns em arquiteturas distribuidas, mas a infraestrutura do `docker-compose.yml` foi reduzida para caber em uma maquina de desenvolvimento.

Na execucao local:

- O Elasticsearch roda com `discovery.type=single-node`, portanto nao ha cluster real nem replicas.
- O Kafka roda com um broker e fator de replicacao 1.
- O Spark roda com `.master("local[*]")`, portanto usa os nucleos da maquina local, nao um cluster Spark.
- A persistencia analitica da recomendacao usa arquivos JSON em `data/recomendacoes`, uma solucao simples e auditavel para a pratica.

Em producao, a arquitetura equivalente usaria:

- Elasticsearch com multiplos nos, shards e replicas.
- Kafka com multiplos brokers e replicacao.
- Spark em Kubernetes, YARN ou ambiente gerenciado.
- Banco analitico ou NoSQL adicional, como Cassandra, HBase, Redis ou armazenamento colunar, para persistir historicos e agregacoes com alta disponibilidade.

## Arquitetura implementada

```text
Gerador Python
   -> Kafka
   -> Spark Structured Streaming
   -> estado analitico em data/recomendacoes
   -> motor de recomendacao
   -> Elasticsearch
   -> produtos recomendados
```

Componentes:

- **Elasticsearch:** catalogo NoSQL de produtos, precos, categorias e avaliacoes.
- **Kafka:** fila de eventos de transacoes em tempo real.
- **Spark Structured Streaming:** consome o Kafka continuamente, agrega vendas por janela e grava historico/coocorrencia real para recomendacao.
- **Motor de recomendacao:** le os resultados produzidos pelo Spark e consulta o Elasticsearch para enriquecer os produtos recomendados.
- **Prometheus/Grafana:** coletam e exibem metricas de geracao, processamento, buscas, recomendacoes e erros.

## Como a recomendacao funciona

O arquivo `src/3_spark_streaming.py` consome transacoes reais do Kafka. A cada micro-batch, ele atualiza:

- `data/recomendacoes/cliente_produtos.json`: produtos realmente comprados por cliente.
- `data/recomendacoes/coocorrencia.json`: produtos que aparecem no historico do mesmo cliente.
- `data/recomendacoes/top_produtos.json`: volume total vendido por produto.

O arquivo `src/4_busca_recomendacao.py` nao usa mocks. Ele le esse estado persistido pelo Spark, calcula produtos relacionados ao historico real do cliente e consulta o Elasticsearch para obter ID, nome, categoria, preco e media das avaliacoes.

## Como executar

### 1. Subir a infraestrutura

```bash
docker-compose up -d
```

Aguarde de 30 a 60 segundos para Kafka e Elasticsearch iniciarem.

### 2. Instalar dependencias Python

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

### 4. Iniciar o Spark Streaming

Em outro terminal:

```bash
python src/3_spark_streaming.py
```

Esse processo deve ficar ativo. Ele consome o Kafka, imprime agregacoes no console e grava os arquivos em `data/recomendacoes`.

### 5. Gerar transacoes reais no Kafka

Em outro terminal:

```bash
python src/2_gerador_eventos_kafka.py
```

Deixe o gerador rodar por alguns segundos para que existam compras suficientes para coocorrencia.

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

- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

Metricas principais:

- `ecommerce_transacoes_geradas_total`
- `ecommerce_transacoes_processadas_total`
- `ecommerce_buscas_realizadas_total`
- `ecommerce_recomendacoes_total`
- `ecommerce_spark_erros_total`
- `ecommerce_api_erros_total`
- `ecommerce_tempo_busca_segundos`
- `ecommerce_spark_tempo_batch_segundos`

## Auditoria tecnica por requisito

| Requisito | Implementacao | Atendido? |
| :--- | :--- | :--- |
| Arquitetura NoSQL | Elasticsearch implementado como catalogo; Cassandra/Redis/banco colunar apenas discutidos como evolucao de producao. | Parcial |
| Busca distribuida | Consultas reais no Elasticsearch por texto, categoria e preco; ambiente local esta em `single-node`. | Parcial |
| Processamento em tempo real | Kafka recebe transacoes continuamente e Spark Structured Streaming consome o topico em micro-batches. | Sim |
| Processamento distribuido em cluster | Spark executa em `local[*]`, sem cluster real. | Parcial |
| Recomendacoes integradas | Recomendacao baseada em historico/coocorrencia produzidos pelo Spark a partir das transacoes reais do Kafka. | Sim |
| Elasticsearch como catalogo | Produtos, precos, categorias, avaliacoes e media de notas sao indexados e consultados no Elasticsearch. | Sim |
| Prometheus | Producer, Spark e API expoem metricas atualizadas durante a execucao. | Sim |
| Grafana | Dashboard provisionado com metricas do pipeline. | Sim |
| Alta disponibilidade | Arquitetura de producao documentada, mas nao implementada na configuracao local. | Parcial |

## Auditoria por etapa do enunciado

| Etapa | O que foi implementado | Arquivos | Status | Limitacao |
| :--- | :--- | :--- | :--- | :--- |
| 1. Arquiteturas NoSQL | Uso real do Elasticsearch como banco de documentos e explicacao de alternativas para producao. | `docker-compose.yml`, `src/1_setup_elasticsearch.py`, `README.md` | Parcial | Apenas Elasticsearch local single-node foi implementado. |
| 2. Busca distribuida | Busca de produtos por termo, preco e categoria usando Elasticsearch. | `src/4_busca_recomendacao.py` | Parcial | A ferramenta e distribuivel, mas a instancia local nao e um cluster. |
| 3. Pipeline de analise em tempo real | Gerador envia transacoes ao Kafka; Spark consome continuamente e atualiza agregacoes/historico. | `src/2_gerador_eventos_kafka.py`, `src/3_spark_streaming.py` | Sim | Executa localmente, nao em cluster Spark. |
| 4. Integracao com e-commerce | Motor de recomendacao usa dados processados pelo Spark e busca metadados no Elasticsearch. | `src/3_spark_streaming.py`, `src/4_busca_recomendacao.py` | Sim | Persistencia analitica e simples, baseada em JSON local. |
| 5. Monitoramento e disponibilidade | Prometheus coleta metricas e Grafana apresenta dashboard. HA e descrita para producao. | `prometheus/prometheus.yml`, `grafana/dashboards/ecommerce_dashboard.json`, `README.md` | Parcial | Monitoramento local existe; alta disponibilidade nao foi implementada localmente. |

## Fluxo validado logicamente

1. Um evento de compra e criado em `src/2_gerador_eventos_kafka.py`.
2. O evento e enviado ao topico Kafka `ecommerce_transacoes`.
3. `src/3_spark_streaming.py` consome o topico com Spark Structured Streaming.
4. O Spark calcula agregacoes de vendas e atualiza historico/coocorrencia.
5. Os resultados ficam disponiveis em `data/recomendacoes`.
6. `src/4_busca_recomendacao.py` identifica produtos relacionados ao historico real do cliente.
7. O Elasticsearch fornece os dados completos dos produtos recomendados.
8. Prometheus coleta metricas do producer, Spark e API.
9. Grafana apresenta essas metricas no dashboard provisionado.
