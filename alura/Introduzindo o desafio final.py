import json
from collections import Counter

# 1 - Carregar o arquivo .txt e transformar em lista
with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as f:
    linhas = [linha.strip() for linha in f if linha.strip()]

# 2 - Simular envio ao modelo e gerar JSON
def simular_modelo(linha):
    partes = linha.split("$")
    usuario_id = partes[0]
    nome = partes[1]
    resenha_en = partes[2]

    # Simulação de tradução e classificação
    if any(p in resenha_en.lower() for p in ["love", "great", "wonderful", "amazing", "rocking", "incredible"]):
        avaliacao = "Positiva"
    elif any(n in resenha_en.lower() for n in ["error", "does not work", "problem", "lies", "obese", "disconnects"]):
        avaliacao = "Negativa"
    else:
        avaliacao = "Neutra"

    return {
        "usuario": nome,
        "resenha_original": resenha_en,
        "resenha_pt": "Tradução simulada",  # Aqui você pode integrar com um tradutor real
        "avaliacao": avaliacao
    }

# 3 - Lista de dicionários
lista_dicionarios = [simular_modelo(linha) for linha in linhas]

# 4 - Função para contar avaliações e unir os itens
def processar_lista(lista):
    contagem = Counter(item["avaliacao"] for item in lista)
    texto_unido = "\n---\n".join(json.dumps(item, ensure_ascii=False) for item in lista)
    return contagem, texto_unido

# Executar
contagem_final, texto_formatado = processar_lista(lista_dicionarios)

# Exibir resultados
print("Contagem de avaliações:", contagem_final)
print("\nTexto formatado:\n", texto_formatado)
