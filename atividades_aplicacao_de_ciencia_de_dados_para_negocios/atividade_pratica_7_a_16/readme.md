# Este repositório contém todas as atividades práticas das aulas 7 a 16 (exceto P&R) da disciplina Aplicação de Ciência de Dados para Negócios

Atividade Prática 7 – Aplicação de Regressão em Negócios



Objetivo


Aplicar técnicas de regressão linear e logística em dados simulados para prever o preço de imóveis e a probabilidade de cliques em anúncios. Interpretar os resultados e discutir as implicações para decisões empresariais.



Materiais, Métodos e Ferramentas


Materiais:
Conjunto de dados fictício com informações de vendas mensais.
Ambiente de desenvolvimento (Google Colab, PyCharm, ou Jupyter Notebook).
Métodos:
Manipulação e pré-processamento de dados utilizando Pandas e NumPy.
Construção e treinamento de modelos de regressão linear e logística com scikit-learn.
Avaliação dos modelos com métricas como MSE, R², precisão, recall, e F1-score.
Visualização dos resultados e da matriz de confusão utilizando Matplotlib e Seaborn.
Ferramentas:
Bibliotecas: Pandas, NumPy, scikit-learn, Matplotlib, Seaborn.


Parte 1: Regressão Linear



1.1. Definição do Problema


Uma imobiliária deseja prever o preço de imóveis com base em características como o número de quartos e a metragem quadrada. Você vai usar a regressão linear para construir um modelo preditivo.



1.2. Dados


Vamos criar um conjunto de dados simulado com as seguintes características:


●        Numero_Quartos: número de quartos do imóvel.


●        Metragem_Quadrada: área total do imóvel em metros quadrados.


●        Preco_Imovel: preço do imóvel em reais.



1.3. Tarefas


Gere um conjunto de dados simulado com as características acima.
Divida os dados em conjuntos de treinamento e teste.
Construa um modelo de regressão linear múltipla para prever o preço do imóvel.
Avalie o modelo utilizando o erro médio quadrático (MSE) e o coeficiente de determinação (R²).
Visualize a relação entre o número de quartos, a metragem quadrada e o preço do imóvel com gráficos apropriados.


Parte 2: Regressão Logística



2.1. Definição do Problema


Você deseja prever a probabilidade de um cliente clicar em um anúncio com base em suas características. Utilizaremos a regressão logística para isso.



2.2. Dados


Vamos criar um conjunto de dados simulado com as seguintes características:


Idade: idade do cliente.
Renda: renda anual do cliente.
Clicou_Anuncio: indicador binário (0 ou 1) de se o cliente clicou no anúncio.


2.3. Tarefas


Gere um conjunto de dados simulado com as características acima.
Divida os dados em conjuntos de treinamento e teste.
Construa um modelo de regressão logística para prever a probabilidade de clique no anúncio.
Avalie o modelo utilizando métricas como precisão, recall, e F1-score.
Visualize a matriz de confusão e o relatório de classificação.


Implementação


Aqui está um esboço de código para cada parte da atividade:



Parte 1: Regressão Linear



import pandas as pd


import numpy as np


import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split


from sklearn.linear_model import LinearRegression


from sklearn.metrics import mean_squared_error, r2_score



# Gerando dados fictícios


np.random.seed(42)


num_quartos = np.random.randint(1, 6, 100)


metragem_quadrada = np.random.randint(50, 200, 100)


preco_imovel = (num_quartos * 10000) + (metragem_quadrada * 50) + np.random.randint(5000, 20000, 100)



df = pd.DataFrame({


    ‘Numero_Quartos’: num_quartos,


    ‘Metragem_Quadrada’: metragem_quadrada,


    ‘Preco_Imovel’: preco_imovel


})



# Dividindo os dados


X = df[[‘Numero_Quartos’, ‘Metragem_Quadrada’]]


y = df[‘Preco_Imovel’]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Modelo de regressão linear


modelo = LinearRegression()


modelo.fit(X_train, y_train)


predicoes = modelo.predict(X_test)



# Avaliação do modelo


mse = mean_squared_error(y_test, predicoes)


r2 = r2_score(y_test, predicoes)


print(f’Erro Médio Quadrático (MSE): {mse}‘)


print(f’Coeficiente de Determinação (R²): {r2}’)



# Visualização


plt.figure(figsize=(12, 6))


plt.scatter(df[‘Metragem_Quadrada’], df[‘Preco_Imovel’], color=‘blue’, label=‘Dados Reais’)


plt.plot(df[‘Metragem_Quadrada’], modelo.predict(df[[‘Numero_Quartos’, ‘Metragem_Quadrada’]]), color=‘red’, label=‘Linha de Regressão’)


plt.title(‘Regressão Linear - Preço do Imóvel’)


plt.xlabel(‘Metragem Quadrada’)


plt.ylabel(‘Preço do Imóvel’)


plt.legend()


plt.show()



Parte 2: Regressão Logística



import pandas as pd


import numpy as np


import matplotlib.pyplot as plt


import seaborn as sns


from sklearn.model_selection import train_test_split


from sklearn.linear_model import LogisticRegression


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report



# Gerando dados fictícios


np.random.seed(42)


idade = np.random.randint(18, 70, 200)


renda = np.random.randint(20000, 100000, 200)


clicou_anuncio = np.random.choice([0, 1], size=200, p=[0.7, 0.3])



df_log = pd.DataFrame({


    ‘Idade’: idade,


    ‘Renda’: renda,


    ‘Clicou_Anuncio’: clicou_anuncio


})



# Dividindo os dados


X_log = df_log[[‘Idade’, ‘Renda’]]


y_log = df_log[‘Clicou_Anuncio’]


X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(X_log, y_log, test_size=0.2, random_state=42)



# Modelo de regressão logística


modelo_logistico = LogisticRegression()


modelo_logistico.fit(X_train_log, y_train_log)


predicoes_log = modelo_logistico.predict(X_test_log)



# Avaliação do modelo


accuracy = accuracy_score(y_test_log, predicoes_log)


precision = precision_score(y_test_log, predicoes_log)


recall = recall_score(y_test_log, predicoes_log)


f1 = f1_score(y_test_log, predicoes_log)


print(f’Precisão: {precision}‘)


print(f’Recall: {recall}’)


print(f’Pontuação F1: {f1}‘)


print(f’Acurácia: {accuracy}’)


print(f’Matriz de Confusão:\n{confusion_matrix(y_test_log, predicoes_log)}‘)


print(f’Relatório de Classificação:\n{classification_report(y_test_log, predicoes_log)}’)



# Visualização da matriz de confusão


sns.heatmap(confusion_matrix(y_test_log, predicoes_log), annot=True, fmt=‘d’, cmap=‘Blues’)


plt.title(‘Matriz de Confusão - Regressão Logística’)


plt.xlabel(‘Previsões’)


plt.ylabel(‘Valores Reais’)


plt.show()



Discussão


Regressão Linear: Discuta como o modelo pode ser melhorado e as implicações dos coeficientes das variáveis preditoras.
Regressão Logística: Analise a performance do modelo e como as métricas de avaliação podem informar a eficácia do modelo em prever cliques em anúncios.



Esta atividade prática permitirá que você aplique e entenda as técnicas de regressão em contextos empresariais, ajudando a desenvolver habilidades importantes para análise de dados.




Gabarito Esperado



Parte 1: Regressão Linear



1.1. Definição do Problema



O modelo de regressão linear deve prever o preço de imóveis com base em características como o número de quartos e a metragem quadrada.



1.2. Dados



O conjunto de dados simulado deve ter as colunas Numero_Quartos, Metragem_Quadrada, e Preco_Imovel, com valores gerados aleatoriamente.



1.3. Tarefas


Geração dos Dados

O código para gerar os dados deve criar um DataFrame com 100 amostras, onde Preco_Imovel é uma combinação linear de Numero_Quartos e Metragem_Quadrada, adicionando um erro aleatório.



Divisão dos Dados

Os dados devem ser divididos em conjuntos de treinamento e teste, com uma proporção de 80% para treinamento e 20% para teste.



Construção do Modelo

O modelo de regressão linear deve ser ajustado usando o método fit com os dados de treinamento.



Avaliação do Modelo

O erro médio quadrático (MSE) e o coeficiente de determinação (R²) devem ser calculados e interpretados. O MSE indica a média dos erros quadráticos, enquanto o R² indica a proporção da variabilidade explicada pelo modelo.



Exemplos de saída esperada:


Erro Médio Quadrático (MSE): [valor próximo do esperado, dependendo da aleatoriedade]


Coeficiente de Determinação (R²): [valor próximo do esperado, entre 0 e 1]



Visualização

O gráfico deve mostrar a relação entre Metragem_Quadrada e Preco_Imovel, com a linha de regressão representando o modelo ajustado.



Parte 2: Regressão Logística



2.1. Definição do Problema


O modelo de regressão logística deve prever a probabilidade de um cliente clicar em um anúncio com base em características como idade e renda.



2.2. Dados


O conjunto de dados simulado deve ter as colunas Idade, Renda, e Clicou_Anuncio, com valores aleatórios.



2.3. Tarefas


Geração dos Dados

O código para gerar os dados deve criar um DataFrame com 200 amostras, onde Clicou_Anuncio é uma variável binária (0 ou 1) com base em uma distribuição aleatória.



Divisão dos Dados

Os dados devem ser divididos em conjuntos de treinamento e teste, com uma proporção de 80% para treinamento e 20% para teste.



Construção do Modelo

O modelo de regressão logística deve ser ajustado usando o método fit com os dados de treinamento.



Avaliação do Modelo

As métricas de avaliação incluem precisão, recall, F1-score e acurácia. A matriz de confusão deve ser calculada e exibida para verificar o desempenho do modelo.


Exemplos de saída esperada:



Precisão: [valor esperado, próximo do valor real, entre 0 e 1]


Recall: [valor esperado, próximo do valor real, entre 0 e 1]


Pontuação F1: [valor esperado, próximo do valor real, entre 0 e 1]


Acurácia: [valor esperado, próximo do valor real, entre 0 e 1]


Matriz de Confusão:


[[valor verdadeiro negativo, valor falso positivo],


 [valor falso negativo, valor verdadeiro positivo]]



Visualização

A matriz de confusão deve ser visualizada com uma escala de cores, mostrando a contagem de verdadeiros positivos, falsos positivos, verdadeiros negativos e falsos negativos.





Resultado Esperado


Regressão Linear
Melhoria do Modelo: considerar adicionar mais variáveis ou usar técnicas de regularização para melhorar a performance do modelo. Verificar a multicolinearidade entre variáveis.
Implicações dos Coeficientes: coeficientes positivos indicam uma relação direta com o preço do imóvel, enquanto coeficientes negativos indicam uma relação inversa.
Regressão Logística
Performance do Modelo: a análise das métricas de avaliação deve informar sobre a capacidade do modelo de classificar corretamente os cliques.
Métricas de Avaliação: precisão indica a proporção de verdadeiros positivos entre todos os positivos previstos, recall indica a proporção de verdadeiros positivos entre todos os positivos reais, e F1-score é a média harmônica entre precisão e recall.


Este gabarito deve ajudar a verificar se as respostas e interpretações dos resultados estão corretas. Ajustes podem ser necessários dependendo da aleatoriedade nos dados simulados.




Atividade Prática 8 – Avaliação e Otimização de Modelos de Classificação



Objetivos



Analisar a eficácia de um modelo de classificação utilizando métricas básicas e avançadas.
Aplicar técnicas de pré-processamento de dados e validação cruzada para melhorar a performance do modelo.
Interpretar resultados de métricas como acurácia, precisão, recall e F1-score para ajustar e otimizar modelos.


Materiais, Métodos e Ferramentas


Materiais: base de dados de vinhos (ou qualquer outro dataset relevante)
Métodos: pré-processamento de dados, treinamento de modelos, avaliação de métricas


Ferramentas


Python, pandas, scikit-learn, XGBoost, matplotlib, seaborn


Atividade Prática


Primeiramente, leia atentamente o texto a seguir:


Você recebeu uma base de dados contendo informações sobre vinhos e deseja avaliar a performance de um modelo de classificação. Seu objetivo é construir um modelo usando o XGBoost Classifier, analisar a eficácia do modelo com métricas como acurácia, precisão, recall e F1-score, e identificar possíveis anomalias e ruídos nos dados.



Agora, vamos praticar!



PASSO A PASSO DETALHADO DA ATIVIDADE:


Importação e Pré-processamento dos Dados:
Importe as bibliotecas necessárias (pandas, numpy, matplotlib, seaborn, sklearn, xgboost).
Carregue o dataset de vinhos (ou o dataset fornecido) usando pd.read_csv().
Realize a limpeza dos dados, removendo valores nulos e variáveis desnecessárias.
Divisão dos Dados:
Separe os dados em variáveis preditoras (X) e variável alvo (y).
Divida o dataset em conjuntos de treinamento e teste usando train_test_split().
Padronização dos Dados:
Aplique a padronização dos dados utilizando StandardScaler.
Treinamento do Modelo:
Crie e treine um modelo de classificação utilizando o XGBClassifier.
Faça previsões no conjunto de teste.
Avaliação do Modelo:
Calcule as métricas de desempenho: acurácia, precisão, recall e F1-score usando as funções apropriadas do sklearn.
Gere e visualize a matriz de confusão.
Crie um gráfico de barras para ilustrar as métricas de desempenho do modelo (precisão, recall e F1-score).
Validação Cruzada:
Realize a validação cruzada utilizando cross_val_score() com o RandomForestClassifier.
Compare os resultados de acurácia obtidos com e sem validação cruzada.
Análise de Anomalias e Ruídos:
Utilize gráficos de dispersão para identificar possíveis anomalias nos dados.
Aplique técnicas de limpeza para tratar anomalias e ruídos.
Documentação dos Resultados:
Compile os resultados em um relatório, incluindo as métricas de desempenho, visualizações e qualquer ajuste realizado nos dados ou no modelo.
Discuta os resultados obtidos e sugira melhorias para o modelo, se necessário.





Resultado Esperado



Importação e Pré-processamento dos Dados: o aluno deve ter importado corretamente as bibliotecas, carregado e limpo o dataset, e separado variáveis preditoras e alvo.
Treinamento e Avaliação do Modelo: o aluno deve ter criado e treinado o modelo XGBoost, realizado as previsões e calculado as métricas corretamente. A matriz de confusão e gráficos devem estar presentes e bem elaborados.
 Validação Cruzada e Análise de Dados: o aluno deve ter realizado a validação cruzada, identificado anomalias e ruídos, e aplicado técnicas de limpeza. O relatório deve incluir uma discussão dos resultados e sugestões de melhorias.
