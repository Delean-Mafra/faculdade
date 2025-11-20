print("Bem-vindo ao sistema de pedidos da Cafeteria!")

# Entrada: quantidade de itens
while True:
    try:
        n = int(input("Quantos itens o cliente vai pedir?\nR: "))
        if n <= 0:
            print("Digite um número maior que zero.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

total = 0

# Loop para registrar os itens
for i in range(n):
    nome = input(f"Digite o nome do item {i+1}: ")

    # Loop para garantir que o preço seja válido
    while True:
        try:
            preco = float(input(f"Digite o preço do item {i+1}: "))
            if preco < 0:
                print("O preço não pode ser negativo. Digite novamente.")
                continue
            total += preco
            break
        except ValueError:
            print("Entrada inválida. Você deve digitar apenas números para o preço do item.")

# Verificação de cadastro
while True:
    cadastrado = input("O cliente é cadastrado? (sim/não): ").strip().lower()
    if cadastrado in ["sim","s", "não", "nao","n"]:
        break
    else:
        print("Entrada inválida. Digite apenas 'sim' ou 'não'.")

# Aplicação do desconto
if cadastrado == "sim" or cadastrado == "s":
    desconto = total * 0.10
    total_com_desconto = total - desconto
    print(f"Valor total com desconto: R$ {total_com_desconto:.2f}")
else:
    print(f"Valor total sem desconto: R$ {total:.2f}")
