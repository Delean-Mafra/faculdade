import random
from re import X
from turtle import mode
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



# Aula 1 e 2

altura = [1.70, 1.80, 1.60, 1.75, 1.65]
peso = [70, 80, 60, 75, 65]
sexo = ['M', 'M', 'F', 'M', 'F']


model = LogisticRegression()
X = np.array(list(zip(altura, peso)))
y = np.array(sexo)

model.fit(X, y)


nova_amostra = np.array([[1.50, 54]])
decisao = model.predict(nova_amostra)

if decisao[0] == 'F':
    print('Provavelmente é uma mulher')
else:
    print('Provavelmente é um homem')





# Continuação do final da aula 2 e início da aula 3


vendas = [{'Produto': 'Coca-cola', 'Valor': 10.0, 'Quantidade': 100},
          {'Produto': 'Pepsi', 'Valor': 8.0, 'Quantidade': 150},
          {'Produto': 'Fanta', 'Valor': 9.0, 'Quantidade': 120}]

with open('vendas.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(['Produto', 'Valor', 'Quantidade'])
    for venda in vendas:
        writer.writerow([venda['Produto'], venda['Valor'], venda['Quantidade']])


dados = pd.read_csv('vendas.csv')
print(dados)


X = dados[['Quantidade', 'Valor']]

modelo = KMeans(n_clusters=3)
modelo.fit(X)

dados['Cluster'] = modelo.labels_
print(dados)


cores = ['red', 'green', 'blue']
for i in range(3):
    plt.scatter(X[dados['Cluster'] == i]['Quantidade'],X[dados['Cluster'] == i]['Valor'], color = cores[i])




# Aula 4

comprimento = [1.4, 1.3, 1.5, 4.7, 4.5, 4.9, 5.1, 6.0, 5.8, 6.6, 6.6, 6.9, 5.7, 6.3] # Removed 6.1
largura = [0.2, 0.3, 0.1, 1.4, 1.5, 1.5, 1.8, 2.5, 2.3, 2.1, 2.3, 2.8, 2.5, 2.8]
classe = ['Setosa', 'Setosa', 'Setosa', 'Versicolor', 'Versicolor', 'Versicolor',
          'Virginica', 'Virginica', 'Virginica', 'Virginica', 'Virginica', 'Virginica', 'Virginica', 'Virginica']

df_flores = pd.DataFrame({'Comprimento': comprimento, 'Largura': largura, 'Classe': classe})

modelo = KNeighborsClassifier(n_neighbors=3)
X = df_flores[['Comprimento', 'Largura']]
y = df_flores['Classe']

modelo.fit(X, y)

nova_amostra = [[5.0,2.0]]
previsao = modelo.predict(nova_amostra)
print('A nova flor pertence à classe:',previsao)


# Aula 5

random.seed(42)
nota_anterior = [random.randint(0,100) for _ in range(100)]
horas_estudando = [random.randint(0,10) for _ in range(100)]
passou = [1 if nota >= 5 else 0 for nota in nota_anterior]
dados = pd.DataFrame({'Nota Anterior': nota_anterior, 'Horas Estudando': horas_estudando, 'Passou': passou})
print(dados)

X = dados[['Nota Anterior', 'Horas Estudando']]
y = dados['Passou']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   

cfl = DecisionTreeClassifier(max_depth=3)
cfl.fit(X_train, y_train)
accuracy = cfl.score(X_test, y_test)
print(f'Exatidão do modelo é de: {accuracy:.2f}')


novos_dados = pd.DataFrame({'Nota Anterior': [4], 'Horas Estudando': [1]})

previsao = cfl.predict(novos_dados)
print(f'Previsão para os novos dados: {previsao[0]}')


if previsao[0] == 1:
    print('Provavelmente o aluno passará na prova')
else:    print('Provavelmente o aluno não passará na prova')



# Atividades das aulas

# Qual o propósito do Machine Learning?

# Permitir que humanos aprendam a programar máquinas
# Permitir que máquinas aprendam com dados para tomar decisões ou fazer previsões
# Automatizar processos manuais de programação
# Permitir que máquinas aprendam a programar humanos
# Permitir que pessoas aprendam com dados para tomar melhores decisões


# Exemplo simples de Machine Learning com Regressão Logística com a solução da resposta "Qual o propósito do Machine Learning?"

# Dados fictícios: altura e peso
X = np.array([[1.70, 70], [1.80, 80], [1.60, 60], [1.75, 75], [1.65, 65]])
y = np.array(['M', 'M', 'F', 'M', 'F'])

# Treinando o modelo
model = LogisticRegression()
model.fit(X, y)

# Nova amostra
nova_amostra = np.array([[1.50, 54]])
print("Previsão:", model.predict(nova_amostra))





# Qual o objetivo da Regressão Linear?

# Classificar dados em categorias
# Encontrar padrões em dados não estruturados
# Aprender a separar dados em grupos distintos
# Prever valores numéricos a partir de um conjunto de variáveis
# Classificar dados desestruturados



# Exemplo simples de Regressão Linear 

# Dados fictícios: quilometragem e preço de carros
X = np.array([[10000], [20000], [30000], [40000], [50000]])
y = np.array([50000, 45000, 40000, 35000, 30000])

# Treinando o modelo
model = LinearRegression()
model.fit(X, y)

# Previsão para um carro com 25000 km
nova_amostra = np.array([[25000]])
print("Preço previsto:", model.predict(nova_amostra))



# Como o algoritmo K-NN determina a categoria de um novo ponto de dados?

# Encontrando o hiperplano que organiza objetos similares.
# Utilizando uma função logística para determinar a probabilidade de cada categoria.
# Encontrando o hiperplano que melhor separa as categorias.
# Utilizando uma função de custo para minimizar o erro entre as previsões e as categorias verdadeiras.
# Calculando a distância desse ponto para todos os pontos de dados de treinamento e escolhendo os k pontos mais próximos para determinar a categoria.



# Exemplo simples de K-NN - Solução da resposta "Como o algoritmo K-NN determina a categoria de um novo ponto de dados?"

# Dados fictícios: altura e peso
X = np.array([[1.70, 70], [1.80, 80], [1.60, 60], [1.75, 75], [1.65, 65]])
y = np.array(['M', 'M', 'F', 'M', 'F'])

# Criando o modelo K-NN com k=3
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Nova amostra
nova_amostra = np.array([[1.55, 58]])
print("Previsão:", model.predict(nova_amostra))



# Qual é a função principal da Regressão Logística no Aprendizado de Máquina?

# Classificar dados em categorias geralmente binárias
# Separar dados em grupos distintos
# Encontrar padrões em dados não estruturados
# Prever valores numéricos a partir de um conjunto de variáveis
# Classificar dados em grupos não-binários



# Exemplo simples de Regressão Logística - Solução da resposta "Qual é a função principal da Regressão Logística no Aprendizado de Máquina?"

# Dados fictícios: altura e peso
X = np.array([[1.70, 70], [1.80, 80], [1.60, 60], [1.75, 75], [1.65, 65]])
y = np.array(['M', 'M', 'F', 'M', 'F'])

# Treinando o modelo
model = LogisticRegression()
model.fit(X, y)

# Nova amostra
nova_amostra = np.array([[1.55, 58]])
print("Previsão:", model.predict(nova_amostra))




# Qual é a principal função do algoritmo K-NN (K-Nearest Neighbors) no contexto de Aprendizado de Máquina?

# Prever valores numéricos a partir de um conjunto de variáveis.
# Encontrar padrões em dados não estruturados.
# Aprender a separar dados em grupos distintos de forma não supervisionada.
# Classificar dados em categorias, podendo ser binárias ou multi-classes, com base na proximidade dos exemplos no espaço dos dados.
# Criar grupos binários de objetos parecidos sem utilizar rótulos prévios.



# Exemplo simples de K-NN - Solução da resposta "Qual é a principal função do algoritmo K-NN (K-Nearest Neighbors) no contexto de Aprendizado de Máquina?"

# Dados fictícios: altura e peso
X = np.array([[1.70, 70], [1.80, 80], [1.60, 60], [1.75, 75], [1.65, 65]])
y = np.array(['M', 'M', 'F', 'M', 'F'])

# Criando o modelo K-NN com k=3
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Nova amostra
nova_amostra = np.array([[1.55, 58]])
print("Previsão:", model.predict(nova_amostra))



# Uma empresa de vendas online deseja implementar um sistema de recomendação de produtos para seus clientes,
# com base em seu histórico de compras. Qual seria o melhor algoritmo para esse caso?

# Regressão Linear
# Regressão Logística
# K-NN
# Árvores de Decisão
# Random Forest



# Exemplo simples de K-NN aplicado a recomendação - Solução da resposta "Uma empresa de vendas online deseja implementar um sistema de recomendação de produtos para seus clientes, com base em seu histórico de compras. Qual seria o melhor algoritmo para esse caso?"

# Dados fictícios: histórico de compras (valores simplificados)
X = np.array([[1, 0, 0],   # Cliente comprou Coca-cola
              [0, 1, 0],   # Cliente comprou Pepsi
              [0, 0, 1],   # Cliente comprou Fanta
              [1, 1, 0],   # Cliente comprou Coca-cola e Pepsi
              [0, 1, 1]])  # Cliente comprou Pepsi e Fanta

y = np.array(['Coca-cola', 'Pepsi', 'Fanta', 'Coca-cola', 'Pepsi'])

# Criando o modelo K-NN com k=3
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Novo cliente com histórico de compras
novo_cliente = np.array([[1, 0, 1]])  # comprou Coca-cola e Fanta
print("Produto recomendado:", model.predict(novo_cliente))



# Pensar & responder

"""
Pensar & Responder
Uma empresa está planejando um novo projeto de negócios que envolve a análise de dados de clientes para identificar padrões de comportamento e preferências de compra. A equipe de análise de dados está considerando duas abordagens: Aprendizado Supervisionado e Aprendizado Não-Supervisionado.
Levando em consideração o contexto acima, discuta as vantagens e desvantagens de utilizar algoritmos de Aprendizado Supervisionado e Aprendizado Não-Supervisionado para analisar os dados de clientes. Além disso, apresente exemplos de problemas que seriam mais adequados para cada tipo de algoritmo e explique como eles seriam aplicados em cada caso.
"""

# 1. Exemplo de Aprendizado Supervisionado (Classificação de Churn)



# Dados fictícios de clientes
dados = pd.DataFrame({
    "idade": [25, 45, 30, 50, 35, 40],
    "renda": [2000, 5000, 3000, 7000, 4000, 6000],
    "frequencia_compras": [5, 15, 8, 20, 10, 18],
    "churn": [1, 0, 1, 0, 1, 0]  # 1 = cancelou, 0 = manteve
})


# Separar variáveis independentes e alvo
X = dados[["idade", "renda", "frequencia_compras"]]
y = dados["churn"]


# Treinar modelo supervisionado
modelo = LogisticRegression()
modelo.fit(X, y)


# Previsão para novo cliente
novo_cliente = np.array([[28, 2500, 6]])  # idade, renda, frequência
print("Probabilidade de churn:", modelo.predict_proba(novo_cliente))
print("Previsão:", "Cancelará" if modelo.predict(novo_cliente)[0] == 1 else "Manterá")


# 2. Exemplo de Aprendizado Não-Supervisionado (Segmentação de Clientes)

# Dados fictícios de clientes
dados = pd.DataFrame({
    "idade": [25, 45, 30, 50, 35, 40, 22, 55, 60, 28],
    "renda": [2000, 5000, 3000, 7000, 4000, 6000, 1800, 8000, 9000, 2500]
})


X = dados[["idade", "renda"]]


# Treinar modelo não-supervisionado (clusterização)
kmeans = KMeans(n_clusters=3, random_state=42)
dados["cluster"] = kmeans.fit_predict(X)


print(dados)


# Visualização dos clusters
plt.scatter(dados["idade"], dados["renda"], c=dados["cluster"], cmap="viridis")
plt.xlabel("Idade")
plt.ylabel("Renda")
plt.title("Segmentação de Clientes com K-Means")
plt.show()


# Código com DataFrame para com quadro comparativo entre os dois tipos de aprendizado para facilitar a visualização das diferenças:



# Dados do quadro comparativo
dados = {
    "Aspecto": [
        "Definição",
        "Objetivo",
        "Exemplos de Problemas",
        "Vantagens",
        "Desvantagens",
        "Exemplo de Aplicação",
        "Algoritmos Comuns"
    ],
    "Aprendizado Supervisionado": [
        "Modelo treinado com dados rotulados (entrada + saída conhecida).",
        "Aprender a função que mapeia entradas para saídas, permitindo previsões futuras.",
        "Classificação (spam/não spam, churn/não churn) e regressão (previsão de preços, vendas).",
        "Alta precisão em previsões quando há rótulos de qualidade; interpretabilidade dos modelos.",
        "Necessidade de dados rotulados; custo elevado para rotulação; menos flexível a mudanças.",
        "Previsão de churn: prever se um cliente irá cancelar a assinatura com base em histórico.",
        "Regressão Linear, Regressão Logística, Árvores de Decisão, Random Forest, SVM."
    ],
    "Aprendizado Não-Supervisionado": [
        "Modelo treinado apenas com dados de entrada, sem rótulos.",
        "Identificar padrões, estruturas ou agrupamentos ocultos nos dados.",
        "Clusterização (segmentação de clientes), redução de dimensionalidade, detecção de anomalias.",
        "Não requer rótulos; útil para explorar dados e descobrir padrões ocultos.",
        "Resultados podem ser menos interpretáveis; clusters podem não ter relevância prática.",
        "Segmentação de clientes: agrupar clientes por comportamento de compra para campanhas de marketing.",
        "K-Means, DBSCAN, PCA, Hierarchical Clustering."
    ]
}


# Criar DataFrame
df = pd.DataFrame(dados)


# Criar figura
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')


# Renderizar tabela
tabela = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='left', loc='center')


# Ajustar estilo
tabela.auto_set_font_size(False)
tabela.set_fontsize(10)
tabela.auto_set_column_width(col=list(range(len(df.columns))))


# Título
plt.title("Quadro Comparativo: Aprendizado Supervisionado vs Não-Supervisionado", fontsize=14, weight='bold')


# Mostrar imagem
plt.show()

