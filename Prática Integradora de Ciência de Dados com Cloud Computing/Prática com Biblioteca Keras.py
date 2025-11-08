# Importando as bibliotecas necessárias
import numpy as np
from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import plot_model
from keras.optimizers import Adam, SGD, RMSprop

# Atividade Prática 14 — Prática com Biblioteca Keras

# Título da Prática: Classificação de Dígitos MNIST com Keras
# Objetivos: Construir um modelo de rede neural para prever o preço de casas com base em suas características. Usaremos o conjunto de dados de preços de casas da biblioteca keras.datasets para simplificar.
# Materiais, Métodos e Ferramentas: Para realizar esta prática utilizaremos o Colab.

# Atividade Prática
# Nesta atividade, você criará um modelo de rede neural usando a biblioteca Keras para prever preços de casas com base em suas características.

# Carregando os dados de treinamento e teste do Boston Housing
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

# Calcula a média e o desvio padrão dos dados de treinamento
mean = x_train.mean(axis=0)
std = x_train.std(axis=0)

# Normaliza os dados de treinamento e teste
x_train -= mean
x_train /= std
x_test -= mean
x_test /= std

# Criação do modelo sequencial
model = Sequential()

# Adiciona uma camada densa (fully connected) com 64 neurônios e função de ativação ReLU
model.add(Dense(64, activation='relu', input_shape=(x_train.shape[1],)))

# Adiciona outra camada densa com 64 neurônios e função de ativação ReLU
model.add(Dense(64, activation='relu'))

# Adiciona a camada de saída com 1 neurônio (para regressão)
model.add(Dense(1))

# Compilação do modelo
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Treinamento do modelo
model.fit(x_train, y_train, epochs=100, batch_size=1, verbose=1)

# Avaliação do modelo nos dados de teste
loss, mae = model.evaluate(x_test, y_test)

# Impressão do erro absoluto médio (MAE)
print(f"Mean Absolute Error: {mae:.2f}")



# Aula 2 - Representação gráfica usando Keras

# Modelo
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(10, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.add(Dense(30, activation='relu'))

# Compilação
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Visualização
plot_model(model, to_file="modelo.png", show_shapes=True, show_layer_names=True)



# Aula 4 - Trabalhando com diferentes funções de ativação e otimizadores


# Gerando dados aleatórios
np.random.seed(42)
x = np.random.rand(100, 1)
y = 2 + 3 * np.random.rand(100, 1)

# Criando o modelo
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))
model.add(Dense(1, activation='linear'))

# Definindo o otimizador
optimizer = RMSprop(learning_rate=0.1)

# Compilando o modelo
model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mse'])

model.fit(x, y, epochs=50, batch_size=10, verbose=2)

predictions = model.predict(x)

print(predictions)
