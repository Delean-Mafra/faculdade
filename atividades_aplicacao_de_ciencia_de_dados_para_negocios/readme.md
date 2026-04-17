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
