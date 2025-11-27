import json
import pandas as pd
import requests
from collections import Counter

# -------------------------------
# 1. Tratamento de exceções
# -------------------------------
def operacoes_arriscadas(a, b):
    try:
        x = int(a)  # pode gerar ValueError
        y = b + "texto"  # pode gerar TypeError
        z = x / 0  # gera ZeroDivisionError
        return x, y, z

    except ValueError as e:
        print(f"[ValueError] Entrada inválida: {e}. Forneça números válidos.")
    except TypeError as e:
        print(f"[TypeError] Tipo incompatível: {e}. Verifique os tipos das variáveis.")
    except ZeroDivisionError as e:
        print(f"[ZeroDivisionError] Não é possível dividir por zero: {e}.")
    except Exception as e:
        print(f"[Erro não previsto] Ocorreu um erro inesperado: {e}")
    finally:
        print("[Finally] Encerrando recursos (ex.: fechar arquivos).")

# -------------------------------
# 2. Classificação heurística simples
# -------------------------------
def classificar_sentimentos_heuristico(texto):
    t = texto.lower()
    positivos = ["great", "wonderful", "amazing", "love", "rocking", "incredible"]
    negativos = ["error", "does not work", "problem", "lies", "obese", "disconnects", "stuck", "limit"]
    if any(p in t for p in positivos):
        return "Positivo"
    if any(n in t for n in negativos):
        return "Negativo"
    return "Neutro"

# -------------------------------
# 3. Preparar DataFrame
# -------------------------------
def preparar_dataframe(caminho_csv):
    df = pd.read_csv(caminho_csv)
    if "sentimento" not in df.columns:
        df["sentimento"] = df["reviewText"].astype(str).apply(classificar_sentimentos_heuristico)
    return df

# -------------------------------
# 4. Prompts para LLM
# -------------------------------
def prompt_categorias(resenhas_unidas):
    return f"""
Você é um analista de dados. Vou te passar muitas resenhas negativas de um produto, separadas por '###'.
Encontre 5 categorias de reclamações.
- Cada categoria deve ser definida por APENAS uma palavra
- Sem acentos, em letra minúscula
- Retorne exatamente 5 categorias, separadas por vírgula

Resenhas:
{resenhas_unidas}
"""

def prompt_json_por_resenha(resenhas_unidas):
    return f"""
Você é um analista de dados. Receberá resenhas negativas separadas por '###'.
Para cada resenha, retorne APENAS um objeto JSON com:
- "resenha_original": a resenha em inglês
- "resenha_pt": tradução para português
- "categoria": uma palavra (minúscula, sem acentos)

Formato (um JSON por linha):
{{"resenha_original": "...", "resenha_pt": "...", "categoria": "..."}}

Resenhas:
{resenhas_unidas}
"""

# -------------------------------
# 5. Cliente LLM local (exemplo com Ollama)
# -------------------------------
def llm_local_generate(prompt, model="gemma:2b"):
    try:
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False}
        )
        r.raise_for_status()
        data = r.json()
        return data.get("response", "")
    except requests.RequestException as e:
        print(f"[LLM local] Erro de conexão: {e}")
        return ""

# -------------------------------
# 6. Funções para obter categorias e JSONs
# -------------------------------
def obter_categorias(resenhas_unidas):
    texto = llm_local_generate(prompt_categorias(resenhas_unidas))
    categorias = [c.strip() for c in texto.split(",") if c.strip()]
    return categorias[:5]

def obter_jsons(resenhas_unidas):
    texto = llm_local_generate(prompt_json_por_resenha(resenhas_unidas))
    linhas = [l for l in texto.splitlines() if l.strip()]
    dicionarios = []
    for l in linhas:
        try:
            dicionarios.append(json.loads(l))
        except json.JSONDecodeError:
            pass
    return dicionarios

# -------------------------------
# 7. Processamento em lote
# -------------------------------
def processar_lote(df):
    # Filtrar negativas
    df_neg = df[df["sentimento"] == "Negativo"].copy()
    resenhas_unidas = "###".join(df_neg["reviewText"].astype(str).tolist())

    # Categorias
    categorias = obter_categorias(resenhas_unidas)

    # JSON por resenha
    jsons = obter_jsons(resenhas_unidas)

    # Contagem de avaliações
    contagem = df["sentimento"].value_counts().to_dict()

    # Texto unificado
    texto_unico = "\n---\n".join(json.dumps(j, ensure_ascii=False) for j in jsons)

    return {
        "categorias": categorias,
        "contagem_sentimentos": contagem,
        "jsons_por_resenha": jsons,
        "texto_unificado": texto_unico,
    }

# -------------------------------
# 8. Execução principal
# -------------------------------
if __name__ == "__main__":
    # Teste de exceções
    operacoes_arriscadas("abc", 10)
    operacoes_arriscadas("12", 10)
    operacoes_arriscadas("12", "ok")

    # Preparar DataFrame
    df = preparar_dataframe("reviews.csv")

    # Processar lote
    resultado = processar_lote(df)

    print("Categorias:", resultado["categorias"])
    print("Contagem:", resultado["contagem_sentimentos"])
    print("Texto unificado:\n", resultado["texto_unificado"])
