# Relatorio de Pratica Integradora: Ciencia de Dados para Negocios

## 1. Descricao do Processo de Coleta e Preparacao Inicial

### Parte 1: Web Scraping Etico e Robusto

Para a coleta de dados, foi selecionado o site Books to Scrape, uma plataforma projetada especificamente para testes de web scraping. A escolha garantiu que a atividade fosse realizada de forma etica, respeitando os termos de uso.

#### Destaques tecnicos da coleta

- Validacao de permissao: o script utiliza a biblioteca `urllib.robotparser` para consultar o arquivo `robots.txt` do site antes de iniciar, garantindo conformidade com as regras do servidor.
- Tratamento de paginacao: o codigo nao se limita a primeira pagina; ele identifica o botao "Next" e percorre todo o catalogo dinamicamente.
- Robustez no separador: foi utilizado o caractere pipe (`|`) como separador no CSV, em vez da virgula ou ponto e virgula. Essa foi uma decisao estrategica de engenharia de dados, pois titulos de livros frequentemente contem virgulas, o que causaria erros de quebra de colunas (parsing) em ferramentas como Excel ou bancos de dados.

Repositorio com o codigo:

- https://github.com/Delean-Mafra/faculdade/blob/main/coleta_limpeza_e_tratamento_de_dados/coleta_limpeza_e_tratamento_de_dados.ipynb

### Parte 2: Refino com OpenRefine

Apos a geracao do CSV bruto, utilizei o OpenRefine para uma auditoria de qualidade.

- Conversao de encoding: os dados foram convertidos de "UTF-8 com BOM" para "UTF-8". O BOM (Byte Order Mark), em varios cenarios, insere caracteres invisiveis no inicio do arquivo e isso pode causar erros de leitura em scripts Python e no Excel.
- Tipagem de dados: a coluna `preco` foi transformada de texto para o formato numerico, permitindo calculos matematicos imediatos.

## 2. Analise do Script de Tratamento e Visualizacao (Python/Flask)

O segundo script Python representa a etapa de Transformacao e Carga (ETL) e Business Intelligence (BI).

### Intencao do codigo

A intencao principal foi criar um fluxo automatizado que nao apenas limpa os dados, mas tambem gera insights visuais imediatos por meio de um dashboard web local. Em vez de apenas olhar para uma planilha, o usuario interage com uma interface grafica.

### O que o codigo faz e por que

#### Limpeza adicional com Pandas

- Filtra apenas livros com preco superior a R$ 30,00 (`PRECO_MINIMO`), focando em produtos de maior margem.
- Filtra apenas itens "In stock", garantindo que a analise reflita a disponibilidade real do inventario.
- Remove duplicatas remanescentes e trata valores nulos.

#### Calculos estatisticos

- Gera media, mediana e moda dos precos, fundamentais para entender a distribuicao de precos do catalogo.
- Identifica os valores extremos (mais caro e mais barato).

#### Visualizacao de dados (Matplotlib)

- Cria um histograma da distribuicao de precos, permitindo identificar visualmente em qual faixa de valor a maioria dos livros se encontra.

#### Servidor Flask

- O codigo inicia um microservidor web que renderiza um template HTML com os dados processados.
- O grafico e convertido para Base64, permitindo que a imagem seja exibida diretamente no navegador sem precisar de arquivos externos.

### Beneficios dessa abordagem

- Automatizacao: o processo de tratamento e repetivel. Se o site mudar ou novos dados forem coletados, basta rodar o script novamente.
- Portabilidade: ao converter o grafico para Base64 e usar Flask, cria-se uma ferramenta de visualizacao que nao depende de softwares de BI pagos para uma analise rapida.
- Integridade: o uso de blocos `try/except` para salvar o arquivo (tratando erros de permissao) demonstra preocupacao com robustez em ambiente de producao.

## 3. Analise e Reflexao (Relatorio de Fechamento)

### Etapas realizadas

O trabalho percorreu o ciclo completo da Ciencia de Dados:

- Extracao: captura automatizada de dados brutos via scraping.
- Normalizacao: padronizacao de encodings e tipos de dados (OpenRefine).
- Tratamento: filtragem de negocios e remocao de ruidos (Pandas).
- Comunicacao: geracao de relatorio visual (Flask/Matplotlib).

### Desafios e solucoes aplicadas

- Desafio 1 (formatacao de moeda): os precos vinham com simbolos de moeda (ex.: GBP).
  Solucao: implementacao de funcao de normalizacao com substituicao de strings e conversao para `float`.

- Desafio 2 (caracteres especiais): a presenca de virgulas nos titulos ameacava a estrutura do CSV.
  Solucao: substituicao do delimitador padrao pelo pipe (`|`).

- Desafio 3 (encoding): problemas de leitura por conta do formato UTF-8 BOM.
  Solucao: uso do OpenRefine para garantir um arquivo UTF-8 limpo e uso de `encoding='utf-8-sig'` no Python para maior compatibilidade.

### A importancia da qualidade e integridade dos dados

A integridade dos dados e o alicerce de qualquer analise de negocios. Se a etapa de limpeza (Partes 2 e 3) fosse ignorada, as decisoes seriam baseadas em dados distorcidos:

- Livros fora de estoque inflariam a media de precos sem representar receita potencial.
- Titulos duplicados enviesariam moda e mediana.
- Erros de encoding poderiam causar perda de registros inteiros durante o processamento.

Garantir a qualidade dos dados antes da analise evita o fenomeno "Garbage In, Garbage Out". Uma analise so e valiosa se os dados que a sustentam forem precisos, consistentes e confiaveis. Este trabalho demonstrou que grande parte do esforco de um cientista de dados nao esta apenas na analise final, mas na preparacao cuidadosa do insumo.

Repositorio com o codigo:

- https://github.com/Delean-Mafra/faculdade/blob/main/coleta_limpeza_e_tratamento_de_dados/tratamento_de_dados_com_python.py
