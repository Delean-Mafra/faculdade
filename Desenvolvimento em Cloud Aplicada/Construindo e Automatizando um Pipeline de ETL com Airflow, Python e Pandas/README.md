# Pipeline ETL com Apache Airflow: Automatização de Fluxos de Dados

## RESUMO

Neste estudo, apresento em detalhes a criação de um exercício prático que visa construir e automatizar um fluxo de Extração, Transformação e Carga (ETL). Usando o Apache Airflow para orquestrar o processo, o projeto combina as funcionalidades das bibliotecas Python e Pandas no tratamento dos dados. O fluxo de trabalho criado espelha uma situação do mundo real, pegando arquivos CSV e JSON de um local de dados, fazendo modificações para juntar e padronizar as informações e, no final, colocando o resultado em um sistema de armazenamento. A documentação descreve a estrutura do Grafo Acíclico Dirigido (DAG), a lógica por trás de cada etapa (extração, transformação, carregamento e limpeza), o uso de XComs para a troca de informações entre as etapas, a inclusão de métodos para garantir a confiabilidade, como repetições, e a definição de diferentes caminhos no fluxo de execução. O produto final é um processo automático, forte e eficaz, que mostra como os conceitos teóricos aprendidos sobre a orquestração de fluxos de dados em ambientes de nuvem podem ser aplicados na prática.

## SUMÁRIO

1. [INTRODUÇÃO](#1-introdução)
2. [DESENVOLVIMENTO](#2-desenvolvimento)
   - 2.1 [Estrutura do Pipeline de ETL no Airflow](#21-estrutura-do-pipeline-de-etl-no-airflow)
   - 2.2 [Etapa de Extração de Dados](#22-etapa-de-extração-de-dados)
   - 2.3 [Etapa de Transformação de Dados](#23-etapa-de-transformação-de-dados)
   - 2.4 [Etapa de Carregamento de Dados](#24-etapa-de-carregamento-de-dados)
   - 2.5 [Confiabilidade e Limpeza do Pipeline](#25-confiabilidade-e-limpeza-do-pipeline)
3. [CONCLUSÃO](#3-conclusão)

---

## 1 INTRODUÇÃO

Na área atual da engenharia de dados, a administração de condutos de dados é imprescindível. A metodologia de Extração, Conversão e Inserção (ETL) organiza o trânsito de dados desde a sua proveniência até a localização final, permitindo sua aplicação em análises e decisões. Utilitários de coordenação de fluxos de trabalho, como o Apache Airflow, são cruciais neste sistema, administrando, programando e supervisionando a efetivação de condutos complexos. Notavelmente, o Airflow não efetua as ações de ETL em si, mas coordena serviços e roteiros externos que realizam a maior parte do trabalho.

Esta atividade prática visa aplicar os conceitos teóricos estudados, construindo um pipeline de ETL funcional. Para tal, serão utilizadas as bibliotecas Python e Pandas, integradas ao Airflow, para realizar as etapas de extração e transformação. O objetivo é desenvolver um Grafo Acíclico Dirigido (DAG) que automatize a coleta de arquivos CSV e JSON de um repositório, consolide essas informações e as carregue em um destino final.

Essa atividade detalha todas as fases do desenvolvimento do projeto. A seção de Desenvolvimento aborda a estrutura do DAG, a lógica por trás de cada tarefa implementada, as estratégias para garantir a confiabilidade do processo e a limpeza dos artefatos temporários. Por fim, a Conclusão resume os resultados alcançados e as habilidades práticas desenvolvidas durante a atividade.

---

## 2 DESENVOLVIMENTO

O desenvolvimento do projeto seguiu as etapas descritas no enunciado da atividade, resultando em um DAG funcional que simula um processo de ETL de ponta a ponta. As seções a seguir detalham as decisões de implementação para cada fase do pipeline.

### 2.1 Estrutura do Pipeline de ETL no Airflow

O pipeline foi estruturado como um DAG no Airflow, que é a unidade fundamental para a definição de workflows na ferramenta. O DAG foi projetado para seguir as boas práticas recomendadas, como a criação de tarefas atômicas e independentes, onde cada uma é responsável por uma ação mínima e específica.

O fluxo de trabalho foi definido com as seguintes tarefas principais:

- **Extração**: Uma tarefa responsável por baixar os arquivos de dados (CSVs e JSONs) de um repositório externo, como o AWS S3.

- **Transformação**: Uma tarefa que utiliza a biblioteca Pandas para ler os arquivos baixados, unificar os múltiplos CSVs em um único DataFrame e enriquecê-lo com as informações dos arquivos JSON.

- **Carregamento**: Uma tarefa que persiste os dados transformados em um sistema de armazenamento, como um banco de dados relacional.

- **Limpeza**: Uma tarefa final responsável por remover todos os arquivos e diretórios temporários criados durante a execução, garantindo que o worker não acumule dados desnecessários.

A orquestração dessas tarefas é realizada pelo Airflow, que gerencia as dependências entre elas, garantindo que sejam executadas na ordem correta. A comunicação de metadados entre as tarefas, como o nome dos arquivos temporários, é realizada por meio do mecanismo XCom do Airflow.

### 2.2 Etapa de Extração de Dados

A primeira etapa do pipeline consiste na extração dos dados brutos. Conforme solicitado, esta tarefa foi implementada para interagir com um repositório de dados externo. Para simular uma interação com a nuvem, utilizou-se o S3Hook do Airflow, que facilita a conexão com o serviço AWS S3.

A lógica da tarefa de extração, encapsulada em uma função Python e executada por um PythonOperator, realiza os seguintes passos:

**Instanciação do Hook**: O S3Hook é instanciado, utilizando uma conexão pré-configurada na interface do Airflow para autenticação segura.

**Seleção de Arquivos**: A função define um intervalo de datas para processamento. Com base nesse intervalo, ela busca por arquivos CSV e JSON correspondentes no bucket do S3. Essa abordagem permite a implementação tanto de cargas completas (processando um período extenso) quanto de cargas incrementais (processando apenas o dia corrente).

**Download dos Arquivos**: Utilizando o hook, os arquivos selecionados são baixados para um diretório temporário no worker do Airflow. Os nomes desses arquivos são passados para a próxima tarefa via XCom.

Essa abordagem mantém a tarefa de extração atômica, com a única responsabilidade de disponibilizar os dados brutos para a etapa seguinte do pipeline.

### 2.3 Etapa de Transformação de Dados

Após a extração, os dados brutos precisam ser processados. A tarefa de transformação foi implementada utilizando um PythonOperator que executa uma função para manipular os dados com a biblioteca Pandas, conhecida por sua eficiência em processamento de dados em memória.

O processo de transformação segue os seguintes passos:

**Recebimento de Dados**: A função recebe, via XCom, a lista de arquivos CSV e JSON que foram baixados pela tarefa de extração.

**Concatenação de CSVs**: Os múltiplos arquivos CSV, que representam dados diários, são lidos e concatenados em um único DataFrame do Pandas.

**Processamento de JSONs**: Os arquivos JSON, contendo metadados ou informações complementares, são lidos e processados.

**Join de Dados**: O DataFrame principal (originado dos CSVs) é enriquecido por meio de operações de join com os dados extraídos dos arquivos JSON, criando uma tabela unificada e consolidada.

**Limpeza e Formatação**: São aplicadas transformações adicionais, como limpeza de valores nulos, padronização de tipos de dados e renomeação de colunas.

**Salvamento Temporário**: O DataFrame transformado é salvo como um único arquivo CSV em um diretório temporário. O caminho para este novo arquivo é então enviado via XCom para a tarefa de carregamento.

Ao delegar transformações mais pesadas a serviços externos como Spark ou AWS Glue em cenários de grande volume de dados, esta etapa evita a sobrecarga do worker do Airflow, uma boa prática recomendada.

### 2.4 Etapa de Carregamento de Dados

A etapa final do fluxo de ETL é o carregamento (Load). O objetivo desta tarefa é persistir os dados transformados e consolidados em um sistema de destino, como um banco de dados, para que possam ser consumidos por outras aplicações ou para fins de análise.

A implementação desta tarefa considerou as seguintes ações:

**Recebimento do Arquivo Final**: A tarefa obtém o caminho do arquivo CSV final da etapa de transformação por meio do XCom.

**Conexão com o Banco de Dados**: Utilizando um hook apropriado, como o PostgresHook, a tarefa estabelece uma conexão com o banco de dados de destino. O uso de hooks para interações externas é uma boa prática que evita a sobrecarga do scheduler do Airflow.

**Inserção dos Dados**: A inserção dos dados é realizada de forma eficiente. Em vez de inserir linha por linha, o que seria ineficiente, foi utilizada uma operação de COPY (ou similar, dependendo do SGBD), que carrega os dados diretamente do arquivo CSV para a tabela de destino. O comando SQL para essa operação pode ser gerenciado por meio de um arquivo de template, o que melhora a organização do código.

Para evitar a duplicação de dados em cargas completas (full), podem ser utilizadas estratégias como upserts (quando o banco de dados suporta) ou a criação de snapshots versionados pela data de execução.

### 2.5 Confiabilidade e Limpeza do Pipeline

Para garantir que meu pipeline fosse robusto e resiliente a falhas, implementei estratégias de retry. Em ambientes distribuídos, sei que uma tarefa pode falhar por motivos transitórios, como a interrupção de um worker. Por isso, configurei retries no DAG, permitindo que o Airflow tentasse executar novamente uma tarefa com falha, aumentando assim a chance de sucesso do pipeline sem que eu precisasse intervir manualmente. Além disso, para evitar execuções múltiplas e indesejadas, especialmente em cargas incrementais, defini um agendamento apropriado e utilizei o parâmetro catchup=False.

Finalmente, implementei a tarefa de limpeza (cleanup) para garantir a higiene do ambiente de execução. Essa tarefa ficou responsável por remover todos os diretórios e arquivos temporários criados durante o processo. Uma configuração essencial que adotei foi o uso da regra trigger_rule="all_done". Com isso, garanti que a limpeza fosse executada ao final do fluxo, independentemente de as tarefas anteriores terem sido bem-sucedidas ou não, evitando que o worker acumulasse arquivos residuais.

---

## 3 CONCLUSÃO

Ao colocar a mão na massa nesta tarefa prática, consegui aplicar e consolidar o que aprendi na teoria sobre como organizar processos de ETL com o Apache Airflow. Criar o fluxo de trabalho, desde buscar os dados até colocá-los no destino correto, me mostrou como o Airflow é flexível e poderoso quando utilizado em conjunto com ferramentas do ecossistema Python, como a biblioteca Pandas.

O projeto alcançou todos os objetivos que eu havia definido, resultando em um DAG que não apenas executa sozinho as fases de ETL, mas também segue as melhores práticas do mercado. Estruturei tarefas pequenas e independentes, controlei conexões externas por meio de hooks, implementei estratégias de retry e garanti que o ambiente de trabalho permanecesse limpo. A experiência reforçou para mim que a capacidade do Airflow de se integrar a diversos serviços externos o torna uma ferramenta essencial e amplamente utilizada para acelerar e automatizar processos de ETL nas empresas.

---

*Desenvolvido por: Delean Mafra*  
*Data: 10 de outubro de 2025*  
*Versão: 1.1*
