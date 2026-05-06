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




 Atividade Prática 9 – Implementando uma Rede Neural para Previsão de Vendas de Produtos



Objetivos


Aplicar conceitos básicos de redes neurais artificiais em um conjunto de dados fictício de vendas.
Construir e treinar um modelo de rede neural utilizando TensorFlow e Keras.
Avaliar o desempenho do modelo e comparar as previsões com os dados reais.


Materiais, Métodos e Ferramentas


Materiais:
Conjunto de dados fictício com informações de vendas mensais.
Ambiente de desenvolvimento (Google Colab, PyCharm, ou Jupyter Notebook).
Métodos:
Manipulação e pré-processamento de dados utilizando Pandas. 
Normalização dos dados com SKLearn.
Construção e treinamento de um modelo de rede neural com TensorFlow e Keras.
Avaliação e visualização dos resultados com Matplotlib.
Ferramentas:
Bibliotecas: Pandas, NumPy, TensorFlow, Matplotlib, SKLearn.


Atividade Prática



Primeiramente, leia atentamente o texto a seguir:


Você foi encarregado de implementar um sistema de previsão de vendas para uma empresa fictícia. A empresa deseja prever suas vendas mensais com base em dados históricos. O objetivo é construir e treinar uma rede neural que possa prever as vendas futuras com base em dados passados.



Agora, vamos praticar!



PASSO A PASSO DETALHADO DA ATIVIDADE:


Configuração do Ambiente:
Configure seu ambiente de desenvolvimento. Você pode usar Google Colab, PyCharm ou Jupyter Notebook.
Importação de Bibliotecas:
Importe as bibliotecas necessárias: Pandas, NumPy, TensorFlow, SKLearn e Matplotlib.


import pandas as pd


import numpy as np


import tensorflow as tf


import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split


from sklearn.preprocessing import StandardScaler



Criação da Base de Dados:
Gere uma base de dados fictícia com meses e vendas. Utilize Pandas e NumPy para criar este conjunto de dados.


meses = pd.date_range(start=‘2023-01-01’, periods=24, freq=‘M’)


vendas = np.random.randint(80000, 120000, size=24) * 2


df = pd.DataFrame({‘Mês’: meses, ‘Vendas’: vendas})



Separação dos Dados:
Separe os dados em características (X) e alvo (Y). Divida os dados em conjuntos de treino e teste.


X = df[[‘Mês’]].values


y = df[‘Vendas’].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



Normalização dos Dados:
Normalizar os dados utilizando o StandardScaler do SKLearn.


scaler = StandardScaler()


X_train_scaled = scaler.fit_transform(X_train)


X_test_scaled = scaler.transform(X_test)



Construção do Modelo:
Defina e compile o modelo de rede neural utilizando TensorFlow e Keras.


model = tf.keras.Sequential([


    tf.keras.layers.Dense(64, activation=‘relu’, input_shape=(X_train_scaled.shape[1],)),


    tf.keras.layers.Dense(32, activation=‘relu’),


    tf.keras.layers.Dense(1)


])


model.compile(optimizer=‘adam’, loss=‘mean_squared_error’)



Treinamento do Modelo:
Treine o modelo com os dados de treino.


model.fit(X_train_scaled, y_train, epochs=100)



Avaliação do Modelo:
Avalie o modelo utilizando os dados de teste e imprima a perda (loss).


loss = model.evaluate(X_test_scaled, y_test)


print(f’Loss: {loss}')



Visualização dos Resultados:
Plote os dados reais e as previsões do modelo para comparar os resultados.


predictions = model.predict(X_test_scaled)


plt.plot(y_test, label=‘Dados Reais’)


plt.plot(predictions, label=‘Previsões’)


plt.xlabel(‘Meses’)


plt.ylabel(‘Vendas’)


plt.legend()


plt.show()






Resultado Esperado


Importação e Configuração: verificar se todas as bibliotecas necessárias foram importadas e se o ambiente está configurado corretamente.
Criação da Base de Dados: confirmar que a base de dados foi criada corretamente com os meses e vendas.
Separação e Normalização: checar se os dados foram separados corretamente e normalizados antes da construção do modelo.
Construção e Treinamento do Modelo: avaliar se o modelo foi definido, compilado e treinado corretamente.
Avaliação e Visualização: validar se o modelo foi avaliado e se os resultados foram visualizados corretamente.


Atividade Prática 11 – Análise de Sentimentos em Comentários de Clientes para Otimização de Produtos e Serviços



Objetivos


Compreender a aplicação da análise de sentimentos na interpretação de feedback de clientes.
Desenvolver habilidades práticas usando ferramentas como TextBlob e VADER para realizar análise de sentimentos em textos.
Interpretar as métricas de sentimentos e utilizar os resultados para gerar insights sobre a percepção dos clientes.


Materiais, Métodos e Ferramentas


Computador com Python instalado.
Bibliotecas Python: TextBlob, VADER SentimentIntensityAnalyzer (disponíveis via pip install textblob vaderSentiment).
Conjunto de textos fictícios para análise (fornecidos como exemplos).


Atividade Prática



Primeiramente, leia atentamente o texto a seguir:


Você recebeu um conjunto de comentários de clientes sobre um novo produto lançado por uma empresa. O objetivo é analisar esses comentários para entender como os clientes estão reagindo ao produto e identificar áreas de melhoria.


Para realizar a análise, você utilizará duas ferramentas de análise de sentimentos: TextBlob e VADER. Sua tarefa é seguir os passos abaixo para analisar os comentários e interpretar os resultados.



Passo a Passo Detalhado da Atividade:


Preparação do Ambiente:
Instale as bibliotecas necessárias se ainda não estiverem instaladas.


pip install textblob vaderSentiment




No seu ambiente Python, importe as bibliotecas necessárias e configure as ferramentas de análise de sentimentos.
Análise com TextBlob:
Utilize o seguinte código para analisar a polaridade e subjetividade dos comentários com TextBlob.


from textblob import TextBlob



# Comentários para análise


comentarios = [


    “Eu adoro o novo produto! Ele superou minhas expectativas.”,


    “O produto é bom, mas o preço é muito alto.”,


    “O atendimento ao cliente foi péssimo.”,


    “A entrega foi rápida, mas o produto não estava bem embalado.”


]



# Analisando sentimentos com TextBlob


for comentario in comentarios:


    blob = TextBlob(comentario)


    sentimento = blob.sentiment


    print(f"Comentário: {comentario}“)


    print(f"Sentimento: Polaridade={sentimento.polarity}, Subjetividade={sentimento.subjectivity}”)



Análise com VADER:
Utilize o seguinte código para analisar a polaridade dos comentários com VADER.


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



# Criando a instância do analisador de sentimentos


analyzer = SentimentIntensityAnalyzer()



# Comentários para análise


comentarios = [


    “Eu adoro o novo produto! Ele superou minhas expectativas.”,


    “O produto é bom, mas o preço é muito alto.”,


    “O atendimento ao cliente foi péssimo.”,


    “A entrega foi rápida, mas o produto não estava bem embalado.”


]



# Analisando cada comentário


for comentario in comentarios:


    pontuacao = analyzer.polarity_scores(comentario)


    print(f"Comentário: {comentario}“)


    print(f"Pontuação: {pontuacao}”)



Interpretação dos Resultados:
Compare os resultados obtidos das análises com TextBlob e VADER.
Identifique quais comentários são classificados como positivos, negativos ou neutros.
Com base nas métricas de polaridade e subjetividade (TextBlob) e na pontuação compound (VADER), discuta o feedback geral sobre o produto e proponha ações para melhorar áreas específicas mencionadas pelos clientes.
Relatório:
Elabore um relatório detalhado com suas observações e conclusões. Inclua gráficos ou tabelas, se necessário, para ilustrar a análise dos sentimentos.
Proponha sugestões para a empresa com base na análise dos sentimentos e no feedback dos clientes.





Resultado Esperado


a. A análise dos resultados deve mostrar a polaridade e subjetividade dos comentários com TextBlob e a pontuação compound, pos, neu, e neg com VADER.


b. As interpretações devem refletir a categorização dos sentimentos dos comentários, com sugestões práticas baseadas nas análises.


c. O relatório deve incluir uma discussão clara sobre as métricas de sentimentos, gráficos ou tabelas conforme necessário, e recomendações para a empresa.


Essa atividade prática ajudará os alunos a aplicar a análise de sentimentos em um cenário realista, facilitando a compreensão de como as ferramentas podem ser usadas para obter insights valiosos a partir de feedback de clientes.



Atividade Prática 12 – Construindo um Sistema de Recomendação Personalizada



Objetivos


Desenvolver e implementar um sistema de recomendação personalizada utilizando a biblioteca Surprise em Python.
Avaliar o desempenho do sistema de recomendação com base em métricas de acurácia.
Aplicar técnicas de pré-processamento de dados e normalização para otimizar o modelo de recomendação.


Materiais, Métodos e Ferramentas


Computador com acesso à internet.
Google Colab ou ambiente Python com suporte à biblioteca Surprise.
Biblioteca Surprise para sistemas de recomendação (disponível via pip).
Biblioteca pandas para manipulação de dados.
Dados fictícios sobre classificações de produtos (fornecidos na atividade).


Atividade Prática


Primeiramente, leia atentamente o texto a seguir:


A recomendação personalizada é uma técnica essencial para melhorar a experiência do usuário e impulsionar as vendas em diversos setores de negócios. Nesta atividade, você terá a oportunidade de implementar um sistema de recomendação utilizando a biblioteca Surprise em Python. Você irá seguir um passo a passo para construir um modelo, avaliar seu desempenho e gerar recomendações personalizadas para um usuário específico.



Agora, vamos praticar!



PASSO A PASSO DETALHADO DA ATIVIDADE:



Preparação do Ambiente:
Acesse o Google Colab ou configure seu ambiente Python local.
Instale as bibliotecas necessárias com os comandos:


!pip install pandas surprise



Importação das Bibliotecas:
Importe as bibliotecas necessárias para a atividade:


import pandas as pd


from surprise import Dataset, Reader, SVD


from surprise.model_selection import train_test_split


from surprise import accuracy



Criação e Estruturação dos Dados:
Crie um DataFrame com dados fictícios sobre classificações de produtos:


data = {


    ‘user_id’: [1, 1, 1, 2, 2, 3, 3, 4],


    ‘item_id’: [1, 2, 3, 1, 2, 2, 3, 1],


    ‘rating’: [5, 3, 2, 5, 4, 3, 5, 4]


}


df = pd.DataFrame(data)



Preparação dos Dados para o Modelo:
Defina o formato dos dados usando o Reader e carregue os dados:


reader = Reader(rating_scale=(1, 5))


data = Dataset.load_from_df(df[[‘user_id’, ‘item_id’, ‘rating’]], reader)



Divisão dos Dados:
Divida os dados em conjuntos de treino e teste:


trainset, testset = train_test_split(data, test_size=0.25)



Construção e Treinamento do Modelo:
Crie e treine o modelo de recomendação utilizando o SVD:


algo = SVD()


algo.fit(trainset)



Avaliação do Modelo:
Faça previsões e avalie o desempenho do modelo:


predictions = algo.test(testset)


print(“RMSE:”, accuracy.rmse(predictions))


print(“MAE:”, accuracy.mae(predictions))



Geração de Recomendações:
Gere as top 5 recomendações para um usuário específico:


user_id = 1


user_items = df[df[‘user_id’] == user_id][‘item_id’]


all_items = set(df[‘item_id’].unique())


items_to_predict = list(all_items - set(user_items))



recommendations = []


for item_id in items_to_predict:


    score = algo.predict(user_id, item_id).est


    recommendations.append((item_id, score))



recommendations.sort(key=lambda x: x[1], reverse=True)



top_5 = recommendations[:5]


print(f"Top 5 recomendações para o usuário {user_id}:“)


for item, score in top_5:


    print(f"Item {item} com pontuação {score:.2f}”)






Resultado Esperado


Preparação do Ambiente: o ambiente deve estar configurado com as bibliotecas necessárias instaladas.
Importação das Bibliotecas: as bibliotecas pandas, surprise devem estar corretamente importadas.
Criação e Estruturação dos Dados: o DataFrame deve ser criado com as colunas user_id, item_id e rating.
Preparação dos Dados para o Modelo: o DataFrame deve ser carregado corretamente utilizando o Reader e Dataset da biblioteca Surprise.
Divisão dos Dados: Os dados devem ser divididos em conjuntos de treino e teste usando o train_test_split.
Construção e Treinamento do Modelo: o modelo SVD deve ser treinado com o conjunto de treino.
Avaliação do Modelo: as métricas RMSE e MAE devem ser calculadas e apresentadas.
Geração de Recomendações: as top 5 recomendações para o usuário especificado devem ser corretamente calculadas e apresentadas.


Certifique-se de que todos os passos foram seguidos corretamente e que o código está funcionando conforme esperado.


Atividade Prática 13 – Segmentação de Clientes: Aplicando K-Means, DBSCAN e Hierarchical Clustering



Objetivos


Compreender e aplicar técnicas de segmentação de clientes utilizando algoritmos de clusterização.
Utilizar Python e bibliotecas como SKLearn e Pandas para realizar análise prática de dados de clientes.
Interpretar os resultados dos algoritmos de clusterização e suas implicações para estratégias de marketing e negócios.


Materiais, Métodos e Ferramentas


Ambiente de desenvolvimento Python (Google Colab, Jupyter Notebook ou IDE de sua preferência).
Bibliotecas Python: Pandas, NumPy, Matplotlib, SKLearn, SciPy.
Base de dados fictícia contendo informações de clientes (idade, renda anual e pontuação de gastos).


Atividade Prática


Primeiramente, leia atentamente o texto a seguir:


Nesta atividade, você explorará técnicas de clusterização para segmentar uma base de dados de clientes. Você irá aplicar três algoritmos diferentes: K-Means, DBSCAN e Hierarchical Clustering, e analisar os resultados obtidos para entender as características dos diferentes grupos de clientes identificados. A base de dados fictícia utilizada contém três variáveis: idade, renda anual e pontuação de gastos.



Agora, vamos praticar!



PASSO A PASSO DETALHADO DA ATIVIDADE:


Preparação do Ambiente:
Abra seu ambiente de desenvolvimento Python (Google Colab, Jupyter Notebook ou IDE de sua escolha).
Instale e importe as bibliotecas necessárias: Pandas, NumPy, Matplotlib, SKLearn e SciPy.


Carregar e Preparar os Dados:
Crie uma base de dados fictícia com as seguintes colunas: Idade, Renda Anual (k$), e Pontuação de Gastos (1-100).
Insira os seguintes dados fictícios:


import pandas as pd


import numpy as np



data = {


    ‘Idade’: [25, 34, 45, 31, 40, 23, 35, 50, 43, 52],


    ‘Renda Anual (k$)’: [15, 25, 35, 45, 50, 55, 60, 70, 80, 90],


    ‘Pontuação de Gastos (1-100)’: [39, 81, 6, 77, 40, 76, 94, 3, 72, 14]


}


df = pd.DataFrame(data)



Normalização dos Dados:
Normalizar os dados utilizando StandardScaler para garantir a consistência no processamento dos algoritmos de clusterização.


from sklearn.preprocessing import StandardScaler



scaler = StandardScaler()


scaled_data = scaler.fit_transform(df)



Aplicação do Algoritmo K-Means:
Aplique o algoritmo K-Means com 3 clusters e visualize os resultados.


from sklearn.cluster import KMeans


import matplotlib.pyplot as plt



kmeans = KMeans(n_clusters=3, random_state=0)


clusters = kmeans.fit_predict(scaled_data)


df[‘Cluster’] = clusters



plt.figure(figsize=(10, 6))


plt.scatter(df[‘Idade’], df[‘Pontuação de Gastos (1-100)’], c=df[‘Cluster’], cmap=‘viridis’)


plt.title(‘Segmentação de Clientes com K-Means’)


plt.xlabel(‘Idade’)


plt.ylabel(‘Pontuação de Gastos (1-100)’)


plt.colorbar(label=‘Cluster’)


plt.show()



Aplicação do Algoritmo DBSCAN:
Aplique o algoritmo DBSCAN e visualize os clusters identificados.


from sklearn.cluster import DBSCAN



dbscan = DBSCAN(eps=0.5, min_samples=2)


clusters_dbscan = dbscan.fit_predict(scaled_data)


df[‘Cluster_DBSCAN’] = clusters_dbscan



plt.figure(figsize=(10, 6))


plt.scatter(df[‘Idade’], df[‘Pontuação de Gastos (1-100)’], c=df[‘Cluster_DBSCAN’], cmap=‘plasma’)


plt.title(‘Segmentação de Clientes com DBSCAN’)


plt.xlabel(‘Idade’)


plt.ylabel(‘Pontuação de Gastos (1-100)’)


plt.colorbar(label=‘Cluster’)


plt.show()



Aplicação do Algoritmo Hierarchical Clustering:
Aplique o Hierarchical Clustering e visualize o dendrograma.


from scipy.cluster.hierarchy import dendrogram, linkage



linked = linkage(scaled_data, method=‘ward’)



plt.figure(figsize=(10, 6))


dendrogram(linked, orientation=‘top’, distance_sort=‘descending’, show_leaf_counts=True)


plt.title(‘Dendrograma para Segmentação de Clientes’)


plt.xlabel(‘Índice dos Clientes’)


plt.ylabel(‘Distância’)


plt.show()



Análise dos Resultados:
Compare os resultados obtidos pelos três algoritmos.
Discuta as diferenças entre os clusters identificados pelos algoritmos K-Means, DBSCAN e Hierarchical Clustering.
Identifique padrões e características dos clusters criados.



Resultado  Esperado


K-Means: identificação de três clusters com base nas características dos dados. O gráfico deve mostrar a segmentação dos clientes em três grupos distintos.
DBSCAN: identificação de clusters com base em densidade. O gráfico deve mostrar os clusters formados pelo DBSCAN, que podem variar dependendo dos parâmetros utilizados.
Hierarchical Clustering: dendrograma mostrando a hierarquia de clusters. Deve permitir a visualização da fusão de clusters e ajudar na decisão sobre o número de clusters a serem utilizados.
Esta atividade visa proporcionar uma compreensão prática das técnicas de clusterização e sua aplicação em segmentação de clientes, preparando os alunos para implementar essas técnicas em situações reais de negócios.

