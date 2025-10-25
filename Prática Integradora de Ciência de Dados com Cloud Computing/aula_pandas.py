import pandas as pd

print(pd.__version__)


dados_pets = {
    'nome_do_pet':['kitara','Raku','Beta'],
    'especie':['cachorro','hamister','peixe'],
    'cor':['preto','amarelo','azul'],
    'idade':['5','3','2']
}

# criando o data dataframe

df = pd.DataFrame(dados_pets)

# salvar os dados

df.to_csv('dados_pets_csv')



try:
    df_existente = pd.read_csv('dados_pets.csv')
except FileNotFoundError:
    df_existente = pd.DataFrame()

# Lista para armazenar os dados
dados_pets = []

# Pedir ao usuário para inserir dados
while True:
    nome_do_pet = input("Digite o nome do pet (ou digite 'sair' para encerrar): ")
    
    if nome_do_pet.lower() == 'sair':
        break
    
    especie = input("Digite a espécie do pet: ")
    cor = input("Digite a cor do pet: ")
    idade = int(input("Informe a idade do pet: "))
    
    # Adicionar os dados à lista
    dados_pets.append({
        'nome_do_pet': nome_do_pet,
        'especie': especie,
        'cor': cor,
        'idade': idade
    })

# Criar DataFrame com os novos dados
df_novos = pd.DataFrame(dados_pets)

# Concatenar dados existentes e novos dados
df_final = pd.concat([df_existente, df_novos], ignore_index=True)

# Salvar DataFrame em um arquivo CSV na raiz
df_final.to_csv('dados_pets.csv', index=False)

# Mostrar o DataFrame final
df_final


dados = pd.read_csv('dados_pets.csv')

print(dados)

linha_1 = dados.loc[0]
print(linha_1)


linha_1 = dados.loc[0]
print(linha_1)

aoutra_linha = dados.iloc[0:3]

outra_linha = dados.iloc[0:1]

print(outra_linha)


dados_com_filtro = dados[dados['idade']>2]
dados_com_filtro

nome_coluna = dados['especie']
print(nome_coluna)

coluna_idade = dados.loc[:,'idade']

print(coluna_idade)

colunas = dados.iloc[0:4]
print(colunas)
