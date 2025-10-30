import numpy as np

# Criando arrays
arr = np.arange(1, 11)
matriz = np.arange(1, 13).reshape(3, 4)

# Exibindo arrays
print("Array 'arr':")
print(arr)

print("\nMatriz 'matriz':")
print(matriz)

# Operações com arrays
arr_slice = arr[2:6]
arr_resultado = arr * 2
soma_matriz = np.sum(matriz)
media_arr = np.mean(arr)
matriz_transposta = np.transpose(matriz)
arr_concatenado = np.concatenate((arr, arr_slice))

# Exibindo resultados
print("\nArray 'arr_slice':")
print(arr_slice)

print("\nArray 'arr_resultado':")
print(arr_resultado)

print("\nSoma da matriz 'matriz':", soma_matriz)
print("\nMédia do array 'arr':", media_arr)

print("\nMatriz transposta:")
print(matriz_transposta)

print("\nArray concatenado 'arr_concatenado':", arr_concatenado)

#______________é o que faz o o cógido, arr = np.arange(1, 11)
# R: Array com números de 1 a 10 é o que faz o o cógido, arr = np.arange(1, 11)


arr = np.arange(1, 11)


print(f"{arr} é o que faz o o cógido, arr = np.arange(1, 11)")


# ______________é o que faz o o cógido, matriz = np.arange(1, 13).reshape(3, 4)
# R: Matriz bidimensional é o que faz o o cógido, matriz = np.arange(1, 13).reshape(3, 4)


matriz = np.arange(1, 13).reshape(3, 4)

print(f"{matriz} é o que faz o o cógido, matriz = np.arange(1, 13).reshape(3, 4)")


# ______________é o que faz o código, print("Array 'arr':")

# R: Imprime o array 'arr':" é o que faz o código, print("Array 'arr':")



print("Array 'arr':","""é o que faz o código, print("Array 'arr':")""")



# ____________é o que faz o código, print("\nMatriz 'matriz':")

# R: Imprime a Matriz 'matriz' é o que faz o código, print("\nMatriz 'matriz':")


print("\nMatriz 'matriz':",r""" é o que faz o código, print("\nMatriz 'matriz':")""")


