# Atividade Prática 14 – Distribuída e Bancos de Dados em Big Data

## 1. Introdução

A atividade propõe o desenvolvimento de uma solução para um cenário de e-commerce, considerando o gerenciamento e a análise de grandes volumes de produtos, preços, avaliações e transações. O projeto foi estruturado para demonstrar, de forma integrada, conceitos de bancos de dados NoSQL, busca distribuída, processamento de dados em tempo real, recomendações personalizadas e monitoramento.

O desenvolvimento foi baseado nos conceitos apresentados na aula, especialmente na utilização do Elasticsearch como mecanismo de busca e análise, nos modelos de bancos NoSQL e nos conceitos de sharding, replicação e processamento distribuído. A aula destaca que a busca distribuída permite recuperar informações de diferentes nós de uma rede com maior eficiência e que a divisão dos dados em shards contribui para a escalabilidade, enquanto a replicação aumenta a disponibilidade e a tolerância a falhas.

## 2. Entendimento geral da solução

O entendimento obtido a partir da atividade é que uma arquitetura de Big Data não depende de uma única tecnologia. Cada componente exerce uma função específica dentro do fluxo de dados.

No projeto, o Elasticsearch foi utilizado como banco orientado a documentos e mecanismo de busca do catálogo de produtos. Os produtos são armazenados em documentos JSON, contendo informações como nome, categoria, preço e avaliações. A utilização de índices permite organizar os documentos e realizar consultas com a Query DSL, conceito apresentado na aula.

Para representar o fluxo de transações em tempo real, foi utilizado o Apache Kafka como mecanismo de mensageria. As transações são produzidas continuamente e enviadas para um tópico, evitando que o processamento fique dependente de arquivos estáticos.

O Apache Spark Structured Streaming foi utilizado para consumir os eventos do Kafka continuamente e realizar análises sobre as transações. Dessa forma, o projeto diferencia o processamento em tempo real do processamento batch e demonstra a aplicação de janelas de tempo para acompanhar o comportamento das vendas.

A camada de recomendação utiliza o histórico de compras processado para identificar produtos relacionados ao comportamento do cliente. Após obter os produtos recomendados, o Elasticsearch é consultado para recuperar seus dados cadastrais, permitindo apresentar ao consumidor informações como nome, categoria, preço e avaliação.

Por fim, Prometheus e Grafana foram utilizados para monitorar o comportamento da aplicação. O Prometheus coleta métricas expostas pelos componentes da solução, enquanto o Grafana apresenta essas informações em dashboards, facilitando o acompanhamento da operação.

## 3. Desenvolvimento da solução

### 3.1 Arquiteturas NoSQL

A primeira etapa consistiu em compreender os principais modelos de bancos NoSQL e relacioná-los ao cenário de e-commerce. Foram considerados bancos orientados a documentos, chave-valor e colunares.

O modelo orientado a documentos é adequado ao catálogo porque permite representar produtos e avaliações em estruturas flexíveis, normalmente em JSON ou BSON. O modelo chave-valor pode ser utilizado para informações que exigem acesso rápido, como sessões e carrinhos. Já o modelo colunar é adequado a grandes volumes de dados utilizados em análises.

Na implementação principal, o Elasticsearch foi adotado como componente efetivo da arquitetura, enquanto os demais modelos foram considerados como alternativas arquiteturais para funções específicas.

### 3.2 Busca distribuída

Na segunda etapa, o catálogo foi indexado no Elasticsearch. Cada produto possui seus atributos e avaliações armazenados como um documento. A aplicação utiliza consultas textuais e filtros para localizar produtos por nome, categoria e preço.

A aula apresenta o Elasticsearch como um mecanismo de busca distribuído, no qual os índices podem ser divididos em shards e distribuídos entre nós. Em uma implantação de produção, a replicação desses shards também pode ser utilizada para aumentar a disponibilidade e a tolerância a falhas.

Neste projeto acadêmico, a infraestrutura local utiliza uma configuração simplificada. Portanto, a aplicação demonstra o funcionamento da tecnologia e do fluxo de busca, mas não simula um cluster de múltiplos nós em produção.

### 3.3 Processamento em tempo real

Na terceira etapa, foi implementado um fluxo contínuo de eventos. Um produtor gera transações de forma incremental e as envia ao Kafka. O Spark Structured Streaming recebe esses eventos continuamente e executa as transformações e agregações definidas no pipeline.

Entre os resultados analisados estão a quantidade de vendas e a identificação dos produtos com maior volume de comercialização dentro de janelas de tempo. Essa abordagem se aproxima do cenário proposto pela atividade, no qual as transações precisam ser processadas à medida que são geradas.

### 3.4 Recomendações personalizadas

A quarta etapa integra os dados analíticos com o catálogo de produtos. A lógica de recomendação considera o histórico de compras do cliente e utiliza relações de coocorrência entre produtos para identificar itens potencialmente relevantes.

Os identificadores dos produtos recomendados são então utilizados em uma consulta ao Elasticsearch. Dessa forma, a recomendação não é apresentada apenas como uma lista de identificadores, mas como produtos reais do catálogo, com seus respectivos dados.

### 3.5 Monitoramento e alta disponibilidade

Na quinta etapa, foram utilizadas métricas expostas pela aplicação e coletadas pelo Prometheus. Entre os indicadores acompanhados estão transações geradas, buscas realizadas, recomendações e tempos de processamento. O Grafana utiliza o Prometheus como fonte de dados para apresentar os indicadores em dashboards.

Quanto à alta disponibilidade, foram estudados os conceitos de replicação e sharding apresentados na aula. Em ambiente de produção, seria necessário utilizar múltiplos nós e réplicas para reduzir o impacto de falhas. Como o projeto é executado em ambiente local, a infraestrutura foi simplificada e essa limitação é registrada na documentação, sem afirmar que um ambiente single-node possui alta disponibilidade real.

## 4. Fluxo geral da arquitetura

O fluxo desenvolvido pode ser resumido da seguinte forma:

**Geração de transações → Kafka → Spark Structured Streaming → processamento analítico → mecanismo de recomendação → Elasticsearch → resultados para o e-commerce → Prometheus/Grafana para monitoramento.**

Esse fluxo permite visualizar como diferentes tecnologias podem trabalhar conjuntamente em uma arquitetura orientada a Big Data.

## 5. Resultados e aprendizado

A atividade permitiu compreender que o tratamento de grandes volumes de dados exige mais do que apenas armazenar informações. É necessário escolher tecnologias adequadas para cada necessidade, considerando características como escalabilidade, velocidade de consulta, processamento contínuo e disponibilidade.

O Elasticsearch mostrou-se adequado à busca de produtos por sua capacidade de indexação e utilização da Query DSL. O Kafka permitiu representar a entrada contínua de eventos, enquanto o Spark Structured Streaming possibilitou realizar análises sem depender exclusivamente de processamento batch. A integração com o mecanismo de recomendação demonstrou como os resultados analíticos podem apoiar funcionalidades de negócio. O monitoramento com Prometheus e Grafana complementou a solução ao permitir observar o comportamento do pipeline.

Também foi possível compreender a diferença entre uma demonstração acadêmica e uma arquitetura de produção. Em produção, seria necessário ampliar a infraestrutura com múltiplos nós, replicação, armazenamento persistente e mecanismos de tolerância a falhas. No ambiente local utilizado para a atividade, a prioridade foi demonstrar corretamente o fluxo e o papel de cada tecnologia, documentando as limitações existentes.

## 6. Conclusão

A solução desenvolvida atende ao objetivo de demonstrar uma arquitetura integrada de dados para um cenário de e-commerce, utilizando NoSQL, busca distribuída, processamento em tempo real, recomendações e monitoramento.

O principal entendimento obtido foi que Big Data envolve a combinação de diferentes componentes para atender necessidades distintas. O armazenamento deve ser adequado ao tipo de dado, a busca precisa utilizar mecanismos de indexação eficientes, o processamento deve conseguir acompanhar o fluxo de eventos e os resultados precisam ser integrados ao negócio. Além disso, conceitos como sharding, replicação, escalabilidade e monitoramento são fundamentais para transformar uma solução experimental em uma arquitetura preparada para ambientes de maior escala.

## 7. Referência utilizada

AULA 14. **Busca Distribuída e Bancos de Dados em Big Data**. Material didático da disciplina. O conteúdo aborda busca distribuída, Elasticsearch, indexação, Query DSL, sharding, replicação, modelos NoSQL e estudo de caso com Elasticsearch.
