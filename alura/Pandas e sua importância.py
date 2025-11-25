# import pandas as pd

# df = pd.read_csv("meu_csv.csv")  # Substitua pelo caminho do seu arquivo CSV

# # Exibindo as primeiras linhas do DataFrame
# print(df.head())

# print(df.tail())  # Exibindo as últimas linhas do DataFrame



import csv
import pandas as pd
import time
import os

# --- PASSO 1: Criar arquivo .txt a partir de uma lista ---
lista_de_perguntas = [
    "Qual é a estrutura básica de um DataFrame no Pandas?",
    "Como carregar dados de um arquivo CSV usando Pandas?",
    "Como exibir as primeiras e últimas linhas de um DataFrame?",
    "Como calcular estatísticas descritivas com Pandas?",
    "Como filtrar dados em um DataFrame?",
    "Como lidar com valores ausentes em um DataFrame?",
    "Como agrupar dados em um DataFrame?",
    "Como mesclar dois DataFrames?",
    "Como salvar um DataFrame em um arquivo CSV?",
    "Quais são algumas das principais funcionalidades do Pandas?"
]
nome_arquivo_txt = "perguntas.txt"

# Escreve as perguntas no arquivo txt
with open(nome_arquivo_txt, "w", encoding="utf-8") as arquivo:
    for pergunta in lista_de_perguntas:
        arquivo.write(pergunta + "\n")

print(f"Passo 1 concluído: Arquivo '{nome_arquivo_txt}' criado.")


# --- PASSO 2: Ler as perguntas do arquivo .txt para uma lista ---
lista_perguntas_lidas = []

if os.path.exists(nome_arquivo_txt):
    with open(nome_arquivo_txt, "r", encoding="utf-8") as arquivo:
        # Lê as linhas e remove o caractere de nova linha (\n) do final
        lista_perguntas_lidas = [linha.strip() for linha in arquivo.readlines()]
    print(f"Passo 2 concluído: {len(lista_perguntas_lidas)} perguntas carregadas.")
else:
    print(f"Erro: O arquivo {nome_arquivo_txt} não foi encontrado.")


# --- PASSO 3: Obter respostas de um LLM (Simulação) ---
def consultar_llm(pergunta):
    """
    Função que simula uma chamada a um LLM.
    Num cenário real, você usaria bibliotecas como `openai` ou `google-generativeai`.
    """
    # Simulação de tempo de processamento
    time.sleep(0.2) 
    
    # Respostas baseadas em palavras-chave simples para o exemplo
    pergunta_lower = pergunta.lower()
    if "estrutura" in pergunta_lower:
        return "Um DataFrame é uma estrutura tabular bidimensional, mutável e com eixos rotulados (linhas e colunas)."
    elif "carregar" in pergunta_lower:
        return "Use a função `pd.read_csv('arquivo.csv')`."
    elif "exibir" in pergunta_lower:
        return "Use `.head()` para as primeiras linhas e `.tail()` para as últimas."
    elif "estatísticas" in pergunta_lower:
        return "O método `.describe()` fornece um resumo estatístico das colunas numéricas."
    elif "filtrar" in pergunta_lower:
        return "Você pode filtrar usando indexação booleana, ex: `df[df['coluna'] > 10]`."
    elif "ausentes" in pergunta_lower:
        return "Use `.dropna()` para remover ou `.fillna()` para preencher valores nulos."
    elif "agrupar" in pergunta_lower:
        return "O método `.groupby('coluna')` permite agrupar dados para aplicar funções de agregação."
    elif "mesclar" in pergunta_lower:
        return "As funções `pd.merge()` ou `.join()` são usadas para combinar DataFrames."
    elif "salvar" in pergunta_lower:
        return "Use o método `.to_csv('arquivo.csv', index=False)`."
    elif "funcionalidades" in pergunta_lower:
        return "Manipulação de dados, limpeza, agregação, visualização e integração com SQL/CSV."
    else:
        return "Resposta gerada pelo modelo de IA simulado."

dados_para_salvar = []

print("Consultando LLM (simulado)...")
for pergunta in lista_perguntas_lidas:
    resposta = consultar_llm(pergunta)
    dados_para_salvar.append([pergunta, resposta])

print("Passo 3 concluído: Respostas geradas.")


# --- PASSO 4: Salvar os resultados em um novo arquivo .csv ---
nome_arquivo_csv = "resultado_llm.csv"

with open(nome_arquivo_csv, "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    # Escreve o cabeçalho
    escritor.writerow(["Pergunta", "Resposta"])
    # Escreve os dados
    escritor.writerows(dados_para_salvar)

print(f"Passo 4 concluído: Arquivo '{nome_arquivo_csv}' salvo.")


# --- PASSO 5: Ler o arquivo .csv usando Pandas ---
print("\n--- Conteúdo do DataFrame (Passo 5) ---")
if os.path.exists(nome_arquivo_csv):
    df = pd.read_csv(nome_arquivo_csv)
    # Configuração para exibir o texto completo das colunas
    pd.set_option('display.max_colwidth', None)
    print(df)
else:
    print(f"Erro: O arquivo {nome_arquivo_csv} não foi encontrado.")




lista_de_perguntas = [
    "Qual é a estrutura básica de um DataFrame no Pandas?",
    "Como carregar dados de um arquivo CSV usando Pandas?",
    "Como exibir as primeiras e últimas linhas de um DataFrame?",
    "Como calcular estatísticas descritivas com Pandas?",
    "Como filtrar dados em um DataFrame?",
    "Como lidar com valores ausentes em um DataFrame?",
    "Como agrupar dados em um DataFrame?",
    "Como mesclar dois DataFrames?",
    "Como salvar um DataFrame em um arquivo CSV?",
    "Quais são algumas das principais funcionalidades do Pandas?"
]


import csv
import pandas as pd
import time
import os



with open('perguntas.txt', 'w', encoding="utf-8") as arquivo:
    for pergunta in lista_de_perguntas:
        arquivo.write(pergunta + '\n')


lista_desfio = []

with open('perguntas.txt', 'r', encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_desfio.append(linha.strip())
print(lista_desfio)





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






prompt = input('Digite a sua pergunta: ')

chat_history = []

while prompt != 'sair':
  chat_history.append({"role": "user", "content": prompt})

  completion = client_groq.chat.completions.create(
      model="openai/gpt-oss-20b", # Use an appropriate Groq model, e.g., 'llama3-8b-8192'
      messages=chat_history,
      temperature=1,
      max_completion_tokens=8192,
      reasoning_effort="medium",
      stream=True,
      stop=None
  )

  full_response_content = ""
  for chunk in completion:
      content = chunk.choices[0].delta.content or ""
      full_response_content += content
      print(content, end="") # Print as it streams

  print("\n") # Newline after the streamed response
  chat_history.append({"role": "assistant", "content": full_response_content.strip()})
  prompt = input('Digite a sua pergunta: ')



lista_de_dicionarios = []

for pergunta in lista_desfio:
  full_response_content = ""
  completion = client_groq.chat.completions.create(
      model="openai/gpt-oss-20b",
      messages=[
          {
              "role": "user",
              "content": f"Gere respostas muito sucinta para a pergunta: {pergunta}"
          }
      ],
      temperature=1, # Ajuste conforme a criatividade desejada
      max_completion_tokens=8192, # Ajuste o limite de tokens se necessário
      reasoning_effort="medium",
      stream=True,
      stop=None
  )
  for chunk in completion:
      full_response_content += chunk.choices[0].delta.content or ""

  lista_de_dicionarios.append({"Pergunta": pergunta, "resposta": full_response_content.strip()})



print(lista_de_dicionarios)

# [{'Pergunta': 'Qual é a estrutura básica de um DataFrame no Pandas?',
#   'resposta': "- Tabela bidimensional (linhas × colunas) com rótulos de índice e cabeçalhos.  \n- Cada coluna pode conter um tipo de dado distinto (int, float, str, etc.).  \n- Acesso via `df['coluna']` para colunas e `df.loc[]/df.iloc[]` para linhas.  \n- Pode ser criado a partir de dicionários, listas, arrays NumPy ou arquivos CSV/Excel."},
#  {'Pergunta': 'Como carregar dados de um arquivo CSV usando Pandas?',
#   'resposta': "- `df = pd.read_csv('caminho/para/arquivo.csv')`  \n- Se precisar de separador diferente: `pd.read_csv('arquivo.csv', sep=';')`  \n- Para ignorar linhas de cabeçalho: `pd.read_csv('arquivo.csv', header=None)`  \n- Para carregar apenas colunas específicas: `pd.read_csv('arquivo.csv', usecols=['col1', 'col2'])`"},
#  {'Pergunta': 'Como exibir as primeiras e últimas linhas de um DataFrame?',
#   'resposta': '1. `df.head()` – primeiras 5 linhas.  \n2. `df.tail()` – últimas 5 linhas.  \n3. `df.head(10)`\u202f/\u202f`df.tail(10)` – mostra 10 linhas de cada lado.  \n4. `df.iloc[[0, -1]]` – apenas a primeira e a última linha.'},
#  {'Pergunta': 'Como calcular estatísticas descritivas com Pandas?',
#   'resposta': "**Como calcular estatísticas descritivas com Pandas**\n\n1. **Carregar dados**  \n   ```python\n   import pandas as pd\n   df = pd.read_csv('arquivo.csv')   # ou pd.DataFrame(...)\n   ```\n\n2. **Método geral**  \n   ```python\n   stats = df.describe()   # soma, média, std, quartis, mínimo/máximo\n   ```\n\n3. **Coluna específica**  \n   ```python\n   df['coluna'].describe()\n   ```\n\n4. **Estatísticas customizadas**  \n   ```python\n   df.mean(); df.median(); df.std(); df.min(); df.max()\n   ```\n\n5. **Números inteiros ou booleans**  \n   ```python\n   df.describe(include=['int64','float64','bool'])\n   ```\n\n6. **Resumo resumido (sem quartis)**  \n   ```python\n   df.describe(percentiles=[])\n   ```\n\n7. **Valores nulos**  \n   ```python\n   df.isna().sum()\n   ```\n\nUse esses métodos para obter rapidamente os principais indicadores de seus dados."},
#  {'Pergunta': 'Como filtrar dados em um DataFrame?',
#   'resposta': '- `df[df[\'col\']==\'valor\']`\n- `df.loc[df[\'col\']>10]`\n- `df.query(\'col == "valor"\')`\n- `df[df[\'col\'].between(5,15)]`\n- `df[df[\'date\']>= \'2020-01-01\']`\n- `df[df[\'col\'].isin([1,2,3])]`'},
#  {'Pergunta': 'Como lidar com valores ausentes em um DataFrame?',
#   'resposta': "- **Excluir:** `df.dropna()` – remove linhas ou colunas com NaN.  \n- **Substituir por valor constante:** `df.fillna(valor)` – ex.: média, mediana.  \n- **Interpolação:** `df.interpolate(method='linear')` – preenche valores faltantes com base nos vizinhos.  \n- **Preenchimento por coluna:** `df['col'].fillna(df['col'].median(), inplace=True)` – aplica por coluna específica.  \n- **Imputação avançada:** `SimpleImputer` ou `KNNImputer` (scikit‑learn) – substitui por média, moda ou vizinhos.  \n- **Indicador de faltante:** `df['col_falt'] = df['col'].isna().astype(int)` – cria coluna flag para posterior modelagem."},
#  {'Pergunta': 'Como agrupar dados em um DataFrame?',
#   'resposta': "- **Com `groupby`:** `df.groupby('coluna')`  \n- **Agregação básica:** `df.groupby('coluna').sum()`  \n- **Múltiplas colunas:** `df.groupby(['c1', 'c2']).mean()`  \n- **Funções múltiplas:** `df.groupby('coluna').agg({'col1': 'sum', 'col2': 'mean'})`  \n- **Índice opcional:** `df.groupby('coluna', as_index=False).sum()`"},
#  {'Pergunta': 'Como mesclar dois DataFrames?',
#   'resposta': "- **Usando `merge`:**  \n  ```python\n  df3 = pd.merge(df1, df2, on='chave', how='inner')\n  ```  \n\n- **Concatenação simples:**  \n  ```python\n  df3 = pd.concat([df1, df2], axis=0)   # vertical\n  df3 = pd.concat([df1, df2], axis=1)   # horizontal\n  ```  \n\n- **Método `join` (pelo índice):**  \n  ```python\n  df3 = df1.join(df2, lsuffix='_1', rsuffix='_2')\n  ```  \n\n- **Usando `pd.concat` com `ignore_index`:**  \n  ```python\n  df3 = pd.concat([df1, df2], ignore_index=True)\n  ```"},
#  {'Pergunta': 'Como salvar um DataFrame em um arquivo CSV?',
#   'resposta': "Use o método **`to_csv`** do pandas:  \n\n```python\ndf.to_csv('arquivo.csv', index=False)   # salva sem índice\n```"},
#  {'Pergunta': 'Quais são algumas das principais funcionalidades do Pandas?',
#   'resposta': '**Principais funcionalidades do Pandas**\n\n- Manipulação de DataFrames (criar, filtrar, agrupar, pivotar).  \n- Leitura/escrita de arquivos (CSV, Excel, SQL, JSON).  \n- Operações vetorizadas e de cálculo estatístico (média, std, corr, etc.).  \n- Manipulação de datas e horários (indexação temporal, resampling).  \n- Tratamento de dados faltantes (fillna, dropna, interpolation).  \n- Agrupamentos avançados (groupby, merge, join).  \n- Visualização rápida (plot() integrado com Matplotlib).'}]


df_perguntas_e_respostas = pd.DataFrame(lista_de_dicionarios)

df_perguntas_e_respostas.to_csv("resposta2.csv", index=False,encoding="utf-8")
novo_df = pd.read_csv("resposta2.csv")
print(novo_df)




 
  # Saida da variavel "novo_df":
    

  #   .dataframe tbody tr th:only-of-type {
  #       vertical-align: middle;
  #   }

  #   .dataframe tbody tr th {
  #       vertical-align: top;
  #   }

  #   .dataframe thead th {
  #       text-align: right;
  #   }


  
    
      
  #     Pergunta
  #     resposta
    
  
  
    
  #     0
  #     Qual é a estrutura básica de um DataFrame no P...
  #     - Tabela bidimensional (linhas × colunas) com ...
    
    
  #     1
  #     Como carregar dados de um arquivo CSV usando P...
  #     - `df = pd.read_csv('caminho/para/arquivo.csv'...
    
    
  #     2
  #     Como exibir as primeiras e últimas linhas de u...
  #     1. `df.head()` – primeiras 5 linhas.  \n2. `df...
    
    
  #     3
  #     Como calcular estatísticas descritivas com Pan...
  #     **Como calcular estatísticas descritivas com P...
    
    
  #     4
  #     Como filtrar dados em um DataFrame?
  #     - `df[df['col']=='valor']`\n- `df.loc[df['col'...
    
    
  #     5
  #     Como lidar com valores ausentes em um DataFrame?
  #     - **Excluir:** `df.dropna()` – remove linhas o...
    
    
  #     6
  #     Como agrupar dados em um DataFrame?
  #     - **Com `groupby`:** `df.groupby('coluna')`  \...
    
    
  #     7
  #     Como mesclar dois DataFrames?
  #     - **Usando `merge`:**  \n  ```python\n  df3 = ...
    
    
  #     8
  #     Como salvar um DataFrame em um arquivo CSV?
  #     Use o método **`to_csv`** do pandas:  \n\n```p...
    
    
  #     9
  #     Quais são algumas das principais funcionalidad...
  #     **Principais funcionalidades do Pandas**\n\n- ...
    
  


    

  
    

  
    
  
    

  
  #   .colab-df-container {
  #     display:flex;
  #     gap: 12px;
  #   }

  #   .colab-df-convert {
  #     background-color: #E8F0FE;
  #     border: none;
  #     border-radius: 50%;
  #     cursor: pointer;
  #     display: none;
  #     fill: #1967D2;
  #     height: 32px;
  #     padding: 0 0 0 0;
  #     width: 32px;
  #   }

  #   .colab-df-convert:hover {
  #     background-color: #E2EBFA;
  #     box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
  #     fill: #174EA6;
  #   }

  #   .colab-df-buttons div {
  #     margin-bottom: 4px;
  #   }

  #   [theme=dark] .colab-df-convert {
  #     background-color: #3B4455;
  #     fill: #D2E3FC;
  #   }

  #   [theme=dark] .colab-df-convert:hover {
  #     background-color: #434B5C;
  #     box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
  #     filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
  #     fill: #FFFFFF;
  #   }
  

    
  #     const buttonEl =
  #       document.querySelector('#df-46f1ed7c-bfe7-4c90-956e-97355f8fae79 button.colab-df-convert');
  #     buttonEl.style.display =
  #       google.colab.kernel.accessAllowed ? 'block' : 'none';

  #     async function convertToInteractive(key) {
  #       const element = document.querySelector('#df-46f1ed7c-bfe7-4c90-956e-97355f8fae79');
  #       const dataTable =
  #         await google.colab.kernel.invokeFunction('convertToInteractive',
  #                                                   [key], {});
  #       if (!dataTable) return;

  #       const docLinkHtml = 'Like what you see? Visit the ' +
  #         '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
  #         + ' to learn more about interactive tables.';
  #       element.innerHTML = '';
  #       dataTable['output_type'] = 'display_data';
  #       await google.colab.output.renderOutput(dataTable, element);
  #       const docLink = document.createElement('div');
  #       docLink.innerHTML = docLinkHtml;
  #       element.appendChild(docLink);
  #     }
    
  


    
      


    
        
    

      


  # .colab-df-quickchart {
  #     --bg-color: #E8F0FE;
  #     --fill-color: #1967D2;
  #     --hover-bg-color: #E2EBFA;
  #     --hover-fill-color: #174EA6;
  #     --disabled-fill-color: #AAA;
  #     --disabled-bg-color: #DDD;
  # }

  # [theme=dark] .colab-df-quickchart {
  #     --bg-color: #3B4455;
  #     --fill-color: #D2E3FC;
  #     --hover-bg-color: #434B5C;
  #     --hover-fill-color: #FFFFFF;
  #     --disabled-bg-color: #3B4455;
  #     --disabled-fill-color: #666;
  # }

  # .colab-df-quickchart {
  #   background-color: var(--bg-color);
  #   border: none;
  #   border-radius: 50%;
  #   cursor: pointer;
  #   display: none;
  #   fill: var(--fill-color);
  #   height: 32px;
  #   padding: 0;
  #   width: 32px;
  # }

  # .colab-df-quickchart:hover {
  #   background-color: var(--hover-bg-color);
  #   box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
  #   fill: var(--button-hover-fill-color);
  # }

  # .colab-df-quickchart-complete:disabled,
  # .colab-df-quickchart-complete:disabled:hover {
  #   background-color: var(--disabled-bg-color);
  #   fill: var(--disabled-fill-color);
  #   box-shadow: none;
  # }

  # .colab-df-spinner {
  #   border: 2px solid var(--fill-color);
  #   border-color: transparent;
  #   border-bottom-color: var(--fill-color);
  #   animation:
  #     spin 1s steps(1) infinite;
  # }

  # @keyframes spin {
  #   0% {
  #     border-color: transparent;
  #     border-bottom-color: var(--fill-color);
  #     border-left-color: var(--fill-color);
  #   }
  #   20% {
  #     border-color: transparent;
  #     border-left-color: var(--fill-color);
  #     border-top-color: var(--fill-color);
  #   }
  #   30% {
  #     border-color: transparent;
  #     border-left-color: var(--fill-color);
  #     border-top-color: var(--fill-color);
  #     border-right-color: var(--fill-color);
  #   }
  #   40% {
  #     border-color: transparent;
  #     border-right-color: var(--fill-color);
  #     border-top-color: var(--fill-color);
  #   }
  #   60% {
  #     border-color: transparent;
  #     border-right-color: var(--fill-color);
  #   }
  #   80% {
  #     border-color: transparent;
  #     border-right-color: var(--fill-color);
  #     border-bottom-color: var(--fill-color);
  #   }
  #   90% {
  #     border-color: transparent;
  #     border-bottom-color: var(--fill-color);
  #   }
  # }


      
  #       async function quickchart(key) {
  #         const quickchartButtonEl =
  #           document.querySelector('#' + key + ' button');
  #         quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
  #         quickchartButtonEl.classList.add('colab-df-spinner');
  #         try {
  #           const charts = await google.colab.kernel.invokeFunction(
  #               'suggestCharts', [key], {});
  #         } catch (error) {
  #           console.error('Error during call to suggestCharts:', error);
  #         }
  #         quickchartButtonEl.classList.remove('colab-df-spinner');
  #         quickchartButtonEl.classList.add('colab-df-quickchart-complete');
  #       }
  #       (() => {
  #         let quickchartButtonEl =
  #           document.querySelector('#df-66f333bd-5379-4083-95cb-96381f5947a7 button');
  #         quickchartButtonEl.style.display =
  #           google.colab.kernel.accessAllowed ? 'block' : 'none';
  #       })();
      
    

  
    
  #     .colab-df-generate {
  #       background-color: #E8F0FE;
  #       border: none;
  #       border-radius: 50%;
  #       cursor: pointer;
  #       display: none;
  #       fill: #1967D2;
  #       height: 32px;
  #       padding: 0 0 0 0;
  #       width: 32px;
  #     }

  #     .colab-df-generate:hover {
  #       background-color: #E2EBFA;
  #       box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
  #       fill: #174EA6;
  #     }

  #     [theme=dark] .colab-df-generate {
  #       background-color: #3B4455;
  #       fill: #D2E3FC;
  #     }

  #     [theme=dark] .colab-df-generate:hover {
  #       background-color: #434B5C;
  #       box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
  #       filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
  #       fill: #FFFFFF;
  #     }
    
    

  
    
  
    
    
  #     (() => {
  #     const buttonEl =
  #       document.querySelector('#id_a195b4ce-1553-4247-8f3e-24bbc3a28b8c button.colab-df-generate');
  #     buttonEl.style.display =
  #       google.colab.kernel.accessAllowed ? 'block' : 'none';

  #     buttonEl.onclick = () => {
  #       google.colab.notebook.generateWithVariable('novo_df');
  #     }
  #     })();
    
  

    
  







