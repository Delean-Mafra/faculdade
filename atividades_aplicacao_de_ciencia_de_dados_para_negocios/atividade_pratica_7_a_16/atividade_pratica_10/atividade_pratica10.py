# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# 1. Gerar dados fictícios de vendas mensais (24 meses)
np.random.seed(42)

# Usando 'M' para fim de mês (mais compatível que 'ME')
datas = pd.date_range(start='2022-01-01', periods=24, freq='M')

# Criando componentes da série temporal
tendencia = np.linspace(100, 200, 24)  # Tendência de crescimento
sazonalidade = 20 * np.sin(np.linspace(0, 3 * np.pi, 24))  # Padrão sazonal
ruido = np.random.normal(0, 10, 24)  # Ruído aleatório

# Série final
vendas = tendencia + sazonalidade + ruido
df = pd.DataFrame({'Data': datas, 'Vendas': vendas})
df.set_index('Data', inplace=True)

# Exibir os primeiros dados (compatível em qualquer ambiente)
print(df.head())

# 2. Plotar gráfico inicial da série temporal
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Vendas'], marker='o', linestyle='-', color='b')
plt.title('Série Temporal de Vendas Mensais (Dados Brutos)')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.grid(True)
plt.show()

# 3. Calcular Média Móvel (janela de 3 meses)
df['Media_Movel'] = df['Vendas'].rolling(window=3).mean()

# Plotar comparação entre série original e suavizada
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Vendas'], label='Vendas Originais', alpha=0.5)
plt.plot(df.index, df['Media_Movel'], label='Média Móvel (3 meses)', color='red', linewidth=2)
plt.title('Suavização: Vendas Originais vs Média Móvel')
plt.legend()
plt.grid(True)
plt.show()

# 4. Decomposição da série temporal
# Usando período = 12 para capturar sazonalidade anual em dados mensais
decomposicao = seasonal_decompose(df['Vendas'], model='additive', period=12)

# Plotar os componentes da decomposição
fig = decomposicao.plot()
fig.set_size_inches(10, 8)
plt.show()
