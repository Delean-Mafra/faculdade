import pandas as pd
import sqlite3

dados = pd.read_csv('dados_pets.csv')

# Comentando a parte do SQLite pois não há banco de dados configurado
#conn = sqlite3.connect('banco_de_dados.db')
#query = "SELECT * FROM tabela"
#df_dados = pd.read_sql(query, conn)

# Usando os dados do CSV diretamente
df_dados = dados

# Comentando a leitura do JSON pois o arquivo não existe
#data = pd.read_json('dados.json')

filtro_query = df_dados.query("especie == 'cachorro' and cor == 'preto'")
print("\nFiltro - Cachorros pretos:")
print(filtro_query)

df_dados['idade_meses'] = df_dados['idade'] * 12
print(df_dados)

# Salvando o DataFrame atualizado de volta no CSV
df_dados.to_csv('dados_pets.csv', index=False)
print("\n✅ Arquivo 'dados_pets.csv' atualizado com a coluna 'idade_meses'!")

estat_idade = df_dados['idade'].describe()
print(estat_idade)

estat_idade = df_dados['idade_meses'].describe()
print(estat_idade)

estat_idade = df_dados['especie'].describe()
print(estat_idade)

media_idades = df_dados['idade'].mean()
print(media_idades)

midiana_idades = df_dados['idade'].median()
print(midiana_idades)

soma_idades = df_dados['idade'].sum()
print(soma_idades)

df_novos = pd.DataFrame({
    'nome_do_pet':['pet1','pet2'],
    'especie':['cachorro','cachoro'],
    'cor':['azul','verde',],
    'idade':[10,20]
})

df_concat = (pd.concat([df_dados, df_novos], ignore_index=True))
print(df_concat)
df_outro= pd.DataFrame({'nome_pet':['pet3','pet4'],
                        'tutor':['luiz','alea..']})
print(df_outro)

df_merger = pd.merge(df_concat, df_outro, left_on='nome_do_pet', right_on='nome_pet', how='left')
print(df_merger)
