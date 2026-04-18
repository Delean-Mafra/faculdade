# Relatório Atividade Prática 6

## Capa
**Título:** Construção e Avaliação de Modelos de Machine Learning para Previsão de Vendas e Detecção de Fraudes  
**Autor:** Delean Mafra  
**Instituição:** Curso de Ciência de Dados  
**Data:** Abril de 2026  

---

## Resumo
Este relatório apresenta a aplicação de técnicas de Machine Learning em dois contextos de negócios distintos: previsão de vendas e detecção de fraudes. Utilizando os arquivos `vendas.csv` e `fraudes.csv`, foram construídos modelos de regressão linear e regressão logística, respectivamente. A análise incluiu preparação dos dados, treinamento dos modelos e avaliação por métricas adequadas. Os resultados demonstram a aplicabilidade das técnicas para apoiar decisões estratégicas em e-commerce e segurança financeira.

**Palavras-chave:** Machine Learning, Previsão de Vendas, Detecção de Fraudes, Regressão Linear, Regressão Logística.

---

## Introdução
A inteligência artificial e o aprendizado de máquina têm se consolidado como ferramentas essenciais para a tomada de decisão em ambientes empresariais. Este trabalho tem como objetivo aplicar conceitos de Machine Learning para prever a demanda de produtos e identificar transações fraudulentas, utilizando bases de dados fictícias. A atividade foi desenvolvida em conformidade com a norma **ABNT NBR 14724:2024**, que estabelece padrões para a apresentação de trabalhos acadêmicos.

---

## Metodologia
### Base de Dados
- **Vendas:** O arquivo `vendas.csv` contém 24 registros mensais com colunas `Meses`, `Vendas` e `Eventos`.  
- **Fraudes:** O arquivo `fraudes.csv` contém 1000 registros de transações financeiras com colunas `Valor`, `Local` e `Fraude`.

### Ferramentas
Foram utilizadas as bibliotecas **Pandas**, **NumPy**, **Scikit-learn** e **Matplotlib** em ambiente Jupyter Notebook.

### Procedimentos
**Previsão de Vendas:**  
- Divisão dos dados em treino (70%) e teste (30%).  
- Treinamento de modelo de regressão linear com variáveis `Meses` e `Eventos`.  
- Avaliação por **Erro Médio Quadrático (MSE)** e **Coeficiente de Determinação (R²)**.  

**Detecção de Fraudes:**  
- Pré-processamento com one-hot encoding para variável categórica `Local`.  
- Divisão dos dados em treino (70%) e teste (30%).  
- Treinamento de modelo de regressão logística com balanceamento de classes.  
- Avaliação por **acurácia**, **matriz de confusão**, **precision**, **recall** e **f1-score**.  

---

## Resultados e Discussão
### Previsão de Vendas
O modelo de regressão linear apresentou valores de **R² = -0,64**, indicando que o modelo não consegue superar a média simples das vendas com os dados atuais. O **MSE foi de aproximadamente 2379,54**, refletindo erros elevados. Isso sugere a necessidade de mais variáveis explicativas ou um histórico de dados mais longo.

### Detecção de Fraudes
O modelo de regressão logística para detecção de fraudes apresentou **acurácia de aproximadamente 45%** e **AUC ROC de 0,455**, indicando desempenho próximo ao acaso na discriminação entre transações legítimas e fraudulentas. A matriz de confusão e as métricas de precisão, recall e f1-score refletem a dificuldade do modelo em identificar corretamente as classes, sugerindo que as variáveis disponíveis não são suficientes para uma boa predição. Em cenários reais, seria recomendada a inclusão de variáveis adicionais, como horário da transação, IP de origem ou comportamento histórico do usuário, além de técnicas avançadas de engenharia de atributos para melhorar o desempenho.

### Lições Aprendidas
- A importância do pré-processamento adequado para garantir qualidade dos modelos.  
- A necessidade de escolher métricas apropriadas para cada tipo de problema.  
- O impacto de variáveis externas (eventos, locais) na performance dos modelos.  
- A relevância da governança e ética na aplicação de IA em contextos empresariais.  

---

## Considerações Éticas e Governança
- **Ética:** Garantir anonimização e evitar vieses nos dados.  
- **Transparência:** Documentar todas as etapas do processo de modelagem.  
- **Conformidade Legal:** Seguir a LGPD e demais regulamentações.  
- **Responsabilidade:** Definir papéis claros para manutenção e monitoramento dos modelos.  

---

## Conclusão
A atividade demonstrou a aplicabilidade de modelos de Machine Learning em problemas reais de negócios. A regressão linear mostrou-se limitada para previsão de vendas, enquanto a regressão logística apresentou resultados insatisfatórios na detecção de fraudes. É necessário ampliar as bases de dados e explorar modelos mais complexos para aumentar a precisão. O trabalho reforça a importância da ética e da governança na utilização de IA.

---

## Referências
ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724:2024 – Trabalhos Acadêmicos – Apresentação**. Rio de Janeiro: ABNT, 2024.  
PEDREGOSA, F. et al. **Scikit-learn: Machine Learning in Python**. Journal of Machine Learning Research, v. 12, p. 2825–2830, 2011.  
MCKINNEY, W. **Data Analysis with Pandas**. O’Reilly Media, 2018.  
