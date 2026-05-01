# Relatório de Atividade Prática  
**Análise de Séries Temporais para Previsão de Vendas**

---

## 1. Introdução e Objetivos

O objetivo desta atividade foi aplicar conceitos de **[análise de séries temporais](ca://s?q=An%C3%A1lise_de_s%C3%A9ries_temporais)** para prever vendas futuras, utilizando dados fictícios de vendas mensais.  
A proposta incluiu a aplicação de técnicas de **[suavização](ca://s?q=Suaviza%C3%A7%C3%A3o_em_s%C3%A9ries_temporais)** e **[decomposição](ca://s?q=Decomposi%C3%A7%C3%A3o_de_s%C3%A9ries_temporais)**, além do uso prático de ferramentas em Python, como **[Pandas](ca://s?q=Biblioteca_Pandas_em_Python)**, **[Matplotlib](ca://s?q=Biblioteca_Matplotlib_em_Python)**, **[NumPy](ca://s?q=Biblioteca_NumPy_em_Python)** e **[Statsmodels](ca://s?q=Biblioteca_Statsmodels_em_Python)**.  

A atividade buscou transformar dados brutos em informações acionáveis, permitindo identificar padrões de comportamento e apoiar decisões estratégicas relacionadas ao planejamento de vendas e gestão de estoques.

---

## 2. Metodologia

- **Geração de dados fictícios**: foram simuladas vendas mensais ao longo de 24 meses, incorporando tendência de crescimento, sazonalidade e ruído aleatório.  
- **Visualização inicial**: os dados foram plotados em um gráfico de linha para observar o comportamento bruto da série temporal.  
- **Suavização com média móvel**: aplicada uma janela de três meses para reduzir flutuações sazonais e destacar a tendência principal.  
- **Decomposição aditiva**: a série foi decomposta em três componentes — tendência, sazonalidade e resíduos — permitindo uma análise mais detalhada dos fatores que influenciam as vendas.  
- **Interpretação e recomendações**: os resultados foram analisados para sugerir estratégias de planejamento de vendas e gestão de estoques.

---

## 3. Experiência e Desenvolvimento

Durante a execução da atividade, foi possível observar que:  

- A **tendência** mostrou um crescimento consistente ao longo dos meses, indicando expansão gradual da demanda.  
- A **sazonalidade** revelou picos recorrentes em períodos específicos, como feriados, sugerindo a necessidade de reforço de estoque e campanhas promocionais nesses momentos.  
- Os **resíduos** apresentaram baixa variabilidade, o que reforça a estabilidade do modelo e a confiabilidade das previsões.  

A técnica de **média móvel** foi eficaz para suavizar o ruído de curto prazo, enquanto a **decomposição aditiva** permitiu separar os efeitos estruturais da série, fornecendo uma visão mais clara dos padrões de negócio.

---

## 4. Lições Aprendidas

1. **Previsibilidade e planejamento**: compreender a sazonalidade possibilita antecipar períodos de alta demanda e planejar estoques com antecedência.  
2. **Ruído vs. sinal**: nem toda queda nas vendas representa um problema estrutural; muitas vezes trata-se apenas de variações aleatórias ou sazonais.  
3. **Tomada de decisão estratégica**: modelos de séries temporais reduzem a incerteza e fornecem suporte analítico para decisões logísticas e financeiras.  
4. **Integração de ferramentas**: o uso de Python e suas bibliotecas mostrou-se essencial para manipulação de dados, visualização gráfica e aplicação de técnicas estatísticas avançadas.  

---

## 5. Conclusão

A prática demonstrou que a análise de séries temporais é uma ferramenta poderosa para **[previsão de vendas](ca://s?q=Previs%C3%A3o_de_vendas_com_s%C3%A9ries_temporais)** e tomada de decisões estratégicas.  
Ao decompor os dados em tendência, sazonalidade e resíduos, foi possível obter insights valiosos que fundamentam ações de planejamento de vendas e gestão de estoques.  

Além disso, a atividade reforçou a importância de utilizar dados históricos robustos e técnicas estatísticas adequadas para aumentar a precisão das previsões.  
A experiência prática com Python consolidou habilidades essenciais para análise de dados temporais, tornando o processo mais confiável e aplicável em cenários reais de negócios.
