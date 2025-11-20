"""
Você está desenvolvendo um sistema para uma empresa de delivery. O valor da taxa de entrega depende da distância até o cliente e se o pedido foi feito em um dia de chuva.

As regras são:

Para entregas até 5 km, a taxa é R$ 5,00.
Entre 5 e 10 km, a taxa é R$ 8,00.
Acima de 10 km, a taxa é R$ 10,00.
Se estiver chovendo, acrescenta R$ 2,00 à taxa padrão.
O desafio desta atividade é criar um algoritmo em linguagem natural que informe o valor final da entrega.

Para entender melhor como elaborar uma solução para esse desafio, clique na Opinião da Pessoa Instrutora.

"""
def distancia():
    try:
        km = float(input('Informe a distancia da entrega em km: '))
        if km < 0:
            print('A distancia não pode ser negativa')
            return distancia()
        return km
    except ValueError:
        print('Informe uma distancia valida')
        return distancia()
km = distancia()
def chuva():
    try:
        esta_chovendo = input("Esta chovendo? (s/n): ").strip().lower()
        if esta_chovendo == 's':
            esta_chovendo = True
            return esta_chovendo
        elif esta_chovendo == 'n':
            esta_chovendo = False
            return esta_chovendo
        else:
            print('Informe "s" para "Sim" ou "n" para "Não"')    
            return chuva()
    except ValueError:
        print('Informe se esta chovendo')
        return chuva()
esta_chovendo = chuva()
if not esta_chovendo:
    taxa = 0
else:
    taxa = 2

def obter_valor():
    try:
        if km <= 5:
            valor = 5+taxa
            return valor
        elif km > 5 and km < 10:
            valor = 8+taxa
            return valor
        elif km > 10:
            valor = 10+taxa
            return valor
    except ValueError:
        erro = input('Algo deu errado, seja tentar novamente? (s/n): ')
        if erro == 's':
            return obter_valor()
        else:
            print('Encerrando o programa.')
            return
    except ValueError:
            print('Encerrando o programa.')
            return
valor_final = round(float(obter_valor()), 2)
print(f'O valor final da entrega é R${valor_final:.2f}')








































# def receber_idade():
#     # Função para receber a idade do usuário com tratamento de erro
#     try:
#         idade = int(input("Digite sua idade: "))
#         return idade
#     except ValueError:
#         print("Por favor, insira um número válido para a idade.")
#         return receber_idade()
# # Recebe a idade do usuário
# idade = receber_idade()
# def verifica_estudante():
#     # Função para verificar se o usuário é estudante com tratamento de erro
#     try:
#         estudante = input("Você é estudante? (s/n): ").strip().lower()
#         if estudante == 's':
#             return True
#         else:
#             return False
#     except ValueError:
#         print("Por favor, um valor valido.")
#         return verifica_estudante()
# # Verifica se o usuário é estudante
# estudante = verifica_estudante()


# preco_total = 40


# if idade < 18 or estudante:
#     preco = preco_total / 2
#     print('Meia-enrada aplicada')
# else:
#     preco = preco_total

# print('Valor a pagar: R$', preco)
