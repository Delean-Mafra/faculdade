import array # Importa o módulo array para manipulação de arrays eficientes
from re import sub # Importa a função sub do módulo re para substituições com expressões regulares
from tkinter import font # Importa o módulo font do tkinter para configurações de texto em interfaces
from turtle import color # Importa a função color do módulo turtle para manipulação de cores gráficas
import numpy as np # Importa a biblioteca NumPy para cálculos numéricos e processamento de arrays
from sympy import im # Importa a função im do sympy para lidar com números imaginários
import pandas as pd # Importa a biblioteca Pandas para análise e manipulação de dados
import matplotlib.pyplot as plt # Importa o módulo pyplot do Matplotlib para visualização de dados
from mpl_toolkits.mplot3d import Axes3D # Importa ferramentas para criação de gráficos tridimensionais (3D)

arr1 = np.array([1, 2, 3, 4, 5]) # criando um array unidimensional

arr2 = np.array([[0,9,8,7,6,5,4],[4,5,6,7,8,9,0]]) # criando um array bidimensional

print("Array 1:", arr1) # imprimindo o array 1
print("Array 2:\n", arr2) # imprimindo o array 2

array_1 = np.array([1,1,1]) # criando um array unidimensional

array_2 = np.array([2,2,2]) # criando um array unidimensional

soma_array = array_1 + array_2 # somando os arrays


print("Soma dos arrays:", soma_array) # imprimindo a soma dos arrays

subtracao_array = array_2 - array_1 # subtraindo os arrays

print("Subtração dos arrays:", subtracao_array) # imprimindo a subtração dos arrays
print(subtracao_array[0]) # acessando o primeiro elemento do array de subtração

nova_array = np.append(array_1, array_2) # concatenando os arrays

print("Nova array após append:", nova_array) # imprimindo a nova array

print(nova_array[0:4]) # fatiando a nova array

seno_array = np.sin(nova_array) # aplicando a função seno em cada elemento da nova array
print(seno_array) # Exibe o array com os valores de seno calculados

media_array = np.mean(nova_array) # calculando a média da nova array

mediana_array = np.median(nova_array) # calculando a mediana da nova array

print("Média da nova array:", media_array) # imprimindo a média da nova array
print("Mediana da nova array:", mediana_array) # imprimindo a mediana da nova array

desvio_padrao = np.std(nova_array) # calculando o desvio padrão da nova array
print("Desvio padrão da nova array:", desvio_padrao) # imprimindo o desvio padrão da nova array



nomes_produtos_camisetas = ["Camisa Polo", "Camiseta Regata", "Camiseta Manga Longa", "Camiseta Básica", "Camiseta Estampada"] # lista de nomes de produtos


df_loja = pd.DataFrame({
    "ID Produto": np.random.randint(1,11, 1000), # gerando 1000 IDs de produtos aleatórios entre 1 e 10
    "Nome produto": np.random.choice(nomes_produtos_camisetas,1000), # escolhendo aleatoriamente nomes de produtos da lista
    'Quantidade Vendida': np.round(np.random.uniform(10,100,1000),2), # gerando quantidades vendidas aleatórias entre 10 e 100, arredondadas para 2 casas decimais
    'Data da Venda': np.random.choice(pd.date_range(start = '2021-01-01',end = '2021-12-31'),1000), # escolhendo aleatoriamente datas de venda em 2021
    'Preço Unitário': np.round(np.random.uniform(20.0,150.0,1000),2) # gerando preços unitários aleatórios entre 20.0 e 150.0, arredondados para 2 casas decimais
    
    
    })

print(df_loja) # imprimindo o DataFrame

print(df_loja.describe()) # exibindo estatísticas descritivas do DataFrame

df_loja.to_csv('vendas.csv',index=False) # salvando o DataFrame em um arquivo CSV sem o índice

# Desafio: Regenerar (recriar) esta base com nomes de compradores, datas de aniversário e quantidade comprada

df_loja_novo = df_loja # criando uma cópia do DataFrame original

nomes_compradores = ["Ana", "Bruno", "Carla", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"] # lista de nomes de compradores
df_loja_novo['Nome Comprador'] = np.random.choice(nomes_compradores,1000) # escolhendo aleatoriamente nomes de compradores da lista
df_loja_novo['Data de Aniversário'] = np.random.choice(pd.date_range(start = '1970-01-01',end = '2003-12-31'),1000) # escolhendo aleatoriamente datas de aniversário entre 1970 e 2003
df_loja_novo['Quantidade Comprada'] = np.round(np.random.uniform(1,10,1000),2) # gerando quantidades compradas aleatórias entre 1 e 10, arredondadas para 2 casas decimais
print(df_loja_novo) # Exibe o novo DataFrame com as informações de compradores e aniversário



print(df_loja.loc[:'ID Produto']) # Acessa e imprime as linhas até a coluna ID Produto


# consulta os nomes dos produtos em maisuscula sem alterar o dataframe original
print(df_loja['Nome produto'].map(lambda x: x.upper())) # Exibe os nomes dos produtos em caixa alta sem modificar o original

# passa o nome dos produtos para caixa alta/maiuscula utilizando map e lambda
# df_loja['Nome produto'] = df_loja['Nome produto'].map(lambda x: x.upper())


print(df_loja.sort_values(by='Quantidade Vendida', ascending=False)) # ordena o dataframe pela coluna 'Quantidade Vendida' em ordem decrescente

print(df_loja) # Exibe o DataFrame após as operações de filtragem e ordenação


df_loja.groupby('Preço Unitário').mean(numeric_only=True) # agrupa os dados por 'Preço Unitário' e calcula a média das outras colunas numéricas

df_loja.groupby('Nome produto').sum(numeric_only=True) # agrupa os dados por 'Nome produto' e calcula a soma das outras colunas numéricas




# Agrupando os dados por 'Nome Produto' e calculando a média
df_grouped = df_loja.groupby('Nome produto').mean(numeric_only=True) # Agrupa por produto e calcula a média das vendas para valores numéricos

# Gerando o gráfico de barras com as médias de vendas por produto
plt.bar(df_grouped.index, df_grouped['Quantidade Vendida']) # Cria um gráfico de barras com os produtos no eixo X e vendas no Y
plt.xticks(rotation=45) # Rotaciona os nomes dos produtos no eixo X em 45 graus para evitar sobreposição
plt.ylabel('Média de vendas') # Rótulo do eixo y
plt.title('Média de vendas por produto') # Título do gráfico
plt.show() 




df_loja['Mês'] = pd.DatetimeIndex(df_loja['Data da Venda']).month # Extrai o mês da data de venda
df_loja_vendas_mes = df_loja.groupby(['Nome produto', 'Mês'])['Quantidade Vendida'].sum() # Agrupa por nome do produto e mês, somando a quantidade vendida
df_loja_vendas_manga_longa = df_loja_vendas_mes.loc['Camiseta Manga Longa'] # Seleciona os dados para Camisa Manga Longa
df_loja_vendas_gola_polo = df_loja_vendas_mes.loc['Camisa Polo']    # Seleciona os dados para Camisa Gola Polo
df_loja_vendas_camiseta_regata = df_loja_vendas_mes.loc['Camiseta Regata']  # Seleciona os dados para Camiseta Regata
df_loja_vendas_camiseta_estampada = df_loja_vendas_mes.loc['Camiseta Estampada']    # Seleciona os dados para Camiseta Estampada
df_loja_vendas_camiseta_basica = df_loja_vendas_mes.loc['Camiseta Básica']  # Seleciona os dados para Camiseta Básica




plt.plot(df_loja_vendas_manga_longa.index, df_loja_vendas_manga_longa.values, label='Camisa Manga Longa') # Plota a linha para Camisa Manga Longa
plt.plot(df_loja_vendas_gola_polo.index, df_loja_vendas_gola_polo.values, label='Camisa Gola Polo') # Plota a linha para Camisa Gola Polo
plt.plot(df_loja_vendas_camiseta_regata.index, df_loja_vendas_camiseta_regata.values, label='Camiseta Regata') # Plota a linha para Camiseta Regata
plt.plot(df_loja_vendas_camiseta_estampada.index, df_loja_vendas_camiseta_estampada.values, label='Camiseta Estampada') # Plota a linha para Camiseta Estampada
plt.plot(df_loja_vendas_camiseta_basica.index, df_loja_vendas_camiseta_basica.values, label='Camiseta Básica') # Plota a linha para Camiseta Básica

# Personalização do gráfico
plt.legend() # Adiciona a legenda
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']) # Define os rótulos do eixo x
plt.ylabel('Quantidade vendida') # Rótulo do eixo y
plt.title('Quantidade total vendida de cada produto por mês')
plt.tight_layout() # Ajusta o layout para evitar cortes
plt.show() # Exibe o gráfico



df_agrupado = df_loja.groupby('Nome produto').mean(numeric_only=True) # Agrupa por nome do produto e calcula a média
plt.bar(df_agrupado.index, df_agrupado['Quantidade Vendida'], color=['red', 'blue', 'green', 'orange', 'purple' ]) # Define cores diferentes para cada barra
plt.xticks(rotation=45) # Rotaciona os rótulos do eixo x para melhor visualização
plt.ylabel('Média de vendas') # Rótulo do eixo y
plt.title('Média de vendas por produto') # Título do gráfico
plt.grid(axis='y', linestyle='--', alpha=0.7) # Adiciona uma grade horizontal ao gráfico
plt.tight_layout() # Ajusta o layout para evitar cortes
plt.show() # Exibe o gráfico

# Gráfico de dispersão
plt.scatter(df_loja['Preço Unitário'], df_loja['Quantidade Vendida'], alpha=0.5, s=50, c='purple') # Define a transparência, tamanho e cor dos pontos

# Personalização dos eixos e título
plt.xlabel('Preço Unitário', fontsize=12) # Rótulo do eixo x
plt.ylabel('Quantidade Vendida', fontsize=12) # Rótulo do eixo y
plt.title('Relação entre o preço unitário e a quantidade vendida', fontsize=14) # Título do gráfico

# Grade no gráfico
plt.grid(axis='both', linestyle='--', alpha=0.7) # Adiciona uma grade ao gráfico

# Ajuste de layout e exibição
plt.tight_layout() # Ajusta o layout para evitar cortes
plt.show() # Exibe o gráfico



df_loja['Mês'] = pd.DatetimeIndex(df_loja['Data da Venda']).month # Extrai o mês da data de venda
df_loja_vendas_por_mes = df_loja.groupby(['Nome produto', 'Mês'])['Quantidade Vendida'].sum() # Agrupa por nome do produto e mês, somando a quantidade vendida
df_agrupados = df_loja_vendas_por_mes.unstack() # Transforma os meses em colunas
df_agrupados.plot(figsize=(5,2),kind='line', marker = 'o') # Define o tamanho da figura
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']) # Define os rótulos do eixo x
plt.ylabel('Quantidade Vendida') # Rótulo do eixo y 
plt.title('Quantidade total vendida de cada produto por mês') # Título do gráfico
plt.show() # Exibe o gráfico

df_loja_vendas_por_produto = df_loja.groupby('Nome produto')['Quantidade Vendida'].sum() # Agrupa por nome do produto, somando a quantidade vendida
df_loja_vendas_por_produto.plot(kind='pie', autopct='%1.1f%%') # Define o tamanho da figura
plt.title('Distribuição percentual das vendas por produto') # Título do gráfico
plt.show() # Exibe o gráfico


plt.figure(figsize=(10,7)) # Define o tamanho da figura (largura=10, altura=7 polegadas)
plt.scatter(df_loja['Preço Unitário'], df_loja['Quantidade Vendida'], # Cria gráfico de dispersão com Preço (x) e Quantidade (y)
            s=df_loja['Quantidade Vendida'] * 5, # Define o tamanho dos pontos proporcional à quantidade vendida
            c=df_loja['Preço Unitário'], cmap='plasma') # Define a cor dos pontos com base no preço unitário usando mapa de cores 'plasma'
plt.xlabel('Preço Unitário') # Rótulo do eixo x
plt.ylabel('Quantidade Vendida') # Rótulo do eixo y
plt.title('Relação entre o preço unitário e a quantidade vendida') # Título do gráfico
plt.colorbar(label='Preço Unitário') # Barra de cores lateral para indicar a escala do preço unitário
plt.tight_layout() # Ajusta o layout automaticamente para evitar cortes nos rótulos
plt.show() # Exibe o gráfico na tela

df_agrupado = df_loja.groupby('Nome produto').mean(numeric_only=True) # Agrupa por nome do produto e calcula a média das colunas numéricas

print(df_agrupado) # Imprime o DataFrame agrupado


print(df_loja_vendas_mes) # Imprime as vendas por mês e produto
print(df_loja_vendas_manga_longa) # Imprime as vendas de Camisa Manga Longa
print(df_loja_vendas_gola_polo)   # Imprime as vendas de Camisa Gola Polo
print(df_loja_vendas_camiseta_regata) # Imprime as vendas de Camiseta Regata
print(df_loja_vendas_camiseta_estampada)  # Imprime as vendas de Camiseta Estampada
print(df_loja_vendas_camiseta_basica) # Imprime as vendas de Camiseta Básica


df_grouped = df_loja.groupby('Nome produto').mean(numeric_only=True) # Agrupa por nome do produto e calcula a média das colunas numéricas
labels = df_grouped.index # Extrai os rótulos (nomes dos produtos) para o eixo X

camisa_manga_longa = df_grouped.loc['Camiseta Manga Longa', 'Quantidade Vendida'] # Quantidade vendida de Camiseta Manga Longa
camisa_gola_polo   = df_grouped.loc['Camisa Polo', 'Quantidade Vendida'] # Quantidade vendida de Camisa Polo
camiseta_basica    = df_grouped.loc['Camiseta Básica', 'Quantidade Vendida'] # Quantidade vendida de Camiseta Básica
camiseta_regata    = df_grouped.loc['Camiseta Regata', 'Quantidade Vendida'] # Quantidade vendida de Camiseta Regata
camiseta_estampada = df_grouped.loc['Camiseta Estampada', 'Quantidade Vendida'] # Quantidade vendida de Camiseta Estampada

fig, ax = plt.subplots() # Cria uma figura e um conjunto de subplots

ax.bar(labels, camisa_manga_longa, label='Camiseta Manga Longa', color='b') # Adiciona a barra base para Camiseta Manga Longa
ax.bar(labels, camisa_gola_polo,   label='Camisa Polo',
       bottom=camisa_manga_longa, color='g') # Stack de Camisa Polo sobre a Manga Longa
ax.bar(labels, camiseta_basica,    label='Camiseta Básica',
       bottom=camisa_manga_longa + camisa_gola_polo, color='r') # Stack de Camiseta Básica sobre as anteriores
ax.bar(labels, camiseta_regata,    label='Camiseta Regata',
       bottom=camisa_manga_longa + camisa_gola_polo + camiseta_basica, color='c') # Stack de Camiseta Regata
ax.bar(labels, camiseta_estampada, label='Camiseta Estampada',
       bottom=camisa_manga_longa + camisa_gola_polo + camiseta_basica + camiseta_regata,
       color='m') # Stack de Camiseta Estampada no topo

ax.set_ylabel('Quantidade Vendida') # Define o título do eixo vertical
ax.set_xlabel('Nome do Produto') # Define o título do eixo horizontal
ax.set_title('Vendas por Produto') # Define o título do gráfico de barras empilhadas
ax.legend() # Adiciona a legenda para identificar cada cor de produto

plt.show() # Exibe o gráfico de barras empilhadas


fig = plt.figure() # Cria uma nova figura para o gráfico 3D
ax = fig.add_subplot(111, projection='3d') # Adiciona um subplot 3D à figura

x = df_loja['ID Produto'] # Define os dados para o eixo X (ID do Produto)
y = df_loja['Quantidade Vendida'] # Define os dados para o eixo Y (Quantidade Vendida)
z = df_loja['Preço Unitário'] # Define os dados para o eixo Z (Preço Unitário)

ax.scatter(x, y, z) # Cria o gráfico de dispersão tridimensional

ax.set_xlabel('ID Produto') # Define o rótulo do eixo X no 3D
ax.set_ylabel('Quantidade Vendida') # Define o rótulo do eixo Y no 3D
ax.set_zlabel('Preço Unitário') # Define o rótulo do eixo Z no 3D
plt.show() # Exibe o gráfico 3D simples


fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d') # Adiciona o subplot 3D
x = df_loja['ID Produto'] # Define os dados do eixo X
y = df_loja['Quantidade Vendida'] # Define os dados do eixo Y
z = df_loja['Preço Unitário'] # Define os dados do eixo Z

ax.scatter(x, y, z, c=z, cmap='coolwarm', s=y*10) # Cria dispersão 3D com cores variando pelo preço e tamanho pela quantidade
ax.set_xlabel('ID Produto',fontsize=12) # Rótulo do eixo X com fonte tamanho 12
ax.set_ylabel('Quantidade Vendida',fontsize=12) # Rótulo do eixo Y com fonte tamanho 12
ax.set_zlabel('Preço Unitário',fontsize=12) # Rótulo do eixo Z com fonte tamanho 12
ax.tick_params(axis='both', labelsize=10) # Ajusta o tamanho das fontes dos eixos

ax.set_xlim(0, 11) # Define o limite visível do eixo X
ax.set_ylim(0, 23) # Define o limite visível do eixo Y
ax.set_zlim(10, 110) # Define o limite visível do eixo Z
plt.title('Relação entre ID Produto, Quantidade Vendida e Preço Unitário', fontsize=16) # Define o título do gráfico 3D
plt.show() # Exibe o gráfico 3D personalizado
