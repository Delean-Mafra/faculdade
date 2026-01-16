lista_numeros = [2, 3, 5, 8, 10]
numero = 5
inicio = 0
fim = len(lista_numeros) - 1
enc = False

while inicio <= fim and not enc:
    meio = (inicio + fim) // 2
    if lista_numeros[meio] == numero:
        enc = True
    elif numero < lista_numeros[meio]:
        fim = meio - 1
    else:
        inicio = meio + 1

if enc:
    print("O número", numero, "foi encontrado na lista")
else:
    print("O número", numero, "não foi encontrado na lista")
