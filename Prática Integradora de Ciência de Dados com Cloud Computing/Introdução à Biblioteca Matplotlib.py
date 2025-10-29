# import matplotlib as mat
# print(mat.__version__)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

plt.plot(x, y)

plt.title('Gráfico 1')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.show()

categoria = ['cat A', 'cat B', 'cat C', 'cat D']
valores = [25, 30, 90, 45]  # Adicionado o 4º valor para corresponder às 4 categorias

plt.plot(categoria, valores)
plt.bar(categoria, valores, color=['red','blue','green','yellow'])

plt.xlabel('Categorias', fontsize=20)
plt.ylabel('Valores', fontsize=25, color='red')
plt.title('Barras')
plt.legend(['legenda'], loc='upper left')
for i, valor in enumerate(valores):
    plt.text(i, valor + 1, str(valor), ha='center')

plt.annotate("IMPORTANTE", xy=(2,15), arrowprops=dict(facecolor='black'), fontsize=5,ha='center')
plt.yscale('linear')

plt.tight_layout()



plt.show()
