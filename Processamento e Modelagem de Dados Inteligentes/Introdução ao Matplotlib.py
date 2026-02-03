import array
from re import sub
import numpy as np
from sympy import im
import pandas as pd
import matplotlib.pyplot as plt

arr1 = np.array([1, 2, 3, 4, 5])

arr2 = np.array([[0,9,8,7,6,5,4],[4,5,6,7,8,9,0]])

print("Array 1:", arr1)
print("Array 2:\n", arr2)

array_1 = np.array([1,1,1])

array_2 = np.array([2,2,2])

soma_array = array_1 + array_2


print("Soma dos arrays:", soma_array)

subtracao_array = array_2 - array_1

print("Subtração dos arrays:", subtracao_array)

print(subtracao_array[0])

nova_array = np.append(array_1, array_2)

print("Nova array após append:", nova_array)

print(nova_array[0:4])

seno_array = np.sin(nova_array)
print(seno_array)

media_array = np.mean(nova_array)

mediana_array = np.median(nova_array)

print("Média da nova array:", media_array)
print("Mediana da nova array:", mediana_array)

desvio_padrao = np.std(nova_array)
print("Desvio padrão da nova array:", desvio_padrao)



nomes_produtos_camisetas = ["Camisa Polo", "Camiseta Regata", "Camiseta Manga Longa", "Camiseta Básica", "Camiseta Estampada"]

df_loja = pd.DataFrame({
    "ID Produto": np.random.randint(1,11, 1000),
    "Nome produto": np.random.choice(nomes_produtos_camisetas,1000),
    'Quantidade Vendida': np.round(np.random.uniform(10,100,1000),2),
    'Data da Venda': np.random.choice(pd.date_range(start = '2021-01-01',end = '2021-12-31'),1000),
    'Preço Unitário': np.round(np.random.uniform(20.0,150.0,1000),2)
    
    
    })

print(df_loja)

print(df_loja.describe())

df_loja.to_csv('vendas.csv',index=False)

# Desafio: Regenerar (recriar) esta base com nomes de compradores, datas de aniversário e quantidade comprada

df_loja_novo = df_loja

nomes_compradores = ["Ana", "Bruno", "Carla", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]
df_loja_novo['Nome Comprador'] = np.random.choice(nomes_compradores,1000)
df_loja_novo['Data de Aniversário'] = np.random.choice(pd.date_range(start = '1970-01-01',end = '2003-12-31'),1000)
df_loja_novo['Quantidade Comprada'] = np.round(np.random.uniform(1,10,1000),2)
print(df_loja_novo)



print(df_loja.loc[:'ID Produto'])


# consulta os nomes dos produtos em maisuscula sem alterar o dataframe original
print(df_loja['Nome produto'].map(lambda x: x.upper()))

# passa o nome dos produtos para caixa alta/maiuscula utilizando map e lambda
# df_loja['Nome produto'] = df_loja['Nome produto'].map(lambda x: x.upper())


print(df_loja.sort_values(by='Quantidade Vendida', ascending=False))

print(df_loja)


df_loja.groupby('Preço Unitário').mean(numeric_only=True)

df_loja.groupby('Nome produto').sum(numeric_only=True)




# Agrupando os dados por 'Nome Produto' e calculando a média
df_grouped = df_loja.groupby('Nome produto').mean(numeric_only=True)

# Gerando o gráfico de barras com as médias de vendas por produto
plt.bar(df_grouped.index, df_grouped['Quantidade Vendida'])
plt.xticks(rotation=45)
plt.ylabel('Média de vendas')
plt.title('Média de vendas por produto')
plt.show()




df_loja['Mês'] = pd.DatetimeIndex(df_loja['Data da Venda']).month

df_loja_vendas_mes = df_loja.groupby(['Nome produto', 'Mês'])['Quantidade Vendida'].sum()

df_loja_vendas_manga_longa = df_loja_vendas_mes.loc['Camiseta Manga Longa']

df_loja_vendas_gola_polo = df_loja_vendas_mes.loc['Camisa Polo']

df_loja_vendas_camiseta_regata = df_loja_vendas_mes.loc['Camiseta Regata']

df_loja_vendas_camiseta_estampada = df_loja_vendas_mes.loc['Camiseta Estampada']

df_loja_vendas_camiseta_basica = df_loja_vendas_mes.loc['Camiseta Básica']




plt.plot(df_loja_vendas_manga_longa.index, df_loja_vendas_manga_longa.values, label='Camisa Manga Longa')
plt.plot(df_loja_vendas_gola_polo.index, df_loja_vendas_gola_polo.values, label='Camisa Gola Polo')
plt.plot(df_loja_vendas_camiseta_regata.index, df_loja_vendas_camiseta_regata.values, label='Camiseta Regata')
plt.plot(df_loja_vendas_camiseta_estampada.index, df_loja_vendas_camiseta_estampada.values, label='Camiseta Estampada')
plt.plot(df_loja_vendas_camiseta_basica.index, df_loja_vendas_camiseta_basica.values, label='Camiseta Básica')

# Personalização do gráfico
plt.legend()
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'])
plt.ylabel('Quantidade vendida')
plt.title('Quantidade total vendida de cada produto por mês')
plt.tight_layout()
plt.show()



df_agrupado = df_loja.groupby('Nome produto').mean(numeric_only=True)
plt.bar(df_agrupado.index, df_agrupado['Quantidade Vendida'], color=['red', 'blue', 'green', 'orange', 'purple' ])
plt.xticks(rotation=45)
plt.ylabel('Média de vendas')
plt.title('Média de vendas por produto')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfico de dispersão
plt.scatter(df_loja['Preço Unitário'], df_loja['Quantidade Vendida'], alpha=0.5, s=50, c='purple')

# Personalização dos eixos e título
plt.xlabel('Preço Unitário', fontsize=12)
plt.ylabel('Quantidade Vendida', fontsize=12)
plt.title('Relação entre o preço unitário e a quantidade vendida', fontsize=14)

# Grade no gráfico
plt.grid(axis='both', linestyle='--', alpha=0.7)

# Ajuste de layout e exibição
plt.tight_layout()
plt.show()
