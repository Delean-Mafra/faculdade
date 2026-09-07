# Instruções

# Para esta atividade prática, construa o corpo da função simular_nltk. O objetivo é definir, diretamente no código, as variáveis e estruturas de dados que representam as saídas de um fluxo de análise e classificação de texto.

# Você deverá definir, com valores fixos, as estruturas para representar:

# - A tokenização do texto (uma lista de palavras);
# 0 A etiquetagem Morfossintática (POS Tagging) (uma lista de tuplas);
# - A frequência de palavras (um dicionário);
# - Uma mensagem de status para o treinamento do modelo;
# - As métricas de avaliação do modelo (um dicionário aninhado).

# Inclua comentários para explicar o que cada variável representaria em um fluxo de trabalho real com bibliotecas de PLN.



# Entrega:

# - Linguagem: Python;
# - Utilizar apenas estruturas nativas da linguagem;
# - Não utilizar bibliotecas externas ou funções reais do NLTK;
# - Não incluir instruções de teste ou execução de código.


def simular_nltk():
    # Referência ao contexto da atividade prática baseada no documento RNAs10.pdf.

    # 1. Tokenização do texto (lista de palavras)
    # Em um fluxo real (como utilizando word_tokenize), esta estrutura representa 
    # o texto original dividido em unidades fundamentais (tokens), como palavras e sinais de pontuação.
    tokens = ["Capitu", "olhou", "para", "Bentinho", "silenciosamente", "."]

    # 2. Etiquetagem Morfossintática / POS Tagging (lista de tuplas)
    # Representa a classificação gramatical de cada token. Em bibliotecas de PLN, 
    # isso seria o resultado de um anotador sintático (pos_tag), que associa 
    # cada palavra a uma tag (ex: NPROP para nome próprio, V para verbo, ADV para advérbio).
    pos_tags = [
        ("Capitu", "NPROP"),
        ("olhou", "V"),
        ("para", "PREP"),
        ("Bentinho", "NPROP"),
        ("silenciosamente", "ADV"),
        (".", "PONT")
    ]

    # 3. Frequência de palavras (dicionário)
    # Simula a estrutura gerada por ferramentas como o FreqDist. 
    # Mapeia cada palavra/token único do texto para a quantidade de vezes que ele ocorre, 
    # sendo útil para identificar as palavras mais relevantes ou descartar ruídos (stop words).
    frequencia_palavras = {
        "Capitu": 1,
        "olhou": 1,
        "para": 1,
        "Bentinho": 1,
        "silenciosamente": 1,
        ".": 1
    }

    # 4. Mensagem de status para o treinamento do modelo (string)
    # Representa um log ou aviso do sistema após finalizar o treinamento de um algoritmo 
    # de aprendizado de máquina (como um modelo Naive Bayes de classificação de texto).
    mensagem_status = "Treinamento do modelo concluído com sucesso. Corpus analisado: Maquimorfo."

    # 5. Métricas de avaliação do modelo (dicionário aninhado)
    # Estrutura utilizada para armazenar múltiplos indicadores de desempenho 
    # após testar o modelo contra um conjunto de dados de validação. 
    # Permite avaliar detalhes como a acurácia global e as taxas de acerto específicas por classe.
    metricas_avaliacao = {
        "geral": {
            "acuracia": 0.60,
            "tempo_processamento_segundos": 1.45
        },
        "detalhes_por_classe": {
            "NPROP": {
                "precisao": 0.82,
                "recall": 0.78
            },
            "V": {
                "precisao": 0.65,
                "recall": 0.70
            }
        }
    }

    return tokens, pos_tags, frequencia_palavras, mensagem_status, metricas_avaliacao
