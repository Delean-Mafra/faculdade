# Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical

# Carregando o conjunto de dados MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Convertendo o conjunto de dados para o tipo float32 e normalizando os valores
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Convertendo os rótulos para one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Construindo o modelo da rede neural
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))           # Achatando a imagem 28x28 em um vetor
model.add(Dense(128, activation='relu'))           # Camada oculta com 128 neurônios e função de ativação ReLU
model.add(Dense(10, activation='softmax'))         # Camada de saída com 10 neurônios (um para cada dígito)

# Compilando o modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Treinando o modelo
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Avaliando o modelo
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Acurácia no conjunto de teste:", test_accuracy)
