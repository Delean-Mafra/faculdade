def simular_ri():
    # Lista de palavras-chave (tokens) extraídas durante o pré-processamento.
    # Representa os termos essenciais da busca do usuário após a limpeza e tokenização do texto.
    tokens_busca = ["recuperacao", "informacao", "algoritmos"]

    # Número inteiro que representa a distância de Levenshtein.
    # Indica a quantidade mínima de operações necessárias para transformar
    # a string de busca em uma string encontrada em um documento.
    distancia_levenshtein = 4

    # Número de ponto flutuante que representa a similaridade obtida pelo modelo Bag-of-Words.
    # Indica o grau de proximidade entre a consulta e o documento analisado.
    similaridade_bow = 0.85

    return tokens_busca, distancia_levenshtein, similaridade_bow
