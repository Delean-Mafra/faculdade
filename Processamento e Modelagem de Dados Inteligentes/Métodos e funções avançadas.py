# Projeto de notas de alunos com métodos Apply()



# importando a biblioteca
import pandas as pd


# criando dados dos alunos
dados_alunos = {
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eva'],
    "Matematica": [85, 90, 78, 92, 88],
    "Portugues": [88, 76, 95, 89, 91],
    "Ciencias": [90, 85, 88, 92, 87],
    "Historia": [80, 82, 84, 86, 88]    

}

df_notas = pd.DataFrame(dados_alunos)
# print(df_notas)


def calcular_media_aluno(linha):
    return linha[['Matematica', 'Portugues', 'Ciencias', 'Historia']].mean()


df_notas['Media'] = df_notas.apply(calcular_media_aluno, axis=1)
print("\nDataFrame com Média dos Alunos:")
print(df_notas)


# Alterar o axis para 0 sem erros(É possivels usar outros formatos de dados e até mesmo funções.)

def calcular_media_materia(coluna):
    # Calcula a média apenas se a coluna for numérica
    if coluna.dtype in ['float64', 'int64']:
        return coluna.mean()
    return coluna[0]  # Retorna o primeiro valor para colunas não numéricas

df_notas.loc['Media'] = df_notas.apply(calcular_media_materia, axis=0)
print("\nDataFrame com Média das Matérias:")
print(df_notas)




# Projeto câmbio Financerio


# Cria conversão de dados

dados_cambio = {
    'produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
    'Preco USD': [100, 150, 200, 250],
    'Preco EUR': [90, 140, 190, 240],
    'Preco JPY': [80, 130, 180, 230]

}


def conversao_para_usd(preco, taxa):
    return preco / taxa


taxa = {
    'Preco USD': 1,
    'Preco EUR': 0.9,
    'Preco JPY': 110
}

df_cambio = pd.DataFrame(dados_cambio)
print("\nDataFrame de Preços em Diferentes Moedas:")

# Funções Lambda

# Adcionar nova coluna com preços em libras esterlinas (GBP)

df_cambio['Preco GBP'] = df_cambio['Preco USD'].apply(lambda x:x / 1.4)

print(df_cambio)


# Altera o nome da coluna produto para item

df_cambio.rename(columns={'produto': 'item'}, inplace=True)
print("\nDataFrame com coluna renomeada:")
print(df_cambio)


# Concatenação de variáveis damais

# criando conjunto de dados 


dados_1 = {
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eva'],
    "idade": [30, 90, 40, 20, 25],
    'Genero': ['F', 'M', 'F', 'M', 'F'],
    'Salario': [3000, 4000, 3500, 2800, 3200]

}

dados_2 = {
    'nome': ['João', 'Mario', 'José', 'Claudio', 'Manuela'],
    'idade': [10, 25, 78, 92, 50],
    'Genero': ['M', 'M', 'M', 'M', 'F'],
    'Salario': [1500, 2200, 1800, 2500, 3000]


}


dados_1 = pd.DataFrame(dados_1)

dados_2 = pd.DataFrame(dados_2)

print("\nDataFrame 1:")
print(dados_1)
print("\nDataFrame 2:")
print(dados_2)







dados_1['UsaMaquiagem'] = dados_1['Genero'].map({'F': True, 'M': False}).astype(int)
dados_2['UsaMaquiagem'] = dados_2['Genero'].map({'F': True, 'M': False}).astype(int)

print(dados_1)



df_concatenado = pd.concat([dados_1, dados_2], ignore_index=True)
print("\nDataFrame Concatenado:")



df_teste = df_concatenado



for index, row in df_teste.iterrows():
    if row['idade'] >= 18:
        df_teste.at[index, 'MaiorIdade'] = 'Sim'
    else:
        df_teste.at[index, 'MaiorIdade'] = 'Não'

print(df_teste)
