import numpy as np

ints = [1, 2, 3]
floats = [1.1, 2.2, 3.3]
booleans = [True, False, True]
strings = ["a", "b", "c"]
complex_numbers = [1 + 2j, 3 + 4j, 5 + 6j]

print("Valor no indíce 0:", strings[0]) 
print("Valor no indíce 1:", strings[1]) 
print("Valor no indíce 2:", strings[2]) 

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = {'a': 1, 'b': 2, 'c': 3}

primeiro_lista = lista[0]
primeiro_tupla = tupla[0]
primeiro_conjunto = next(iter(conjunto))
primeiro_dicionario = list(dicionario.values())[0]


# Criando uma lista de serviços realizados na oficina mecânica
servicos = ["Troca de óleo", "Alinhamento", "Balanceamento", "Revisão de freios"]

# Modificar um serviço
servicos[1] = "Alinhamento e balanceamento"  # Modifica o segundo serviço

# Remover um serviço
servicos.remove("Revisão de freios")         # Remove o serviço "Revisão de freios"
servico_removido = servicos.pop(2)           # Remove o serviço no índice 2 ("Balanceamento")

# Iterar sobre os serviços
for servico in servicos:
    print(servico)

# Verificar se um serviço existe
contem_oleo = "Troca de óleo" in servicos    # Verifica se "Troca de óleo" está na lista

# Obter o tamanho da lista de serviços
tamanho = len(servicos)                      # Número de serviços na lista

# Adicionar novos serviços
servicos.append("Troca de filtro de ar")     # Adiciona um novo serviço ao final da lista
servicos.insert(1, "Troca de pneus")         # Insere um serviço na posição 1

# Acessar serviços
primeiro_servico = servicos[0]               # Acessa o primeiro serviço
ultimo_servico = servicos[-1]                # Acessa o último serviço


# Ordenar a lista de serviços
servicos.sort()              # Ordena a lista em ordem alfabética
servicos.sort(reverse=True)  # Ordena a lista em ordem alfabética inversa

# Reverter a lista de serviços
servicos.reverse()           # Reverte a ordem dos serviços na lista

# Copiar a lista de serviços
copia_servicos = servicos.copy()  # Cria uma cópia da lista

matriz = [['' for _ in range(3)] for _ in range(3)]  # Declaração e alocação de memória


# Associação de valores na matriz
matriz[0][0] = 'a'
matriz[0][1] = 'b'
matriz[0][2] = 'c'
matriz[1][0] = 'd'
matriz[1][1] = 'e'
matriz[1][2] = 'f'
matriz[2][0] = 'g'
matriz[2][1] = 'h'
matriz[2][2] = 'i'


# Declaração e inicialização da matriz bidimensional de strings
matriz = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]

# Acessando e imprimindo um elemento específico diretamente
print("O elemento na posição [1][2] é:", matriz[1][2])


# Matrizes representando dados de motocicletas
motocicletas = np.array([
    ["Cruiser", "Harley-Davidson", "Street 750"],
    ["Sport", "Yamaha", "YZF-R3"]
]).reshape(2, 3)

# Acessando um valor
print("Modelo da Harley-Davidson:", motocicletas[0, 2])  # Street 750
Modelo_da_Harley_Davidson = "YZF-R3"

# Adicionando uma nova linha
motocicletas = np.vstack((motocicletas, ["Adventure", "BMW", "R 1250 GS"]))
print("Após adicionar uma nova linha:\n", motocicletas)

# Editando um valor
motocicletas[1, 2] = "MT-07"  # Editing Yamaha's model in the second row
print("Após editar o modelo da Yamaha:\n", motocicletas)

# Removendo uma linha
motocicletas = np.delete(motocicletas, 0, axis=0)
print("Após remover a primeira linha:\n", motocicletas)


# Dicionário aninhado com informações sobre motocicletas
motocicletas = {
    "Esportiva": {
        "Yamaha": [
            "Yamaha YZF-R1 - Azul",
            "Yamaha YZF-R6 - Vermelha"
        ],
        "Honda": [
            "Honda CBR1000RR - Preta",
            "Honda CBR600RR - Branca"
        ]
    },
    "Adventure": {
        "BMW": [
            "BMW R 1250 GS - Azul",
            "BMW F 850 GS - Amarela"
        ],
        "KTM": [
            "KTM 1290 Super Adventure - Laranja",
            "KTM 790 Adventure - Branca"
        ]
    }
}

# Acessando um valor específico no dicionário aninhado
print(motocicletas["Esportiva"]["Honda"][0])

carros = {
    "Esportivo": {
        "Ferrari": {
            "488": {
                "Pista": "Ferrari 488 Pista Vermelho (Esportivo)",
                "Spider": "Ferrari 488 Spider Amarelo (Esportivo)"
            },
            "F8": {
                "Tributo": "Ferrari F8 Tributo Azul (Esportivo)",
                "Spider": "Ferrari F8 Spider Preto (Esportivo)"
            }
        },
        "Lamborghini": {
            "Huracan": {
                "Evo": "Lamborghini Huracan Evo Verde (Esportivo)",
                "Performante": "Lamborghini Huracan Performante Laranja (Esportivo)"
            },
            "Aventador": {
                "SVJ": "Lamborghini Aventador SVJ Branco (Esportivo)",
                "S": "Lamborghini Aventador S Cinza (Esportivo)"
            }
        }
    },
    "SUV": {
        "BMW": {
            "X5": {
                "M": "BMW X5 M Preto (SUV)",
                "xDrive40i": "BMW X5 xDrive40i Azul (SUV)"
            },
            "X6": {
                "M": "BMW X6 M Vermelho (SUV)",
                "xDrive40i": "BMW X6 xDrive40i Branco (SUV)"
            }
        },
        "Audi": {
            "Q7": {
                "Premium": "Audi Q7 Premium Prata (SUV)",
                "Prestige": "Audi Q7 Prestige Preto (SUV)"
            },
            "Q8": {
                "Premium": "Audi Q8 Premium Azul (SUV)",
                "Prestige": "Audi Q8 Prestige Vermelho (SUV)"
            }
        }
    }
}
# Acessando e imprimindo um elemento específico
print(carros["Esportivo"]["Ferrari"]["488"]["Pista"])


# Primeiro bloco
lst = [1, 2, 3, 4, 5]
for element in lst:
    print(element)

# Segundo bloco
st = {1, 2, 3, 4, 5}
for element in st:
    print(element)

# Terceiro bloco
dct = {'a': 1, 'b': 2, 'c': 3}
for key, value in dct.items():
    print(f"Key: {key}, Value: {value}")


lst = ['a', 'b', 'c']
for index, element in enumerate(lst):
    print(f"Index: {index}, Element: {element}")


names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")


lst = [1, 2, 3]
it = iter(lst)
print(next(it))  # Saída: 1
print(next(it))  # Saída: 2

lst = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, lst))
print(squared)  # Saída: [1, 4, 9, 16]


lst = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, lst))
print(even)  # Saída: [2, 4]


# Criando um array 2D
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Varredura em um array 2D
for i in range(array_2d.shape[0]):
    for j in range(array_2d.shape[1]):
        print(f'Elemento em ({i}, {j}) = {array_2d[i, j]}')

# Criando um array 3D
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Varredura em um array 3D
for i in range(array_3d.shape[0]):
    for j in range(array_3d.shape[1]):
        for k in range(array_3d.shape[2]):
            print(f'Elemento em ({i}, {j}, {k}) = {array_3d[i, j, k]}')
