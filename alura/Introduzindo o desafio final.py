import json

# 1 - Carregar o arquivo .txt
with open("resenhas.txt", "r", encoding="utf-8") as arquivo:
    linhas = [linha.strip() for linha in arquivo if linha.strip()]

# 2 - Enviar ao modelo local (simulação aqui com função fictícia)
def analisar_resenha(resenha):
    # Simulação de resposta do modelo
    return {
        "usuario": "usuario_desconhecido",
        "resenha_original": resenha,
        "resenha_pt": "Tradução simulada da resenha",
        "avaliacao": "Neutra"  # ou "Positiva", "Negativa"
    }

# 3 - Transformar em lista de dicionários
lista_de_dicionarios = [analisar_resenha(resenha) for resenha in linhas]

# 4 - Função para contar avaliações e unir os textos
def processar_resenhas(lista):
    contagem = {"Positiva": 0, "Negativa": 0, "Neutra": 0}
    texto_unido = ""

    for item in lista:
        avaliacao = item["avaliacao"]
        contagem[avaliacao] += 1
        texto_unido += json.dumps(item) + "\n---\n"

    return contagem, texto_unido

# Executar a função
contagem_final, texto_formatado = processar_resenhas(lista_de_dicionarios)

# Exibir resultados
print("Contagem de avaliações:", contagem_final)
print("\nTexto unido:\n", texto_formatado)
