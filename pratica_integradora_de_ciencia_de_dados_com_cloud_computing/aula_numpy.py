import numpy as np
print(np.__version__)

a = np.array([1,2,3])
b = np.array([4,5,6])

# operações

soma = a + b 
conta = a - b
divisao = a / b

print(soma)
print(conta)
print(divisao)
print("Soma: ", soma, "qwert")



matrix = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(matrix)


elemento = matrix[0,1]


matrix[1,0] - 200
print(matrix)


print(matrix.shape)  # linhas e colunas
print("numero de elementos: ", matrix.size)  # numero de elementos


arr = np.array([1,2,3,4,5,6,7,8,9])

print("O array é: ", arr)
print("O primeiro elemento é: ", arr[0])
print("O ultimo elemento é: ", arr[-1]) # use arr[-1] para o ultimo elemento

# Slicing
subset = arr[2:5]  # elementos do indice 2 ao 4
print(subset)

arr_2 = np.array([0,0,7,9,5,0,0,0,0])

print("O array é: ", arr_2)
print("O primeiro elemento é: ", arr_2[0])
print("O ultimo elemento é: ", arr_2[-1]) # ultimo elemento com arr_2[-1]

# Slicing
subset_2 = arr_2[1:6]  # elementos do indice 1 ao 5
print(subset_2)

# alterar valores com slicing

arr_2[1:6] = 10,11,12,13,14
print("array com novos valores: ", arr_2)
print("array com novos valores: ", arr_2)




arr = np.arange(1, 11)
print(arr) # array de 1 a 10 - [ 1  2  3  4  5  6  7  8  9 10]

print("Array 'arr':")

print("\nMatriz 'matriz':")
