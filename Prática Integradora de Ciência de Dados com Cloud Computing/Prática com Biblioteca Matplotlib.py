import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# dados
categorias = ['Cat A', 'Cat B', 'Cat C', 'Cat D']
valores = [25, 40,30, 90]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.bar(categorias, valores, zs=0, zdir='y', color=['skyblue','lightgreen','lightcoral','lightsalmon'],
       edgecolor='blue', linewidth=5)


ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(False)

plt.xticks(rotation=45, ha='right')

ax.view_init(elev=10, azim=15)

ax.set_xlabel('eixo X')
ax.set_ylabel('eixo Y')
ax.set_zlabel('eixo Z')

ax.set_title("Grafico 3D")


# plt.savefig('graf.png', format='png', dpi=300, bbox_inches='tight')

plt.show()



# --- Plots 2D: seno e cosseno em uma figura separada ---
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Usar subplots de forma consistente (1 linha x 3 colunas)
fig2, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, y1, label='seno', color='tab:blue')
axes[0].set_title('Graf Seno')
axes[0].set_xlabel('x')
axes[0].set_ylabel('seno(x)')
axes[0].legend()

axes[1].plot(x, y2, label='cos', color='tab:orange')
axes[1].set_title('Graf Cos')
axes[1].set_xlabel('x')
axes[1].set_ylabel('cos(x)')
axes[1].legend()

# Comparar seno e cosseno no mesmo eixo
axes[2].plot(x, y1, label='seno', color='tab:green')
axes[2].plot(x, y2, label='cos', color='tab:red', linestyle='--')
axes[2].set_title('Seno vs Cos')
axes[2].set_xlabel('x')
axes[2].legend()

plt.tight_layout()
plt.show()
