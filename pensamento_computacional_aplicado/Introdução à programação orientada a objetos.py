

texto = "teste"
numero = 10
print(texto)
print(numero)
texto = "5"


texto = "10"

print(numero)


try:
    print(texto + numero)
except TypeError:
    try:
        texto = int(texto)
        print(texto + numero)
    except ValueError:
        print("Não é possível converter texto para número")


nome = "Douglas"

sobrenome = "Silva"

nome_completo = nome + " " + sobrenome
print(nome_completo)

nome2 = "João"

nome3 = "João"


print(nome3 == nome2)


# Aula Entrada de dados


nome = input("Digite seu nome: ")


    
with open ('Vetor/teste.txt', 'w') as arquivo:
    arquivo.write("Esta é a aula saida de dados")

with open ('Vetor/teste.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open ('Vetor/teste.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Este é um comentário de uma linha
x = 5  # Aqui estamos atribuindo o valor 5 à

# Este é um comentário de uma linha
x = 5  # Aqui estamos atribuindo o valor 5 à variável x

"""
Este é um comentário de múltiplas linhas.
Podemos usar quantas linhas quisermos aqui.
"""

def funcao_exemplo():
    """Esta função faz algo muito importante."""
    # Corpo da
    
# Exemplo de soma de três números
numero1 = 1
numero2 = 2
numero3 = 3
soma = numero1 + numero2 + numero3
print(soma)
