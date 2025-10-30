import matplotlib.pyplot as plt
import numpy as np

# Criando os dados
x = np.linspace(0, 10, 100) # Cria um array de 100 valores é o que faz o o cógido, x=np.linspace(0,10,100)
print(x)
y1 = np.sin(x)
y2 = np.cos(x) # Calcula o cosseno de cada valor do array é o que faz o o cógido, y2 = np.cos(x)
print(y2)

# Gráfico de linha
plt.plot(x, y1)
plt.title('Gráfico de Linha')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Gráfico de dispersão
plt.figure()
plt.scatter(x, y2) # Cria um gráfico de dispersão é o que faz o o cógido, plt.scatter(x, y2)

plt.title('Gráfico de Dispersão')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Gráfico de barras
valores = [5, 10, 8, 3, 6]
rotulos = ['A', 'B', 'C', 'D', 'E']

plt.figure()
plt.bar(rotulos, valores)
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Subplots
fig, axs = plt.subplots(2, 1) # Cria uma figura com dois subgráficos é o que faz o o cógido, fig, axs = plt.subplots(2, 1)

axs[0].plot(x, y1)
axs[0].set_title('Gráfico de Linha')

axs[1].scatter(x, y2)
axs[1].set_title('Gráfico de Dispersão')

# Salvando o gráfico de barras
plt.savefig('grafico_barras.png')

# Exibindo todos os gráficos
plt.show()


