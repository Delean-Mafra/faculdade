def simular_chatbot(mensagem):
    # Define as listas de palavras predefinidas para a análise de sentimento
    palavras_positivas = ["adoro", "amo", "excelente", "bom", "ótimo", "feliz"]
    palavras_negativas = ["odeio", "ruim", "péssimo", "terrível", "chateado"]
    
    # Converte a string de entrada para letras minúsculas e a divide em uma lista de palavras
    # Isso padroniza a verificação e evita falsos positivos com substrings (ex: 'bomba' ativando 'bom')
    palavras_mensagem = mensagem.lower().split()
    
    # Define o sentimento padrão inicial
    sentimento_detectado = "neutro"
    
    # Lógica de classificação:
    # 1. Itera sobre as palavras da mensagem para buscar marcadores positivos
    for palavra in palavras_mensagem:
        # Remove pontuações comuns que podem estar grudadas à palavra
        palavra_limpa = palavra.strip('.,!?')
        if palavra_limpa in palavras_positivas:
            sentimento_detectado = "positivo"
            break # Interrompe a busca no primeiro acerto
            
    # 2. Se o sentimento continuar neutro, busca por marcadores negativos
    if sentimento_detectado == "neutro":
        for palavra in palavras_mensagem:
            palavra_limpa = palavra.strip('.,!?')
            if palavra_limpa in palavras_negativas:
                sentimento_detectado = "negativo"
                break
                
    # Seleção de resposta:
    # Direciona uma string de resposta correspondente ao sentimento_detectado
    if sentimento_detectado == "positivo":
        resposta = "Que maravilha! Fico muito feliz com isso. Como posso continuar te ajudando hoje?"
    elif sentimento_detectado == "negativo":
        resposta = "Sinto muito que você esteja passando por isso. Há algo específico que eu possa fazer para ajudar?"
    else:
        resposta = "Entendi. Por favor, me diga em que mais posso ser útil."
        
    return resposta
