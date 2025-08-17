"""
Disciplina: Estatística Aplicada
Tema: Distribuição Amostral e Estimação
Data: Agosto de 2025

ENUNCIADO DO PROBLEMA:
Considere uma população com distribuição normal que possui desvio padrão populacional 
σ = 32. Para uma amostra de tamanho n = 4, calcule o erro padrão da média. 
Analise o comportamento do erro padrão quando o tamanho da amostra é sucessivamente 
quadruplicado.

FUNDAMENTAÇÃO TEÓRICA:
O erro padrão da média (σₓ̄) é uma medida da variabilidade da distribuição amostral 
das médias amostrais. Segundo o Teorema Central do Limite, para amostras extraídas 
de uma população com distribuição normal, a distribuição das médias amostrais segue 
a fórmula: σₓ̄ = σ/√n

PARÂMETROS DO PROBLEMA:
- Desvio padrão populacional (σ): 32
- Tamanho inicial da amostra (n): 4
- Distribuição populacional: Normal

SOLUÇÃO ANALÍTICA:
σₓ̄ = σ/√n = 32/√4 = 32/2 = 16

OBJETIVO: Demonstrar matematicamente e computacionalmente o comportamento do erro 
padrão da média quando o tamanho da amostra é quadruplicado sucessivamente.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def resolver_questao_erro_padrao():
    """
    Função principal para resolução do problema proposto sobre erro padrão da média.
    
    Esta função implementa a solução completa do exercício, incluindo:
    - Cálculo direto do erro padrão inicial
    - Análise do comportamento com quadruplicação da amostra
    - Demonstração matemática dos resultados
    - Verificação numérica dos padrões identificados
    
    Returns:
        tuple: Contém os tamanhos de amostra analisados e seus respectivos erros padrão
    """
    
    print("=" * 85)
    print("RESOLUÇÃO DO EXERCÍCIO: ERRO PADRÃO DA MÉDIA EM DISTRIBUIÇÃO NORMAL")
    print("=" * 85)
    
    # Definição dos parâmetros conforme enunciado
    sigma = 32  # Desvio padrão populacional
    n_inicial = 4  # Tamanho inicial da amostra
    
    print("1. DADOS FORNECIDOS NO PROBLEMA:")
    print(f"   • Desvio padrão populacional (σ): {sigma}")
    print(f"   • Tamanho da amostra inicial (n): {n_inicial}")
    print(f"   • Tipo de distribuição: Normal")
    print()
    
    # SEÇÃO 1: SOLUÇÃO DIRETA DO PROBLEMA
    print("2. CÁLCULO DO ERRO PADRÃO DA MÉDIA")
    print("-" * 50)
    
    def calcular_erro_padrao(sigma, n):
        """
        Calcula o erro padrão da média utilizando a fórmula estatística padrão.
        
        Fórmula: σₓ̄ = σ/√n
        
        Parâmetros:
        -----------
        sigma : float
            Desvio padrão populacional
        n : int
            Tamanho da amostra
            
        Retorna:
        --------
        float
            Valor do erro padrão da média
        """
        return sigma / np.sqrt(n)
    
    erro_padrao_inicial = calcular_erro_padrao(sigma, n_inicial)
    
    print("   Aplicação da fórmula fundamental:")
    print("   σₓ̄ = σ/√n")
    print()
    print("   Substituição dos valores:")
    print(f"   σₓ̄ = {sigma}/√{n_inicial}")
    print(f"   σₓ̄ = {sigma}/{np.sqrt(n_inicial):.1f}")
    print(f"   σₓ̄ = {erro_padrao_inicial}")
    print()
    print(f"   RESULTADO: O erro padrão da média é {erro_padrao_inicial}")
    print()
    
    # SEÇÃO 2: ANÁLISE DO COMPORTAMENTO COM QUADRUPLICAÇÃO
    print("3. ANÁLISE DO COMPORTAMENTO COM QUADRUPLICAÇÃO DA AMOSTRA")
    print("-" * 65)
    
    print("   Hipótese a ser testada:")
    print("   Quando o tamanho da amostra é quadruplicado, o erro padrão é reduzido pela metade.")
    print()
    
    # Demonstração numérica com múltiplas quadruplicações
    print("   Tabela de resultados:")
    print(f"   {'Iteração':<10}{'n':<10}{'√n':<10}{'Cálculo':<15}{'σₓ̄':<12}{'Observação':<20}")
    print("   " + "-" * 75)
    
    tamanhos_amostra = [4, 16, 64, 256, 1024]  # Progressão com quadruplicação
    erros_padrao = []
    
    for i, n in enumerate(tamanhos_amostra):
        erro_atual = calcular_erro_padrao(sigma, n)
        erros_padrao.append(erro_atual)
        raiz_n = np.sqrt(n)
        calculo_str = f"{sigma}/√{n}"
        
        if i == 0:
            observacao = "(valor inicial)"
        else:
            fator_reducao = erros_padrao[0] / erro_atual
            observacao = f"redução de {fator_reducao:.1f}x"
            
        print(f"   {i+1:<10}{n:<10}{raiz_n:<10.1f}{calculo_str:<15}{erro_atual:<12.2f}{observacao:<20}")
    
    print()
    
    # SEÇÃO 3: DEMONSTRAÇÃO MATEMÁTICA
    print("4. FUNDAMENTAÇÃO MATEMÁTICA DO PADRÃO OBSERVADO")
    print("-" * 55)
    
    print("   Demonstração algébrica:")
    print()
    print("   Seja σₓ̄₁ o erro padrão inicial:")
    print("   σₓ̄₁ = σ/√n")
    print()
    print("   Quando quadruplicamos o tamanho da amostra (n → 4n):")
    print("   σₓ̄₂ = σ/√(4n)")
    print()
    print("   Aplicando propriedades da radiciação:")
    print("   √(4n) = √4 × √n = 2√n")
    print()
    print("   Portanto:")
    print("   σₓ̄₂ = σ/(2√n) = (1/2) × (σ/√n) = σₓ̄₁/2")
    print()
    print("   CONCLUSÃO TEÓRICA: σₓ̄₂ = σₓ̄₁/2")
    print("   (O erro padrão com amostra quadruplicada é metade do valor inicial)")
    
    # Verificação numérica da demonstração teórica
    print()
    print("   Verificação numérica:")
    n1, n2 = 4, 16
    erro1 = calcular_erro_padrao(sigma, n1)
    erro2 = calcular_erro_padrao(sigma, n2)
    razao_observada = erro1 / erro2
    
    print(f"   • Para n₁ = {n1}: σₓ̄₁ = {erro1}")
    print(f"   • Para n₂ = {n2}: σₓ̄₂ = {erro2}")
    print(f"   • Razão σₓ̄₁/σₓ̄₂ = {razao_observada:.1f}")
    print("   • Confirmação: A razão é exatamente 2, validando a teoria.")
    print()
    
    # SEÇÃO 4: GERAÇÃO DO GRÁFICO
    print("5. REPRESENTAÇÃO GRÁFICA DOS RESULTADOS")
    print("-" * 45)
    print("   Gerando visualização gráfica para análise complementar...")
    criar_grafico_erro_padrao(tamanhos_amostra, erros_padrao, sigma)
    
    # SEÇÃO 5: CONCLUSÕES
    print("6. CONCLUSÕES DO ESTUDO")
    print("-" * 30)
    print(f"   • O erro padrão da média para σ=32 e n=4 é: {erro_padrao_inicial}")
    print("   • Padrão identificado: Quadruplicar n resulta em redução do erro padrão pela metade")
    print("   • Base matemática: Relação σ/√(4n) = σ/(2√n) = (σ/√n)/2")
    print("   • Implicação prática: Para reduzir o erro padrão pela metade, são necessárias")
    print("     quatro vezes mais observações na amostra")
    print("   • Validação: Os resultados numéricos confirmam a fundamentação teórica")
    
    return tamanhos_amostra, erros_padrao

def criar_grafico_erro_padrao(tamanhos_amostra, erros_padrao, sigma):
    """
    Função para criação de visualizações gráficas dos resultados obtidos.
    
    Esta função gera um conjunto de gráficos para análise visual do comportamento
    do erro padrão da média em relação ao tamanho da amostra.
    
    Parâmetros:
    -----------
    tamanhos_amostra : list
        Lista com os tamanhos de amostra analisados
    erros_padrao : list
        Lista com os valores de erro padrão correspondentes
    sigma : float
        Desvio padrão populacional utilizado nos cálculos
    """
    
    plt.figure(figsize=(14, 10))
    plt.suptitle('Análise Gráfica: Comportamento do Erro Padrão da Média', 
                 fontsize=16, fontweight='bold')
    
    # Gráfico 1: Relação entre tamanho da amostra e erro padrão
    plt.subplot(2, 2, 1)
    plt.plot(tamanhos_amostra, erros_padrao, 'bo-', linewidth=2, markersize=8, 
             label='Valores Calculados')
    
    # Curva teórica para comparação
    n_teorico = np.linspace(4, max(tamanhos_amostra), 200)
    erro_teorico = sigma / np.sqrt(n_teorico)
    plt.plot(n_teorico, erro_teorico, 'r--', linewidth=2, 
             label='Curva Teórica: σ/√n')
    
    plt.xlabel('Tamanho da Amostra (n)', fontsize=11)
    plt.ylabel('Erro Padrão (σₓ̄)', fontsize=11)
    plt.title('Erro Padrão vs Tamanho da Amostra', fontsize=12, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log', base=4)  # Escala logarítmica base 4
    
    # Gráfico 2: Análise do fator de redução
    plt.subplot(2, 2, 2)
    fatores_reducao = [erros_padrao[0]/erro for erro in erros_padrao]
    cores = ['blue', 'green', 'orange', 'red', 'purple']
    barras = plt.bar(range(len(tamanhos_amostra)), fatores_reducao, 
                     color=cores, alpha=0.7, edgecolor='black')
    
    plt.xlabel('Iterações (Quadruplicação)', fontsize=11)
    plt.ylabel('Fator de Redução', fontsize=11)
    plt.title('Fatores de Redução do Erro Padrão', fontsize=12, fontweight='bold')
    plt.xticks(range(len(tamanhos_amostra)), 
               [f'n={n}' for n in tamanhos_amostra], rotation=45)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Adiciona valores nas barras
    for i, (barra, fator) in enumerate(zip(barras, fatores_reducao)):
        plt.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.1,
                f'{fator:.1f}x', ha='center', va='bottom', fontweight='bold')
    
    # Gráfico 3: Linearidade da relação √n vs erro padrão
    plt.subplot(2, 2, 3)
    raizes_n = [np.sqrt(n) for n in tamanhos_amostra]
    plt.plot(raizes_n, erros_padrao, 'go-', linewidth=2, markersize=8,
             label='Pontos Observados')
    
    # Linha de tendência teórica
    raiz_teorica = np.linspace(min(raizes_n), max(raizes_n), 100)
    erro_teorico_linear = sigma / raiz_teorica
    plt.plot(raiz_teorica, erro_teorico_linear, 'r--', linewidth=2,
             label='Relação Teórica')
    
    plt.xlabel('√n', fontsize=11)
    plt.ylabel('Erro Padrão (σₓ̄)', fontsize=11)
    plt.title('Verificação da Linearidade: √n vs Erro Padrão', 
              fontsize=12, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfico 4: Resumo teórico
    plt.subplot(2, 2, 4)
    plt.text(0.1, 0.9, 'FUNDAMENTOS TEÓRICOS', fontsize=14, 
             fontweight='bold', transform=plt.gca().transAxes)
    plt.text(0.1, 0.75, 'Fórmula Principal:', fontsize=12, 
             fontweight='bold', transform=plt.gca().transAxes)
    plt.text(0.1, 0.65, 'σₓ̄ = σ/√n', fontsize=18, 
             fontweight='bold', color='blue', transform=plt.gca().transAxes)
    
    plt.text(0.1, 0.5, f'Parâmetros do Problema:', fontsize=12, 
             fontweight='bold', transform=plt.gca().transAxes)
    plt.text(0.1, 0.4, f'• σ = {sigma} (desvio padrão populacional)', 
             fontsize=11, transform=plt.gca().transAxes)
    plt.text(0.1, 0.35, '• n = tamanho da amostra', fontsize=11, 
             transform=plt.gca().transAxes)
    
    plt.text(0.1, 0.2, 'Padrão Identificado:', fontsize=12, 
             fontweight='bold', transform=plt.gca().transAxes)
    plt.text(0.1, 0.1, 'n × 4 → σₓ̄ ÷ 2', fontsize=14, 
             fontweight='bold', color='red', transform=plt.gca().transAxes)
    plt.text(0.1, 0.02, '(Quadruplicar n reduz erro padrão pela metade)', 
             fontsize=10, style='italic', transform=plt.gca().transAxes)
    
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print("   Gráficos gerados com sucesso.")
    print("   Os gráficos demonstram a consistência entre teoria e prática.")
    print()

# Funções auxiliares para análise complementar

def demonstrar_independencia_sigma():
    """
    Função para demonstrar que o padrão de redução é independente do valor de σ.
    
    Esta análise complementar mostra que a propriedade matemática de redução
    pela metade do erro padrão, quando o tamanho da amostra é quadruplicado,
    é válida independentemente do valor do desvio padrão populacional.
    """
    print("\n" + "=" * 85)
    print("ANÁLISE COMPLEMENTAR: INDEPENDÊNCIA DO PADRÃO EM RELAÇÃO AO VALOR DE σ")
    print("=" * 85)
    
    print("   Objetivo: Verificar se o padrão σₓ̄₂ = σₓ̄₁/2 é válido para diferentes valores de σ")
    print()
    
    # Teste com diferentes valores de sigma
    valores_sigma = [1, 5, 10, 20, 32, 50]
    n1, n2 = 4, 16  # n2 = 4 × n1 (quadruplicação)
    
    print(f"   Comparação entre n₁ = {n1} e n₂ = {n2} (quadruplicação)")
    print(f"   {'σ':<8}{'σₓ̄₁ (n=4)':<15}{'σₓ̄₂ (n=16)':<15}{'Razão':<10}{'Status':<15}")
    print("   " + "-" * 70)
    
    for sigma in valores_sigma:
        erro1 = sigma / np.sqrt(n1)
        erro2 = sigma / np.sqrt(n2)
        razao = erro1 / erro2
        status = "✓ Confirmado" if abs(razao - 2.0) < 0.001 else "✗ Discrepante"
        
        print(f"   {sigma:<8}{erro1:<15.4f}{erro2:<15.4f}{razao:<10.1f}{status:<15}")
    
    print()
    print("   CONCLUSÃO: A razão é consistentemente 2.0 para todos os valores de σ testados.")
    print("   Isso confirma que o padrão é uma propriedade matemática intrínseca da fórmula.")


def analise_teorica_avancada():
    """
    Função para apresentar análise teórica avançada do problema.
    
    Esta seção fornece fundamentação matemática mais profunda sobre o
    comportamento do erro padrão e suas implicações práticas.
    """
    print("\n" + "=" * 85)
    print("ANÁLISE TEÓRICA AVANÇADA")
    print("=" * 85)
    
    print("   1. RELAÇÃO MATEMÁTICA FUNDAMENTAL")
    print("   " + "-" * 40)
    print("      Para qualquer fator multiplicativo k aplicado ao tamanho da amostra:")
    print("      Se n₂ = k × n₁, então σₓ̄₂ = σₓ̄₁/√k")
    print()
    print("      Casos especiais:")
    print("      • k = 4 (quadruplicação): σₓ̄₂ = σₓ̄₁/√4 = σₓ̄₁/2")
    print("      • k = 9 (multiplicação por 9): σₓ̄₂ = σₓ̄₁/√9 = σₓ̄₁/3")
    print("      • k = 16 (multiplicação por 16): σₓ̄₂ = σₓ̄₁/√16 = σₓ̄₁/4")
    print()
    
    print("   2. IMPLICAÇÕES PRÁTICAS")
    print("   " + "-" * 30)
    print("      • Para reduzir o erro padrão pela metade: necessário 4x mais observações")
    print("      • Para reduzir o erro padrão a 1/3: necessário 9x mais observações")
    print("      • Para reduzir o erro padrão a 1/4: necessário 16x mais observações")
    print()
    
    print("   3. APLICAÇÃO NO TEOREMA CENTRAL DO LIMITE")
    print("   " + "-" * 45)
    print("      O erro padrão da média é crucial para:")
    print("      • Construção de intervalos de confiança")
    print("      • Testes de hipóteses sobre médias populacionais")
    print("      • Determinação do tamanho de amostra necessário")
    print("      • Análise da precisão de estimativas")


# Programa principal - Execução acadêmica estruturada
if __name__ == "__main__":
    print("UNIVERSIDADE - CURSO DE ESTATÍSTICA")
    print("TRABALHO PRÁTICO: ERRO PADRÃO DA MÉDIA EM DISTRIBUIÇÕES NORMAIS")
    print("DATA: AGOSTO DE 2025")
    print("\n" + "=" * 85)
    
    # Execução da resolução principal
    print("INICIANDO RESOLUÇÃO DO EXERCÍCIO PROPOSTO...")
    print()
    resultados_principais = resolver_questao_erro_padrao()
    
    # Análises complementares
    demonstrar_independencia_sigma()
    analise_teorica_avancada()
    
    # Finalização do trabalho
    print("\n" + "=" * 85)
    print("CONCLUSÃO DO TRABALHO ACADÊMICO")
    print("=" * 85)
    print("\n" + "=" * 85)
