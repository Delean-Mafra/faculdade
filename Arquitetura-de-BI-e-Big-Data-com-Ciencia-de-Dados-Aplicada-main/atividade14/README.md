## 1. Introdução

Este projeto desenvolve uma solução de dados para um cenário de e-commerce, lidando com o gerenciamento e a análise de grandes volumes de produtos, preços, avaliações e transações. O objetivo é demonstrar, na prática, a integração de bancos NoSQL, busca distribuída, processamento em tempo real, sistemas de recomendação e monitoramento. 

Todo o desenvolvimento teve como base os conceitos vistos em aula, com destaque para o uso do Elasticsearch como motor de busca e análise, além dos princípios de processamento distribuído. Como vimos, a busca distribuída otimiza a recuperação de informações na rede, enquanto a divisão dos dados em *shards* garante escalabilidade e a replicação assegura a tolerância a falhas.

## 2. Visão Geral da Solução

A principal lição desta atividade é que uma arquitetura de Big Data não se faz com uma única tecnologia; cada componente tem um papel muito bem definido no fluxo de dados.

No projeto, adotamos o Elasticsearch como banco orientado a documentos e motor de busca do catálogo. Os produtos ficam salvos em documentos JSON (contendo nome, categoria, preço e avaliações), organizados em índices que permitem buscas complexas através da *Query DSL*.

Para lidar com o fluxo de transações em tempo real, usamos o Apache Kafka. Ele atua como mensageria, recebendo eventos continuamente e eliminando a dependência de arquivos estáticos. Na ponta do consumo, o Apache Spark Structured Streaming lê esses eventos do Kafka sem interrupções, permitindo análises dinâmicas em janelas de tempo — um contraste claro com o processamento tradicional em *batch*.

A camada de recomendação, por sua vez, cruza o histórico de compras para sugerir itens relevantes ao perfil de cada cliente. Após calcular as recomendações, o sistema consulta o Elasticsearch para exibir os produtos reais (com preço e detalhes) ao consumidor, e não apenas seus códigos de identificação.

Por fim, toda a operação é acompanhada por uma stack de observabilidade: o Prometheus coleta as métricas dos componentes, e o Grafana exibe as informações em dashboards interativos.

## 3. Desenvolvimento

### 3.1 Arquiteturas NoSQL
O passo inicial foi analisar os modelos NoSQL (documentos, chave-valor e colunares) e como eles se encaixariam no e-commerce. Bancos de documentos são excelentes para o catálogo devido à flexibilidade estrutural. O modelo chave-valor seria o ideal para acessos rápidos, como gerenciar carrinhos de compra, enquanto os colunares brilham em análises massivas. Na prática, o Elasticsearch assumiu a posição central, deixando os demais como alternativas arquiteturais teóricas.

### 3.2 Busca Distribuída
Em seguida, indexamos o catálogo no Elasticsearch. A aplicação consegue buscar produtos usando consultas textuais e filtros. Embora a infraestrutura local do projeto seja simplificada, ela ilustra perfeitamente o fluxo de busca. Em um ambiente de produção real, aplicaríamos a fundo os conceitos de aula: índices divididos em *shards* e distribuídos por vários nós, com replicação ativa para garantir alta disponibilidade.

### 3.3 Processamento em Tempo Real
Aqui, criamos um fluxo contínuo onde um produtor gera transações e as envia ao Kafka. O Spark Structured Streaming captura esses dados instantaneamente e executa agregações, calculando o volume de vendas e identificando os produtos mais populares dentro de janelas de tempo específicas. Isso simula fielmente o desafio de processar informações à medida que nascem.

### 3.4 Recomendações Personalizadas
Nesta etapa, unimos a análise de dados ao catálogo. O motor de recomendação avalia o histórico de compras e as relações de coocorrência para sugerir itens com alta chance de conversão. O diferencial arquitetural é o cruzamento direto desses IDs com o Elasticsearch, entregando ao usuário uma vitrine completa e atualizada.

### 3.5 Monitoramento e Alta Disponibilidade
Para fechar a estrutura, o Prometheus foi configurado para capturar métricas da aplicação (transações geradas, buscas, recomendações e tempos de resposta), que são visualizadas no Grafana. Em relação à alta disponibilidade, o projeto roda localmente de forma enxuta (*single-node*). Essa limitação está registrada na documentação, deixando claro que um cenário de produção exigiria um cluster com múltiplos nós e réplicas.

## 4. Fluxo Geral da Arquitetura

O caminho percorrido pelos dados pode ser resumido da seguinte forma:
**Geração de transações** → **Kafka** → **Spark Structured Streaming** (análise) → **Motor de recomendação** → **Elasticsearch** (recuperação de dados) → **Retorno para o usuário** → **Monitoramento (Prometheus/Grafana)**.
Esse pipeline ilustra de forma clara a sinergia entre as ferramentas em um ecossistema Big Data.

## 5. Resultados e Aprendizado

A atividade deixou evidente que lidar com grandes volumes de dados vai muito além do armazenamento. A escolha da tecnologia precisa equilibrar a velocidade da consulta, o processamento contínuo e a escalabilidade.

O Elasticsearch provou ser a ferramenta certa para o catálogo graças à indexação ágil e à flexibilidade da *Query DSL*. O Kafka e o Spark foram essenciais para tirar o projeto do modelo estático e trazê-lo para o tempo real. Já o sistema de recomendação mostrou como dados analíticos geram valor direto para o negócio, tudo monitorado de perto pela dupla Prometheus e Grafana.

Também ficou clara a diferença entre um laboratório acadêmico e o mundo real. Um ambiente de produção exige infraestrutura robusta, múltiplos nós e armazenamento persistente. Aqui, a prioridade foi validar a arquitetura e o papel de cada tecnologia, documentando com transparência as limitações locais.

## 6. Conclusão

A solução desenvolvida cumpre o objetivo de entregar uma arquitetura integrada de dados para e-commerce, passando por NoSQL, busca distribuída, streaming, recomendações e observabilidade.

O principal aprendizado é que o Big Data funciona como um quebra-cabeça de componentes complementares. É preciso adequar o armazenamento ao tipo de dado, usar índices eficientes para buscas, processar eventos no ritmo em que acontecem e converter tudo isso em funcionalidades úteis. O domínio de conceitos como *sharding* e replicação é justamente o que permite transformar um protótipo local em uma arquitetura pronta para ganhar escala no mercado.

## 7. Referências

**AULA 14.** Busca Distribuída e Bancos de Dados em Big Data (Material didático da disciplina). Conteúdo abordado: busca distribuída, Elasticsearch, indexação, Query DSL, *sharding*, replicação, modelos NoSQL e estudo de caso.
