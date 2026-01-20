# Simula tratativas de erros exeption e try/except em Python

def inoutar_idade():
    while True:
        try:
            idade = int(input("Por favor, insira sua idade: "))
            return idade
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número inteiro para a idade.")



age = inoutar_idade()
try:    
    print("Minha idade é " + age + "anos")
except TypeError:
    print("Erro: Não é possível concatenar string com inteiro. Converta o inteiro para string.")
    print("Minha idade é " ,age, " anos")
except TypeError:
    print("Erro: Não é possível concatenar string com inteiro. Converta o inteiro para string.")




lista = [10, 20, 30, 40, 50]

try:
    print(lista[10])
except IndexError:
    print("Erro: Índice inválido. A lista possui apenas", len(lista), "elementos (índices de 0 a", len(lista)-1, ")")


def calcular_media(a,b,c):
    media = (a + b + c) / 3  # Corrigido: precisa dos parênteses
    return media


try:
    nums = []
    for i in range(5):
        num = int(input(f"Digite o {i+1}º número: "))
        nums.append(num)
    results = calcular_media(nums[0], nums[1], nums[2])  # Passa os 3 primeiros elementos separadamente
    print(f"A média dos 3 primeiros números é: {results}")
except NameError:
    print('Nome da função ou variavel não foi decarada')
except TypeError as e:
    print(f'Erro de tipo: {e}')


