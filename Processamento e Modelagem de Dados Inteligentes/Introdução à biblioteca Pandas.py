import pandas as pd

id = pd.Series([1234,5678,10111,12131,15555])
dados = {'nome': ['Ana','Bob','Ana','Tom','Bob'],
         'idade': [25,30,35,20,27]}

df = pd.DataFrame(dados, index=id)

df = df.reset_index(drop=True)

anadf = df[df.nome == 'Ana']         
print(anadf)

nome_idade = df[['nome','idade']]
print(nome_idade)

# Exemplo de agrupamento (mantém índice padrão)
df_prod = pd.DataFrame({
    'produto': ['A','B','A','C','B'],
    'preco_unit': [10, 20, 15, 30, 25]
})
media_por_produto = df_prod.groupby('produto')['preco_unit'].mean()
print(media_por_produto)
