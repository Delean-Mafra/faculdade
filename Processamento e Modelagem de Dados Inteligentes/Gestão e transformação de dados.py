import pandas as pd

def return_fruta_dataframe():
    df_frutas = pd.DataFrame({
        'fruta': ['maçã', 'banana', 'laranja', 'uva'],
        'preço': [1.50, 0.50, 2.20, 0.75],
        'quantidade': [100, 200, 50, 75]
    })
    print("df_frutas")
    print(df_frutas)
    print()
    selecao = df_frutas[['quantidade', 'fruta']]
    print("selecao = df_frutas[['quantidade', 'fruta']]")
    print(selecao)
    print()
    print("df_frutas.iloc[:2]  # primeiras duas linhas")
    print(df_frutas.iloc[:2])
    print()
    df_frutas_2 = df_frutas.iloc[0]
    print("df_frutas_2 = df_frutas.iloc[0]  # primeira linha como Series")
    print(df_frutas_2)

def return_pessoa_dataframe():
    dados_cadastro = {
        'nome': ['João', 'Maria', 'José', 'Ana', 'Pedro', 'Alan'],
        'idade': [20, 25, 38, 35, 40, 30],
        'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Campinas']
    }
    df_cadastro = pd.DataFrame(dados_cadastro)
    print("df_cadastro")
    print(df_cadastro)
    print()
    media_idade = df_cadastro['idade'].mean()
    print("media_idade =", media_idade)
    desvio_idade = df_cadastro['idade'].std()
    print("desvio_idade =", desvio_idade)
    soma_idades = df_cadastro['idade'].sum()
    print("soma_idades =", soma_idades)

    df = pd.DataFrame({
        'nome': ['João','Maria','José'],
        'idade': [20,25,30],
        'cidade': ['São Paulo','Rio de Janeiro','Belo Horizonte']
    })

    mapeamento = {
        'São Paulo': 'SP',
        'Rio de Janeiro': 'RJ'
    }

    df['cidade'] = df['cidade'].map(mapeamento).fillna(df['cidade'])
    print(df)

    # mudar o nome da coluna 'cidade' para 'estado'
    df = df.rename(columns={'cidade': 'estado'})

    # adciona uma nova coluna 'cidade' e mantem a coluna 'estado'
    df['cidade'] = ['São Paulo','Rio de Janeiro','Belo Horizonte']

    # GrupBy
    df_pessoa_mais_velha = df_cadastro.loc[df_cadastro.groupby('cidade')['idade'].idxmax()]
    print(df_pessoa_mais_velha)

    # add mais 3 pessoas com novos idades na cidade 'Rio de Janeiro'
    novas_pessoas = pd.DataFrame({
        'nome': ['Carlos', 'Fernanda', 'Lucas'],
        'idade': [28, 32, 22],
        'cidade': ['Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro']
    })
    df_cadastro = pd.concat([df_cadastro, novas_pessoas], ignore_index=True)
    print(df_cadastro)



# Geração de dados
def return_dados_dataframe():

    import random

    produtos = {'Arroz': 10.0, 'Feijão': 8.0, 'Macarrão': 5.0, 'Óleo': 7.0, 'Açúcar': 4.0}
    print(produtos)
    dados_vndas = {'Nome do Produto': [], 'Preço Unitário': [], 'Quantidade Vendida': [], 'Preço Total': []}

    for produto, preco in produtos.items():
        quantidade_vendida = random.randint(50, 100)
        preco_total = round(preco * quantidade_vendida, 2)
        
        dados_vndas['Nome do Produto'].append(produto)
        dados_vndas['Preço Unitário'].append(preco)
        dados_vndas['Quantidade Vendida'].append(quantidade_vendida)
        dados_vndas['Preço Total'].append(preco_total)
    df_vendas = pd.DataFrame(dados_vndas)
    print("\ndf_vendas")
    # Passa dados para csv
    df_vendas.to_csv('vendas.csv', index=False)
    print(df_vendas)





def return_pessoa_ou_fruta_dataframe(tipo):
    if tipo == '1':
        return_fruta_dataframe()
    elif tipo == '2':
        return_pessoa_dataframe()
    elif tipo == '3':
        return_dados_dataframe()
    else:
        print("Tipo inválido. Use '1' para fruta ou '2' para pessoa.")

if __name__ == '__main__':
    tipo = input("Digite '1' para dados de frutas, '2' para dados de pessoas ou '3' para dados de vendas: ").strip()
    return_pessoa_ou_fruta_dataframe(tipo)
