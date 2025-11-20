Hamburguer = 12.00
Batata_frita = 7.00
Refrigerante = 5.00

qnt_Hamburguer = int(input("Quantos hambúrgueres você deseja? R: ")) 
qnt_Batata_frita = int(input("Quantas batatas fritas você deseja? R: "))
qnt_Refrigerante = int(input("Quantos refrigerantes você deseja? R: "))

total = (qnt_Hamburguer * Hamburguer) + (qnt_Batata_frita * Batata_frita) + (qnt_Refrigerante * Refrigerante)

print("O total do pedido é: R$", total)
