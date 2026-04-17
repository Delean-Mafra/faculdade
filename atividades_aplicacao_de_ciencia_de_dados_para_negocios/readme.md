# Este repositorio contem todas as atividades praticas da aula Aplicação de Ciência de Dados para Negócios



Prática Integradora em Ciência de Dados para Negócios


Atividade Prática 1 – Análise de Dados com Pandas em Python



Objetivos


Introduzir o uso da biblioteca Pandas para manipulação e análise de dados.
Utilizar técnicas de visualização de dados para apoiar a tomada de decisões.
Aplicar conceitos de transformação de dados para gerar insights relevantes para os negócios.


Materiais, Métodos e Ferramentas


Computador com acesso ao Google Colab (recomendado) ou ambiente de desenvolvimento Python (IDE como Visual Studio Code).
Navegador web (recomendado: Google Chrome).


Atividade Prática


Primeiramente, leia atentamente o texto a seguir:


A análise de dados é essencial para o sucesso dos negócios, permitindo a transformação de dados brutos em informações valiosas que apoiam a tomada de decisões estratégicas. Nesta prática, você trabalhará com uma base de dados fictícia que simula um cenário de vendas em uma empresa. A partir dessa base, você usará a biblioteca Pandas para realizar análises descritivas e criar visualizações que facilitem a compreensão dos dados.



Agora, vamos praticar!



1. Configuração do ambiente e criação do DataFrame:


a. Acesse o Google Colab e crie um novo notebook. b. Importe a biblioteca Pandas usando a abreviação “pd” e crie um DataFrame com dados fictícios de vendas, incluindo colunas como Data, Produto, Quantidade Vendida, Receita e Custo. c. Adicione uma nova coluna ao DataFrame chamada Lucro, calculando a diferença entre a Receita e o Custo. d. Exiba o DataFrame resultante para visualizar os dados.



import pandas as pd



# Dados fictícios


data = {


    ‘Data’: [‘2024-01-01’, ‘2024-01-02’, ‘2024-01-03’],


    ‘Produto’: [‘Produto A’, ‘Produto B’, ‘Produto C’],


    ‘Quantidade Vendida’: [30, 20, 15],


    ‘Receita’: [3000, 2000, 1500],


    ‘Custo’: [2000, 1200, 800]


}



df = pd.DataFrame(data)


df[‘Lucro’] = df[‘Receita’] - df[‘Custo’]


print(df)



2. Análise Descritiva e Transformação de Dados:


a. Calcule o total de receita, custo e lucro para todo o período usando as funções de agregação do Pandas. b. Crie uma nova coluna que indica a margem de lucro percentual (Margem Lucro (%)), calculada como (Lucro / Receita) * 100. c. Filtre o DataFrame para exibir apenas os produtos com uma margem de lucro acima de 30%.



# Agregação dos dados


total_receita = df[‘Receita’].sum()


total_custo = df[‘Custo’].sum()


total_lucro = df[‘Lucro’].sum()



print(f"Total Receita: {total_receita}“)


print(f"Total Custo: {total_custo}”)


print(f"Total Lucro: {total_lucro}")



# Margem de lucro percentual


df[‘Margem Lucro (%)’] = (df[‘Lucro’] / df[‘Receita’]) * 100



# Filtrando produtos com margem de lucro acima de 30%


produtos_lucrativos = df[df[‘Margem Lucro (%)’] > 30]


print(produtos_lucrativos)



3. Visualização de Dados:


a. Utilize a biblioteca Matplotlib ou Seaborn para criar um gráfico de barras que mostre a quantidade vendida de cada produto. b. Crie um gráfico de linha que exiba a evolução do lucro ao longo dos dias. c. Exiba um gráfico de pizza que mostra a participação percentual de cada produto na receita total.



import matplotlib.pyplot as plt



# Gráfico de barras - Quantidade Vendida por Produto


plt.bar(df[‘Produto’], df[‘Quantidade Vendida’])


plt.xlabel(‘Produto’)


plt.ylabel(‘Quantidade Vendida’)


plt.title(‘Quantidade Vendida por Produto’)


plt.show()



# Gráfico de linha - Lucro ao longo dos dias


plt.plot(df[‘Data’], df[‘Lucro’], marker=‘o’)


plt.xlabel(‘Data’)


plt.ylabel(‘Lucro’)


plt.title(‘Evolução do Lucro’)


plt.show()



# Gráfico de pizza - Participação percentual na Receita


plt.pie(df[‘Receita’], labels=df[‘Produto’], autopct=‘%1.1f%%’)


plt.title(‘Participação na Receita por Produto’)


plt.show()



4. Discussão dos Resultados:


a. Analise os gráficos e os resultados obtidos para identificar quais produtos foram mais lucrativos e em quais dias o lucro foi maior. b. Discuta possíveis estratégias de negócio que poderiam ser adotadas com base nesses insights, como o aumento da produção dos produtos mais lucrativos ou a otimização dos custos dos produtos menos lucrativos.






Resultado Esperado



Configuração do ambiente e criação do DataFrame:
DataFrame criado com colunas de Data, Produto, Quantidade Vendida, Receita, Custo e Lucro.
Análise Descritiva e Transformação de Dados:
Totais de receita, custo e lucro calculados.
Coluna de Margem Lucro (%) adicionada e produtos com margem acima de 30% filtrados corretamente.
Visualização de Dados:
Gráfico de barras mostrando a quantidade vendida de cada produto.
Gráfico de linha mostrando a evolução do lucro ao longo dos dias.
Gráfico de pizza mostrando a participação percentual de cada produto na receita total.
Discussão dos Resultados:
Análise clara dos dados e sugestões de estratégias de negócio com base nos insights obtidos.
Essa atividade prática oferece uma introdução ao uso de Pandas e técnicas de visualização de dados em Python, permitindo aos alunos aplicar conceitos de ciência de dados no contexto empresarial.



Parte 3: Aplicação Prática Real


Contexto


A Starbucks deseja utilizar a análise descritiva de dados para entender melhor as vendas de suas bebidas ao longo do ano. Você foi contratado para analisar os dados e fornecer insights que possam auxiliar nas decisões estratégicas da empresa.



Passo 1: Importação dos Dados


Utilize Python para importar um dataset real das vendas da Starbucks disponível em plataformas como o Kaggle.


url = “https://raw.githubusercontent.com/datasets/starbucks-drinks-dataset/master/starbucks_drinkMenu_expanded.csv”


data = pd.read_csv(url)



Passo 2: Análise Descritiva


Gere estatísticas descritivas e visualize as vendas por categoria de bebida e ao longo do tempo, utilizando gráficos de barras e linhas.


Passo 3: Análise dos Resultados


Identifique as categorias de bebidas mais vendidas e discuta como as vendas variam durante o ano.
Forneça recomendações para a Starbucks com base nas tendências observadas.


Conclusão


A análise descritiva de dados, seja com Excel ou Python, é uma ferramenta poderosa para transformar dados em informações visuais e compreensíveis. Ao seguir essa prática, você terá uma melhor compreensão dos padrões e tendências nos dados, facilitando a tomada de decisões informadas em qualquer contexto de negócios.




Atividade Prática 4 – Visualização de Dados



Objetivo


O objetivo desta atividade é aplicar conceitos de visualização de dados em um cenário de negócios. Você vai utilizar gráficos estatísticos para explorar e analisar um conjunto de dados fictício, identificando padrões e insights úteis para a tomada de decisões empresariais.



Contexto


Você é analista de dados em uma empresa de varejo e precisa criar relatórios para a equipe de gestão. Seu trabalho é utilizar a visualização de dados para revelar tendências e padrões nas vendas mensais da empresa, comparando o desempenho de diferentes categorias de produtos e analisando a participação de mercado.



Dados


Utilize o seguinte conjunto de dados fictício que contém informações sobre vendas mensais em diferentes categorias de produtos:



import pandas as pd



# Dados de exemplo


dados = {


    ‘Meses’: [‘Jan’, ‘Fev’, ‘Mar’, ‘Abr’, ‘Mai’, ‘Jun’, ‘Jul’, ‘Ago’, ‘Set’, ‘Out’, ‘Nov’, ‘Dez’],


    ‘Eletrônicos’: [1200, 1300, 1250, 1400, 1500, 1600, 1700, 1650, 1800, 1900, 2000, 2100],


    ‘Roupas’: [900, 950, 920, 1000, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450],


    ‘Alimentos’: [600, 620, 610, 630, 650, 670, 680, 690, 700, 710, 720, 730],


}



df = pd.DataFrame(dados)



Tarefas


Criação de Gráficos:
Gráfico de Linha: crie um gráfico de linha que mostre a tendência de vendas mensais para cada categoria de produto.
Gráfico de Barras: crie um gráfico de barras que compare as vendas por categoria em um mês específico (escolha um mês para destacar).
Gráfico de Pizza: crie um gráfico de pizza para mostrar a participação de mercado de cada categoria no total de vendas anuais.
Interpretação dos Gráficos:
Tendências de Vendas: analise o gráfico de linha para identificar tendências e sazonalidades nas vendas de cada categoria ao longo do ano.
Comparação de Categorias: utilize o gráfico de barras para comparar a performance das categorias em um mês específico e discutir possíveis razões para as diferenças.
Participação de Mercado: examine o gráfico de pizza para entender a distribuição de vendas entre as categorias e identificar qual categoria tem maior participação de mercado.


Ferramentas e Bibliotecas


Utilize as seguintes bibliotecas para criar os gráficos:


Matplotlib para gráficos básicos e de barras.
Seaborn para gráficos de linha e outros gráficos estatísticos.
Pandas para manipulação e organização dos dados.


Exemplos de Código



Gráfico de Linha



import matplotlib.pyplot as plt


import seaborn as sns



plt.figure(figsize=(10, 6))


for categoria in [‘Eletrônicos’, ‘Roupas’, ‘Alimentos’]:


    sns.lineplot(x=‘Meses’, y=categoria, data=df, marker=‘o’, label=categoria)


plt.title(‘Tendência de Vendas Mensais por Categoria’)


plt.xlabel(‘Meses’)


plt.ylabel(‘Vendas’)


plt.legend(title=‘Categorias’)


plt.show()



Gráfico de Barras



plt.figure(figsize=(10, 6))


df_jan = df[[‘Eletrônicos’, ‘Roupas’, ‘Alimentos’]].iloc[0]


df_jan.plot(kind=‘bar’, color=[‘skyblue’, ‘lightgreen’, ‘lightcoral’])


plt.title(‘Vendas por Categoria em Janeiro’)


plt.xlabel(‘Categorias’)


plt.ylabel(‘Vendas’)


plt.show()


Gráfico de Pizza


python


Copiar código


plt.figure(figsize=(8, 6))


plt.pie(df[[‘Eletrônicos’, ‘Roupas’, ‘Alimentos’]].sum(),


        labels=[‘Eletrônicos’, ‘Roupas’, ‘Alimentos’],


        autopct=‘%1.1f%%’,


        colors=[‘gold’, ‘yellowgreen’, ‘lightcoral’])


plt.title(‘Participação de Mercado por Categoria’)


plt.show()






Resultado Esperado



Gráficos: inclua os gráficos criados como imagens no seu relatório.

Certifique-se de que os gráficos estejam bem rotulados e legíveis.


Verifique a precisão dos dados e a clareza na apresentação das informações.


Análise: escreva uma breve análise para cada gráfico, destacando os principais insights e o que eles revelam sobre o desempenho das categorias de produtos.
