


dict_de_nomes_e_notas = {"Ana Silva": 8.5, "João Santos": 5.2, "Maria Oliveira": 2.9, "Pedro Souza": 10.0, "Lucas Pereira": 10.0}



dic_desafio = [{"nome": "Ana Silva", "nota": 8.5},
               {"nome": "João Santos", "nota": 5.2},
               {"nome": "Maria Oliveira", "nota": 2.9},
               {"nome": "Pedro Souza", "nota": 10.0},
               {"nome": "Lucas Pereira", "nota": 10.0}]



print(dict_de_nomes_e_notas["João Santos"])

print(dict_de_nomes_e_notas.items()) # Retorna uma lista de tuplas (chave, valor)
print(dict_de_nomes_e_notas.keys()) # Retorna uma lista com as chaves do dicionário
print(dict_de_nomes_e_notas.values()) # Retorna uma lista com os valores do dicionário


print(dic_desafio[0]["nota"])


n = 0
while n< len(dic_desafio): 
    print(dic_desafio[n])
    n += 1


for elemento in dic_desafio:
    print(elemento)


for n in range(5):
    print(n)



for n in range(2,7,2):
    print(n)
