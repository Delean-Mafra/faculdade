# Neste projeto prático, vamos criar um modelo de dados para uma loja virtual, considerando os seguintes requisitos:

# A loja vende produtos de diferentes categorias, como eletrônicos, roupas, acessórios, etc.

# Cada produto tem um nome, uma descrição, um preço, uma imagem e uma categoria.

# Cada categoria tem um nome e uma descrição.

# Os clientes da loja podem criar uma conta para fazer compras, e cada conta tem um nome, um endereço de e-mail e uma senha.

# Os clientes podem adicionar produtos ao carrinho de compras e finalizar a compra.

# Cada compra tem um número de identificação, uma data e uma lista de produtos comprados.

# Para cada produto comprado, registra-se a quantidade e o preço unitário na data da compra.

# Com base nesses requisitos, podemos criar um modelo de dados com as seguintes tabelas:

# Produtos: ID, nome, descrição, preço, imagem, ID_categoria

# Categorias: ID, nome, descrição

# Clientes: ID, nome, e-mail, senha

# Compras: ID, data, ID_cliente

# Produtos_comprados: ID_compra, ID_produto, quantidade, preço_unitário


sql_creat_table = """

--sql
CREATE TABLE Clientes (
  ID INT PRIMARY KEY,
  nome VARCHAR(255),
  email VARCHAR(255),
  senha VARCHAR(255)
)

CREATE TABLE Compras (
  ID INT PRIMARY KEY,
  dc DATE,
  ID_cliente INT,
  FOREIGN KEY (ID_cliente) REFERENCES Clientes(ID)
)

CREATE TABLE Produtos_comprados (
  ID_compra INT,
  ID_produto INT,
  quantidade INT,
  preco_unitario DECIMAL(10, 2),
  FOREIGN KEY (ID_compra) REFERENCES Compras(ID),
  FOREIGN KEY (ID_produto) REFERENCES Produtos(ID)
);

"""

import datetime

import pandas as pd
import sqlite3
import numpy as np

dados = pd.DataFrame({
    'data_venda': pd.date_range('2022-01-01', periods=365),
    'vendedor': np.random.choice(['João', 'Maria', 'Pedro', 'Ana'], size=365),
    'produto': np.random.choice(['Camiseta', 'Calça', 'Tênis','Boné'], size=365),
    'preco': np.random.normal(loc=100, scale=20, size=365),
    'quantidade': np.random.randint(1, 10, size=365)
})

print(dados.head())

print(dados.describe())


dados['data_venda'] = pd.to_datetime(dados['data_venda'],format='%d-%m-%Y')

print(dados.isnull().sum())


venda_mes = dados.groupby(pd.Grouper(key='data_venda', freq='M')).sum()['preco']

print(venda_mes)