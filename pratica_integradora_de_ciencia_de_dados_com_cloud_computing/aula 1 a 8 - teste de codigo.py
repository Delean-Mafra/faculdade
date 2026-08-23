# ===== IMPORTAÇÕES =====
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# ===== CÓDIGO =====

arr = np.zeros((3, 4))  
print(arr)

matriz = np.array([
    [1, 2, 3],   # linha 0
    [4, 5, 6],   # linha 1
    [7, 8, 9]    # linha 2
])
print(matriz[1, 2])  # Acessa o elemento na linha 1, coluna 2 (resultado: 6)

arr = np.array([1, 2, 3, 4, 5])
media = np.mean(arr)
print(media)  # Resultado: 3.0

matriz = np.array([
    [1, 2, 3],   # linha 0
    [4, 5, 6],   # linha 1
    [7, 8, 9]    # linha 2
])
arr = np.arange(1, 11)
print(arr)  # Resultado: [ 1  2  3  4  5  6  7  8  9 10]
matriz = np.arange(1, 13).reshape(3, 4)
print(matriz)  # Resultado:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Criando um DataFrame simples
dados = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda'],
    'Idade': [23, 34, 29, 40, 31, 27]
})

print(dados.head())      # Mostra as 5 primeiras linhas
print(dados.head(3))     # Mostra apenas as 3 primeiras linhas
print(dados.tail())      # Mostra as 5 últimas linhas

dados = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 34, 29]
})


# Selecionando a coluna "Nome"
coluna_nomes = dados['Nome']
print(coluna_nomes)

# Criando um DataFrame com valores ausentes
dados = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, np.nan, 29],
    'Cidade': ['São Paulo', 'Rio de Janeiro', None]
})

print("Antes do dropna:")
print(dados)

# Removendo linhas com valores ausentes
dados_limpos = dados.dropna()

print("\nDepois do dropna:")
print(dados_limpos)

dados = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 34, 29]
})

# Ordenando pela coluna "Idade"
ordenado = dados.sort_values('Idade')
print(ordenado)

# Ordenando em ordem decrescente
ordenado_desc = dados.sort_values('Idade', ascending=False)
print(ordenado_desc)

dados = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [23, 34, 29, 40]
})

# Selecionando apenas as linhas onde a idade é maior que 30
filtro = dados[dados['Idade'] > 30]
print(filtro)

dados = pd.DataFrame({
    'Produto': ['Camiseta', 'Calça', 'Tênis'],
    'Preço': [29.99, 49.99, 79.99]
})

# Média de toda a coluna "Preço"
media_preco = dados['Preço'].mean()
print("Média dos preços:", media_preco)

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 34, 29]
})

# Selecionando a coluna "Nome"
coluna_nome = df['Nome']
print(coluna_nome)

# Importando um arquivo CSV
df = pd.read_csv("dados.csv")

print(df.head())  # Mostra as primeiras linhas do DataFrame

df = pd.DataFrame({
    'Idade': [20, 25, 30, 35, 40],
    'Salário': [2000, 2500, 3000, 3500, 4000]
})


# Média da coluna "Idade"
media_idade = df['Idade'].mean()
print("Média das idades:", media_idade)

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    'Quantidade': [2, 4, 6],
    'Preço': [10, 20, 30]
})

# Criando uma nova coluna "Total" com base no cálculo entre colunas
df['Total'] = df['Quantidade'] * df['Preço']

print(df)

df = pd.DataFrame({
    'Quantidade': [2, 4, 6],
    'Preço': [10, 20, 30]
})

# Usando lambda com apply em linha
df['Total'] = df.apply(lambda x: x['Quantidade'] * x['Preço'], axis=1)
df['Total'] = df['Quantidade'] * df['Preço']

df = pd.DataFrame({
    'Idade': [23, 34, 29, 40],
    'Salário': [2500, 3200, 2800, 5000]
})

# Valor máximo da coluna "Idade"
max_idade = df['Idade'].max()
print("Maior idade:", max_idade)

# Valor máximo da coluna "Salário"
max_salario = df['Salário'].max()
print("Maior salário:", max_salario)

# Criando um gráfico simples
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Exemplo de gráfico")

# Salvando em PDF
plt.savefig("grafico.pdf")

# Exibindo na tela
plt.show()

# Dados de exemplo
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 12]

# Criando gráfico de barras
plt.bar(categorias, valores)

# Personalizando
plt.title("Exemplo de Gráfico de Barras")
plt.xlabel("Categorias")
plt.ylabel("Valores")
# Exibindo
plt.show()

x = [1, 2, 3, 4, 5]
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

# Adicionando título
plt.title("Exemplo de Gráfico de Linha")

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]

# Primeiro subplot (1 linha, 2 colunas, posição 1)
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Gráfico 1")

# Segundo subplot (1 linha, 2 colunas, posição 2)
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Gráfico 2")

plt.show()

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Linha vermelha
plt.plot(x, y, color='red')

plt.title("Exemplo de gráfico com cor personalizada")
plt.show()

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2, 1)

axs[0].plot(x, y1)   # Primeiro subplot (linha superior)
axs[0].set_title("Gráfico de Linha")

axs[1].scatter(x, y2)  # Segundo subplot (linha inferior)
axs[1].set_title("Gráfico de Dispersão")

plt.show()

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, color='blue', linestyle='--', linewidth=2)
plt.title("Função Seno")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()

# Criando arrays
arr = np.arange(1, 11)
matriz = np.arange(1, 13).reshape(3, 4)

# Exibindo arrays
print("Array 'arr':")
print(arr)

print("\nMatriz 'matriz':")
print(matriz)

# Operações com arrays
arr_slice = arr[2:6]
arr_resultado = arr * 2
soma_matriz = np.sum(matriz)
media_arr = np.mean(arr)
matriz_transposta = np.transpose(matriz)
arr_concatenado = np.concatenate((arr, arr_slice))

# Exibindo resultados
print("\nArray 'arr_slice':")
print(arr_slice)

print("\nArray 'arr_resultado':")
print(arr_resultado)

print("\nSoma da matriz 'matriz':", soma_matriz)
print("\nMédia do array 'arr':", media_arr)

print("\nMatriz transposta:")
print(matriz_transposta)

print("\nArray concatenado 'arr_concatenado':", arr_concatenado)

# Criando um arquivo CSV de exemplo antes de importá-lo
dados_exemplo = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [23, 34, 29, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador']
})
dados_exemplo.to_csv("dados.csv", index=False)
print("\nArquivo 'dados.csv' criado com sucesso!")

X = [
 [1, 100, 2],   # 1 = intercepto, 100 = área, 2 = quartos
 [1, 150, 3],
 [1, 120, 2],
 [1, 200, 4],
 [1, 80,  1]
]

# Dados simulados
X = np.array([2, 4, 6, 8, 10]).reshape(-1, 1)
y = np.array([60, 65, 70, 75, 80])

# Modelo
model = LinearRegression()
model.fit(X, y)

# Previsão
y_pred = model.predict(X)

# Avaliação
print("MSE:", mean_squared_error(y, y_pred))
print("R²:", r2_score(y, y_pred))

# Divisão dos dados em treino e teste (usando os mesmos dados X e y)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criação e treinamento do modelo
modelo = LinearRegression()
modelo.fit(x_train, y_train)

# Previsões
y_prev = modelo.predict(x_test)

# Cálculo do erro quadrático médio (MSE)
mse = mean_squared_error(y_test, y_prev)

print("MSE do modelo de treino/teste:", mse)

A = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

# Broadcasting soma b a cada linha de A
print("\nResultado do Broadcasting:")
print(A + b)

# Exemplos comentados para referência:
# y2 = [cos(0), cos(π/2), cos(π)]
# y2 = [1.0, 0.0, -1.0]
# plt.show()
# plt.subplot(nlinhas, ncolunas, índice)
