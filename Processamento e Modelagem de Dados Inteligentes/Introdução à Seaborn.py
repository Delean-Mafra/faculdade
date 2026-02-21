# Introdução a Seaborn

import random

import seaborn as sns # type: ignore
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para gerar vendas aleatórias
def ger_num(min_val=100, max_val=700, quantidade=4):
    return [random.randint(min_val, max_val) for _ in range(quantidade)]

# Gerando dados aleatórios de notas
notas = np.random.normal(loc=70, scale=10, size=100)

# Exibindo o array de notas
notas

dados = pd.DataFrame({'Notas': notas})

sns.kdeplot(data=dados, x='Notas', fill=True)

sns.kdeplot(data=dados['Notas'], fill=True)


altura = np.random.normal(loc=175, scale=10, size=100)
largura = np.random.normal(loc=70, scale=10, size=100)

dados_join_1 = pd.DataFrame({'Altura': altura, 'Largura': largura})

sns.jointplot(data=dados_join_1, x='Altura', y='Largura', kind='scatter', color='blue')
sns.jointplot(data=dados_join_1, x='Altura', y='Largura', kind='kde', color='blue')





dados_vendas = {'Produto': ['A', 'B', 'C', 'D', 'E'],
                  'Vendas Jan': ger_num(),
                  'Vendas Fev': ger_num(),
                  'Vendas Mar': ger_num(),
                  'Vendas Abr': ger_num(),
                  'Vendas Mai': ger_num(),
                  'Vendas Jun': ger_num(),
                  'Vendas Jul': ger_num(),
                  'Vendas Ago': ger_num(),
                  'Vendas Set': ger_num(),
                  'Vendas Out': ger_num(),
                  'Vendas Nov': ger_num(),
                  'Vendas Dez': ger_num()}


df_vendas = pd.DataFrame(dados_vendas)
sns.set_style('whitegrid')

sns.barplot(x='Produto', y='Vendas Jan', data=df_vendas, color='blue')

vendas_scatter = pd.DataFrame({'Vendas': ger_num(),
                               'Gastos': ger_num(),
                               'Média de preço': ger_num()
                               })


plt.scatter(x="Gastos", y="Vendas", c='Média de preço', cmap='Blues', data=vendas_scatter)
plt.title('Vendas vs Gastos')
plt.xlabel('Vendas(Em unidades)')
plt.colorbar().set_label('Média de preço')
plt.show()


sns.barplot(x='Produto', y='Vendas Jan', data=df_vendas)


vendas_scatter = pd.DataFrame({'Vendas': ger_num(),
                               'Gastos': ger_num(),
                                 'Média de preço': ger_num()
                                 })


vendas_scatter_doc = vendas_scatter.copy()
vendas_scatter_doc['Média de preço'] = vendas_scatter_doc['Média de preço'].apply(lambda x: f'R${x:.2f}')




"""Qual dos gráficos abaixo é o mais utilizado para representar a distribuição de um conjunto de dados numéricos?

Scatterplot.

Gráfico de Densidade.

Gráfico de Pizza.

Gráfico de Barras.

Gráfico de Linhas."""


plt.scatter(x="Gastos", y="Vendas", c='Média de preço', cmap='Blues', data=vendas_scatter)
plt.title('Relação entre Vendas e Gastos')
plt.xlabel('Gastos (Em reais)')
plt.ylabel('Vendas (Em unidades)')
plt.colorbar().set_label('Média de preço(Em reais)')
plt.show()





# Qual gráfico de Seaborn é utilizado para mostrar a relação entre duas variáveis numéricas?

# Heatmap

# Boxplot

# Violinplot

# Scatterplot

# Lineplot



# Dados fictícios
horas_estudadas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nota_obtida = [40, 55, 65, 75, 80, 85, 90, 95, 98, 100]

# Gráfico de dispersão
sns.scatterplot(x=horas_estudadas, y=nota_obtida)

plt.title('Relação entre horas estudadas e nota obtida')
plt.xlabel('Horas estudadas')
plt.ylabel('Nota obtida')
plt.show()




# Qual gráfico de Seaborn é mais recomendado para mostrar a distribuição de uma única variável numérica?

# Jointplot  
# Boxplot  
# Violinplot  
# Lineplot  
# Histogram  


# Resposta: Histogram  

# Exemplo de gráfico de distribuição
dados = [70, 65, 80, 75, 90, 85, 60, 72, 68, 77]

# Gráfico de histograma
sns.histplot(dados, bins=5, kde=True, color='blue')

plt.title('Distribuição de uma variável numérica')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()


# Qual é a principal característica de um outlier em um conjunto de dados?

# É um valor acima ou abaixo do intervalo interquartil (IQR)
# É um valor dentro do intervalo interquartil (IQR)
# É um valor que não pode ser visualizado em um gráfico de dispersão
# É um valor que aparece com frequência em um conjunto de dados
# É um valor que pode ser substituído por um valor médio

# Resposta: É um valor acima ou abaixo do intervalo interquartil (IQR)


# Exemplo simples de detecção de outliers
dados = [10, 12, 13, 15, 18, 19, 20, 22, 100]  # 100 é um outlier

# Boxplot para visualizar outliers
sns.boxplot(x=dados)

plt.title('Detecção de Outliers em um Conjunto de Dados')
plt.xlabel('Valores')
plt.show()




# Qual dos gráficos abaixo é recomendado para representar a relação entre duas variáveis numéricas,
# mostrando a distribuição marginal de cada uma delas na forma de histograma ou densidade?

# Gráfico de Barra
# Gráfico de Pizza
# Gráfico de Scatterplot
# Gráfico de Jointplot
# Gráfico de Boxplot

# Resposta: Gráfico de Jointplot


# Exemplo de gráfico de Jointplot

# Dados fictícios
x = [10, 20, 30, 40, 50, 60, 70]
y = [15, 25, 35, 45, 55, 65, 75]

# Jointplot com regressão
sns.jointplot(x=x, y=y, kind="reg", color="blue")

plt.suptitle('Relação entre duas variáveis com distribuições marginais')
plt.show()


# A empresa XYZ realizou uma pesquisa com seus clientes para avaliar a satisfação com relação à qualidade do atendimento e ao tempo de espera.
# Para visualizar as informações de forma mais clara, foi criado um gráfico de jointplot utilizando a biblioteca Seaborn em Python.

# Qual o tipo de gráfico recomendado para representar a relação entre duas variáveis numéricas em um gráfico de duas dimensões?

# Gráfico de barras
# Gráfico de caixa
# Joinplot ou scatterplot
# Gráfico de linhas
# Gráfico 3D

# Resposta: Joinplot ou scatterplot


# Exemplo de gráfico de dispersão (scatterplot)
x = [5, 10, 15, 20, 25, 30]
y = [7, 14, 18, 22, 28, 35]

sns.scatterplot(x=x, y=y)

plt.title('Relação entre duas variáveis numéricas')
plt.xlabel('Tempo de espera')
plt.ylabel('Satisfação')
plt.show()
