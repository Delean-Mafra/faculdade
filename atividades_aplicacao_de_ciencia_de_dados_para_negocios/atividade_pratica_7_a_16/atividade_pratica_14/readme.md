# Atividade Prática 14 – Aplicação de Naive Bayes para Filtragem de Spam

Este diretório foi criado para registrar a **Atividade Prática 14** da disciplina **Prática Integradora em Ciência de Dados para Negócios**.

---

## 🎯 Objetivos
- Aplicar o algoritmo de **Naive Bayes** na classificação de mensagens como spam ou não spam.  
- Desenvolver habilidades práticas em **pré-processamento de dados textuais** e treinamento de modelos de aprendizado de máquina.  
- Avaliar e interpretar o desempenho do modelo utilizando métricas como **acurácia, precisão, recall, F1-score** e **matriz de confusão**.  

---

## 📚 Materiais, Métodos e Ferramentas

**Materiais**  
- Conjunto de dados contendo mensagens rotuladas como spam ou não spam (SMS Spam Collection).  

**Métodos**  
1. Importação e pré-processamento dos dados.  
2. Vetorização dos textos com **CountVectorizer**.  
3. Treinamento do modelo **Multinomial Naive Bayes**.  
4. Avaliação do modelo com métricas de desempenho e matriz de confusão.  

**Ferramentas**  
- Google Colab ou Jupyter Notebook  
- Bibliotecas Python: `Pandas`, `Scikit-learn`, `Seaborn`, `Matplotlib`  

---

## 🛠️ Passo a Passo da Atividade
1. Importação e limpeza dos dados.  
2. Vetorização dos textos com `CountVectorizer`.  
3. Divisão em treino (80%) e teste (20%).  
4. Treinamento do modelo Naive Bayes.  
5. Avaliação com métricas de desempenho.  
6. Interpretação dos resultados e discussão de melhorias.  

---

## 📊 Resultados Obtidos
- **Acurácia geral**: 99,19%  
- **Classe Ham (mensagens legítimas)**  
  - Precisão: 0.99  
  - Recall: 1.00  
  - F1-score: 1.00  
- **Classe Spam**  
  - Precisão: 1.00  
  - Recall: 0.94  
  - F1-score: 0.97  

A matriz de confusão mostrou que o modelo classificou corretamente quase todas as mensagens, com pouquíssimos falsos negativos.

---

## 🔎 Discussão
- O modelo demonstrou alta eficácia, confirmando que o **Naive Bayes** é uma solução robusta para classificação de textos curtos.  
- A vetorização com `CountVectorizer` foi essencial para transformar o texto bruto em representações numéricas.  
- Possíveis melhorias incluem uso de **N-grams**, **TF-IDF** e remoção de stopwords para reduzir ruído.  

---

## ✅ Conclusão
A atividade permitiu consolidar conhecimentos em **Processamento de Linguagem Natural (PLN)** e **Aprendizado de Máquina**.  
O resultado final de **99,19% de acurácia** valida a eficiência do Naive Bayes como uma solução rápida e confiável para filtragem de spam.  

---

📌 Este repositório contém:  
- O notebook da atividade (`atividade_pratica14.ipynb`)  
- O relatório descritivo da prática  
