---

# Relatório da Atividade Prática  
**Aplicação do Algoritmo Naive Bayes na Filtragem de Spam**

---

## 1. Introdução
O crescimento exponencial do volume de e-mails trouxe consigo o aumento de mensagens indesejadas, conhecidas como *spam*. A filtragem automática dessas mensagens é um desafio clássico da área de Ciência de Dados e Aprendizado de Máquina. Nesta atividade prática, aplicou-se o algoritmo **Naive Bayes** para classificar e-mails como spam ou não spam, utilizando o conjunto de dados **Spambase**, disponibilizado pelo UCI Machine Learning Repository.  

O objetivo principal foi desenvolver habilidades práticas em pré-processamento de dados, treinamento de modelos de classificação e avaliação de desempenho por meio de métricas como acurácia, precisão, recall, F1-score e matriz de confusão.

---

## 2. Metodologia
### 2.1 Conjunto de Dados
O dataset Spambase contém 4.601 e-mails, cada um descrito por 57 atributos numéricos relacionados à frequência de palavras e caracteres. A variável alvo (`is_spam`) indica se o e-mail é spam (1) ou não spam (0).  

### 2.2 Etapas Realizadas
1. **Importação dos dados**: leitura do arquivo `.csv` diretamente do repositório UCI.  
2. **Separação das variáveis**: `X` com os 57 atributos e `y` com o rótulo binário.  
3. **Divisão em treino e teste**: 80% dos dados para treinamento e 20% para teste.  
4. **Treinamento do modelo**: aplicação do algoritmo **Multinomial Naive Bayes**, adequado para dados de frequência.  
5. **Avaliação**: cálculo das métricas de desempenho e construção da matriz de confusão para análise dos erros.

---

## 3. Resultados
### 3.1 Métricas de Desempenho
- **Acurácia geral**: **78,61%**  
- **Classe Não Spam (0)**:  
  - Precisão: 0.80  
  - Recall: 0.84  
  - F1-score: 0.82  
- **Classe Spam (1)**:  
  - Precisão: 0.76  
  - Recall: 0.72  
  - F1-score: 0.74  

### 3.2 Matriz de Confusão
- Verdadeiros negativos (Não Spam corretamente classificados): 445  
- Falsos positivos (Não Spam classificados como Spam): 86  
- Falsos negativos (Spam classificados como Não Spam): 111  
- Verdadeiros positivos (Spam corretamente classificados): 279  

Esses resultados mostram que o modelo teve desempenho ligeiramente superior na identificação de e-mails legítimos em comparação à detecção de spams.

---

## 4. Análise
O modelo apresentou desempenho satisfatório, com acurácia próxima de 79%. A análise da matriz de confusão revela que o maior desafio está nos **falsos negativos** (111 casos), ou seja, spams que não foram detectados. Esse tipo de erro é crítico, pois compromete a eficácia do filtro.  

Por outro lado, os **falsos positivos** (86 casos) também merecem atenção, já que classificam e-mails legítimos como spam, prejudicando a experiência do usuário. O equilíbrio entre precisão e recall mostra que o modelo é razoável, mas ainda há espaço para melhorias.

---

## 5. Possíveis Melhorias
- **Testar outros algoritmos**: como Random Forest ou Support Vector Machines, que podem capturar relações mais complexas.  
- **Normalização dos atributos**: o uso de GaussianNB poderia ser explorado, já que os atributos são contínuos.  
- **Validação cruzada**: para avaliar a estabilidade do modelo em diferentes divisões dos dados.  
- **Seleção de atributos**: reduzir dimensionalidade e eliminar variáveis pouco relevantes.  
- **Uso de TF-IDF**: caso o dataset fosse textual, essa técnica poderia melhorar a representação dos dados.

---

## 6. Conclusão
A aplicação do algoritmo Naive Bayes demonstrou ser uma solução simples e eficiente para a filtragem de spam, alcançando resultados consistentes com métricas próximas de 79% de acurácia. A atividade permitiu compreender o fluxo completo de um projeto de classificação: desde a preparação dos dados até a avaliação do modelo.  

As principais lições aprendidas incluem a importância de analisar múltiplas métricas além da acurácia, a necessidade de interpretar a matriz de confusão para identificar os tipos de erro e a relevância de explorar diferentes algoritmos e técnicas de pré-processamento para aprimorar o desempenho.  

Em síntese, o exercício reforçou a aplicabilidade prática do Naive Bayes em problemas de classificação e destacou os desafios inerentes à detecção de spam em ambientes reais.

---
