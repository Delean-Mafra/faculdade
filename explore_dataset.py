import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("=" * 70)
print("   ANÁLISE EXPLORATÓRIA - PREVISÃO DE SAÍDA DE FUNCIONÁRIOS")
print("=" * 70)

# 1. CARREGAR OS DADOS
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

print("\n" + "=" * 70)
print("✅ Análise concluída!")
print("=" * 70)
