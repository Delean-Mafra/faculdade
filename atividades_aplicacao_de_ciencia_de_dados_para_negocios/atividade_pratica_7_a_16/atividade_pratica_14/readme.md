# Relatório da Atividade Prática: Filtragem de Spam com Naive Bayes

## 1. Introdução
O objetivo desta atividade prática foi a aplicação do algoritmo **Multinomial Naive Bayes** para a classificação de mensagens de texto como spam ou "ham" (mensagens legítimas). A tarefa envolveu o fluxo completo de um projeto de Ciência de Dados: carregamento de dados brutos, pré-processamento de linguagem natural (vetorização), treinamento do modelo e análise rigorosa de métricas de desempenho.

## 2. Metodologia

### 2.1 Conjunto de Dados
Utilizou-se o dataset **SMS Spam Collection**, que contém 5.572 mensagens reais. Ao contrário de datasets pré-processados, este conjunto exigiu a transformação de strings (texto) em representações numéricas para que o algoritmo pudesse realizar os cálculos probabilísticos.

### 2.2 Etapas Realizadas
1.  **Divisão dos Dados**: O conjunto foi dividido utilizando a função `train_test_split`, reservando 80% das mensagens para o treinamento do modelo e 20% para o teste de validação.
2.  **Vetorização com CountVectorizer**: Atendendo aos objetivos da atividade, utilizou-se o `CountVectorizer`. Esta ferramenta converteu as mensagens em uma matriz de contagem de tokens, construindo um vocabulário a partir das palavras presentes nas mensagens de treino.
3.  **Treinamento**: O classificador `MultinomialNB` foi ajustado aos dados vetorizados. Este algoritmo foi escolhido por ser o padrão ouro para problemas de classificação baseados em frequências de palavras.
4.  **Avaliação**: O modelo realizou predições sobre 1.115 mensagens inéditas (conjunto de teste) para validar sua eficácia.

## 3. Resultados

### 3.1 Métricas de Desempenho
Os resultados obtidos foram extremamente satisfatórios, conforme detalhado abaixo:

*   **Acurácia Geral**: **99,19%**
*   **Classe Legítima (0 - Ham)**:
    *   Precisão: 0.99
    *   Recall: 1.00
    *   F1-score: 1.00
*   **Classe Spam (1)**:
    *   Precisão: **1.00**
    *   Recall: 0.94
    *   F1-score: 0.97

### 3.2 Análise das Métricas
A métrica mais impressionante foi a **Precisão de 1.00 para a classe Spam**. Isso indica que, das mensagens classificadas como spam pelo modelo, **todas eram realmente spam**. Em um cenário real, isso significa que nenhum SMS legítimo do usuário seria movido para a pasta de lixo eletrônico por engano. O **Recall de 0.94** mostra que o modelo conseguiu capturar 94% de todos os spams existentes, deixando passar apenas uma pequena fração.

## 4. Discussão
A alta performance do modelo demonstra que o Naive Bayes, apesar de sua simplicidade e da "suposição ingênua" de independência entre as palavras, é altamente eficaz para classificação de textos curtos. A etapa de vetorização foi crucial, pois permitiu ao modelo identificar palavras-chave que possuem forte correlação estatística com mensagens indesejadas, como termos promocionais ou de urgência.

## 5. Possíveis Melhorias
Apesar do resultado próximo à perfeição, em conjuntos de dados maiores ou mais complexos (como e-mails longos), poderiam ser exploradas:
*   **N-grams**: Analisar sequências de duas ou três palavras (ex: "você ganhou") em vez de palavras isoladas.
*   **TF-IDF**: Aplicar uma ponderação para diminuir a importância de palavras muito frequentes que não ajudam na distinção (como conectivos).
*   **Limpeza de Texto (Stopwords)**: Remover pontuações e palavras vazias para reduzir o ruído nos dados.

## 6. Conclusão
A atividade permitiu o desenvolvimento de habilidades fundamentais em Processamento de Linguagem Natural e Aprendizado de Máquina. A implementação do `CountVectorizer` foi o diferencial técnico que possibilitou a transição do texto bruto para um modelo matemático de alta precisão. O resultado final de **99,19% de acurácia** valida a eficiência do Naive Bayes como uma solução robusta, rápida e confiável para o problema de filtragem de spam.

---
