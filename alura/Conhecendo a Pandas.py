from networkx import display
import pandas as pd
import numpy as np

# Gerar 50 linhas de dados aleatórios
num_rows = 50

# Nomes de produtos
product_names = [f'Produto {i+1}' for i in range(num_rows)]

# Categorias de produtos
categories = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros', 'Casa']
product_categories = np.random.choice(categories, size=num_rows)

# Preço do produto
product_prices = np.round(np.random.uniform(10.0, 500.0, size=num_rows), 2)

# Quantos itens do produto foram vendidos
items_sold = np.random.randint(1, 1000, size=num_rows)

# Avaliação do produto
product_ratings = np.round(np.random.uniform(1.0, 5.0, size=num_rows), 1)

# Criar o DataFrame
df = pd.DataFrame({
    'Nome do produto': product_names,
    'Categoria do produto': product_categories,
    'Preço do produto': product_prices,
    'Quantos itens do produto foram vendidos': items_sold,
    'Avaliação do produto': product_ratings
})

# # Exibir as primeiras 5 linhas do DataFrame
# print((df.head()))


# print(set(df['Categoria do produto'].unique() ))

# print(df['Categoria do produto'].unique())

# print(df['Nome do produto'])



print(df[(df['Categoria do produto'] == 'Eletrônicos') & (df['Preço do produto'] >= 350.0)])

print(df[df['Categoria do produto'] < 'Avaliação do produto'])

print(df.shape)

df_com_indice_produto = df.set_index('Nome do produto')
display(df_com_indice_produto.head())

df_produto = df[df['Categoria do produto'] < 'Avaliação do produto']

df_com_indice_produto = df_produto.set_index('Nome do produto')
(df_com_indice_produto.head())

print(df_com_indice_produto.loc["Produto 10"])



df = pd.read_csv("reviews.csv")

def classificar_sentimento(texto):
    # Aqui você chamaria o modelo LLM com o texto
    # Exemplo fictício:
    if "ótimo" in texto or "excelente" in texto:
        return "Positivo"
    elif "péssimo" in texto or "horrível" in texto:
        return "Negativo"
    else:
        return "Neutro"
df["sentimento"] = df["feedback"].apply(classificar_sentimento)
df.to_csv("reviews_classificados.csv", index=False)




df = pd.read_csv("/content/reviews.csv")

def classificar_sentimento(texto):
    if "ótimo" in texto or "excelente" in texto:
        return "Positivo"
    elif "péssimo" in texto or "horrível" in texto:
        return "Negativo"
    else:
        return "Neutro"

# aplica na coluna correta
df["sentimento"] = df["reviewText"].apply(classificar_sentimento)

# salva o resultado
df.to_csv("reviews_classificados.csv", index=False)

print(df.head())  # só para conferir as primeiras linhas


def classificar_sentimento(texto):
    texto = texto.lower()
    positivos = ["great", "excellent", "amazing", "works", "reliable", "good"]
    negativos = ["bad", "poor", "horrible", "terrible", "disappointed", "failed", "crap"]

    if any(p in texto for p in positivos):
        return "Positivo"
    elif any(n in texto for n in negativos):
        return "Negativo"
    else:
        return "Neutro"

df["sentimento"] = df["reviewText"].apply(classificar_sentimento)

print(df.head())

df_reviews = pd.read_csv("/content/reviews.csv")
df_reviews.head()
coluna_de_reviews = df_reviews["reviewText"]
coluna_de_reviews.head()

# !pip install groq

import os
from google.colab import userdata

os.environ["GROQ_API_KEY"] = userdata.get('GROQ_API_KEY')



from groq import Groq

client_groq = Groq()

completion = client_groq.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1, #0 - o menos criativo possível; 2 - o mais criativo possível
    max_completion_tokens=8192,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")



lista_de_analises_de_sentimentos = []
for review_numero, resenha in enumerate(coluna_de_reviews):
    resposta = client_groq.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
          {
            "role": "user",
            "content": f"""Você irá analisar a resenha que eu te mandarei abaixo, e retornar com uma análise de sentimento.
Você deve responder APENAS com uma das seguintes palavras: 'Positiva', 'Negativa' ou 'Neutra',
indicando o sentimento relativo àquela resenha específica. Exemplos:

'Eu adorei esse produto' -> Positiva
'Gostei, mas não é nada de especial' -> Neutra
'Odiei esse produto' -> Negativa


Segue a resenha a ser analisada: {resenha}
"""
          }
        ],
        temperature=1,
        max_completion_tokens=8192,
        stream=False # Changed to False because we expect a single response for .content
    )
    # Acessar o conteúdo da resposta corretamente
    sentimento_analisado = resposta.choices[0].message.content
    lista_de_analises_de_sentimentos.append(sentimento_analisado)
    print("Resenha", review_numero, ": '", resenha, "' -> Sentimento:", sentimento_analisado)

lista_de_analises_de_sentimentos

df_reviews["Anlises de sentimento(Cria nova coluna)"] = lista_de_analises_de_sentimentos
