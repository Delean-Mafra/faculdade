import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os
from datetime import datetime

print("=" * 70)
print("   ANÁLISE EXPLORATÓRIA - PREVISÃO DE SAÍDA DE FUNCIONÁRIOS")
print("=" * 70)

# Verificar se já existe arquivo de resultados processados
arquivo_resultados = 'resultados_processados.csv'
arquivo_metricas = 'metricas_modelo.txt'

if os.path.exists(arquivo_resultados):
    print(f"\n📁 Arquivo de resultados anterior encontrado: {arquivo_resultados}")
    print(f"   Última modificação: {datetime.fromtimestamp(os.path.getmtime(arquivo_resultados)).strftime('%d/%m/%Y %H:%M:%S')}")
    
    while True:
        opcao = input("\n❓ Deseja:\n   [1] Carregar resultados anteriores\n   [2] Fazer novo processamento\n   Escolha (1 ou 2): ").strip()
        
        if opcao == '1':
            print("\n📂 Carregando resultados anteriores...")
            df_resultados = pd.read_csv(arquivo_resultados)
            print("\n✅ Resultados carregados com sucesso!")
            print(f"\n📊 Total de registros: {len(df_resultados)}")
            print(f"\n🔍 Primeiras linhas dos resultados:")
            print(df_resultados.head(10))
            
            # Mostrar métricas salvas
            if os.path.exists(arquivo_metricas):
                print(f"\n📈 Métricas do modelo anterior:")
                with open(arquivo_metricas, 'r', encoding='utf-8') as f:
                    print(f.read())
            
            print("\n" + "=" * 70)
            print("✅ Processo concluído!")
            print("=" * 70)
            exit()
        elif opcao == '2':
            print("\n🔄 Iniciando novo processamento...")
            break
        else:
            print("❌ Opção inválida! Digite 1 ou 2.")

# 1. CARREGAR OS DADOS
print("\n📥 Carregando dados de treinamento...")
df = pd.read_csv('train.csv')

# 2. EXPLORAÇÃO INICIAL DOS DADOS
print("\n📊 Primeiras 5 linhas do conjunto de dados:")
print(df.head())

print("\n📋 Informações sobre o conjunto de dados:")
print(df.info())

print("\n⚠️ Valores ausentes por coluna:")
print(df.isna().sum())

print(f"\n📐 Dimensões do conjunto de dados: {df.shape[0]} linhas x {df.shape[1]} colunas")

# 3. PREPARAÇÃO DOS DADOS (Codificação One-Hot)
print("\n🔄 Convertendo variáveis categóricas em numéricas...")

# Define quais colunas são categóricas e precisam ser convertidas
colunas_categoricas = ['Escolaridade', 'Genero', 'FicouReserva', 'Cidade']

# Aplica One-Hot Encoding (cria colunas binárias para cada categoria)
# drop_first=True remove uma categoria de referência para evitar multicolinearidade
df_codificado = pd.get_dummies(df, columns=colunas_categoricas, drop_first=True)

print("\n✅ Após codificação One-Hot:")
print(df_codificado.head())
print(f"Novas dimensões: {df_codificado.shape[0]} linhas x {df_codificado.shape[1]} colunas")

# 4. SEPARAÇÃO DE CARACTERÍSTICAS (X) E ALVO (Y)
print("\n🎯 Separando características (X) e alvo (y)...")

# X = todas as colunas exceto o alvo que queremos prever
X = df_codificado.drop(columns='VaiSair')

# y = apenas a coluna alvo (o que queremos prever: vai sair ou não?)
y = df_codificado['VaiSair']

print(f"Características (X): {X.shape[1]} colunas")
print(f"Alvo (y): {y.shape[0]} valores")

# 5. DIVISÃO EM CONJUNTOS DE TREINO E TESTE
print("\n✂️ Dividindo dados em treino (70%) e teste (30%)...")

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, 
    test_size=0.3,  # 30% dos dados para teste
    random_state=58  # Garante reprodutibilidade dos resultados
)

print(f"Treino: {X_treino.shape[0]} amostras")
print(f"Teste: {X_teste.shape[0]} amostras")

# 6. TREINAMENTO DO MODELO
print("\n🤖 Treinando modelo de Regressão Logística...")

modelo = LogisticRegression(max_iter=1000)  # max_iter para garantir convergência
modelo.fit(X_treino, y_treino)

print("✅ Modelo treinado com sucesso!")

# 7. PREVISÕES E AVALIAÇÃO
print("\n🔮 Fazendo previsões no conjunto de teste...")

y_previsao = modelo.predict(X_teste)

# Calcula a acurácia (porcentagem de acertos)
acuracia = accuracy_score(y_teste, y_previsao)

print("\n" + "=" * 70)
print(f"🎯 ACURÁCIA DO MODELO: {acuracia * 100:.2f}%")
print("=" * 70)

# 8. ANÁLISE ADICIONAL
print("\n📊 Distribuição das previsões:")
print(f"   • Funcionários que vão sair (1): {sum(y_previsao)}")
print(f"   • Funcionários que vão ficar (0): {len(y_previsao) - sum(y_previsao)}")

print("\n📊 Distribuição real (valores verdadeiros):")
print(f"   • Funcionários que saíram (1): {sum(y_teste)}")
print(f"   • Funcionários que ficaram (0): {len(y_teste) - sum(y_teste)}")

# 9. SALVAR RESULTADOS EM ARQUIVO CSV
print("\n💾 Salvando resultados do processamento...")

# Obter data e hora atual do processamento
data_hora_processamento = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# Criar DataFrame com os resultados do teste
df_resultados = X_teste.copy()
df_resultados['VaiSair_Real'] = y_teste.values
df_resultados['VaiSair_Previsto'] = y_previsao
df_resultados['Previsao_Correta'] = (y_teste.values == y_previsao)

# Resetar índice para facilitar visualização
df_resultados = df_resultados.reset_index(drop=True)

# Adicionar colunas no início
df_resultados.insert(0, 'Data_Hora_Processamento', data_hora_processamento)
df_resultados.insert(1, 'ID_Amostra', range(1, len(df_resultados) + 1))

# Salvar em CSV
df_resultados.to_csv(arquivo_resultados, index=False, encoding='utf-8-sig')
print(f"✅ Resultados salvos em: {arquivo_resultados}")

# Salvar métricas em arquivo texto
with open(arquivo_metricas, 'w', encoding='utf-8') as f:
    f.write("=" * 70 + "\n")
    f.write(f"   RELATÓRIO DE MÉTRICAS DO MODELO\n")
    f.write(f"   Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    f.write("=" * 70 + "\n\n")
    
    f.write(f"🎯 ACURÁCIA DO MODELO: {acuracia * 100:.2f}%\n\n")
    
    f.write("📊 DADOS DE TREINAMENTO:\n")
    f.write(f"   • Total de amostras: {len(df)}\n")
    f.write(f"   • Amostras de treino: {X_treino.shape[0]} (70%)\n")
    f.write(f"   • Amostras de teste: {X_teste.shape[0]} (30%)\n")
    f.write(f"   • Número de características: {X.shape[1]}\n\n")
    
    f.write("📊 RESULTADOS NO CONJUNTO DE TESTE:\n")
    f.write(f"   • Previsões corretas: {sum(y_teste.values == y_previsao)}\n")
    f.write(f"   • Previsões incorretas: {sum(y_teste.values != y_previsao)}\n\n")
    
    f.write("📊 DISTRIBUIÇÃO DAS PREVISÕES:\n")
    f.write(f"   • Funcionários que vão sair (1): {sum(y_previsao)}\n")
    f.write(f"   • Funcionários que vão ficar (0): {len(y_previsao) - sum(y_previsao)}\n\n")
    
    f.write("📊 DISTRIBUIÇÃO REAL:\n")
    f.write(f"   • Funcionários que saíram (1): {sum(y_teste)}\n")
    f.write(f"   • Funcionários que ficaram (0): {len(y_teste) - sum(y_teste)}\n\n")
    
    f.write("🔍 CARACTERÍSTICAS UTILIZADAS:\n")
    for i, col in enumerate(X.columns, 1):
        f.write(f"   {i}. {col}\n")

print(f"✅ Métricas salvas em: {arquivo_metricas}")

# Mostrar resumo dos resultados salvos
print(f"\n📋 Resumo dos resultados salvos ({len(df_resultados)} registros):")
print(df_resultados.head(10))

print(f"\n📊 Estatísticas das previsões:")
print(f"   • Acertos: {sum(df_resultados['Previsao_Correta'])} ({sum(df_resultados['Previsao_Correta'])/len(df_resultados)*100:.1f}%)")
print(f"   • Erros: {sum(~df_resultados['Previsao_Correta'])} ({sum(~df_resultados['Previsao_Correta'])/len(df_resultados)*100:.1f}%)")

print("\n" + "=" * 70)
print("✅ Análise concluída!")
print(f"📁 Arquivos gerados:")
print(f"   • {arquivo_resultados} - Resultados detalhados")
print(f"   • {arquivo_metricas} - Métricas do modelo")
print("=" * 70)

