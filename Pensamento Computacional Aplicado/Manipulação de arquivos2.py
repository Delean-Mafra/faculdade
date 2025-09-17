import csv

# Dados iniciais a serem escritos no arquivo CSV
dados_iniciais = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', 30, 'São Paulo'],
    ['Maria', 25, 'Rio de Janeiro'],
    ['Pedro', 35, 'Belo Horizonte']
]

# Escrever dados iniciais no arquivo CSV
with open('dados.csv', 'w', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerows(dados_iniciais)

# Ler e exibir o conteúdo do arquivo CSV
with open('dados.csv', 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    print('Conteúdo inicial do arquivo CSV:')
    for linha in leitor_csv:
        print(linha)

# Modificar os dados (adicionar uma nova linha)
nova_linha = ['Ana', 28, 'Curitiba']
with open('dados.csv', 'a', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(nova_linha)

# Ler e exibir o conteúdo atualizado do arquivo CSV
with open('dados.csv', 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    print('Conteúdo atualizado do arquivo CSV:')
    for linha in leitor_csv:
        print(linha)
