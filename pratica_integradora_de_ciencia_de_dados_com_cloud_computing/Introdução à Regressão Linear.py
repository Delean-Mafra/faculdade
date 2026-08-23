import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Ler CSV com separador de ponto e vírgula
df = pd.read_csv('dadosAuda7.csv', sep=';')

# Limpar e converter os dados corretamente
# Volume_Negociacoes: remover pontos (separadores de milhar) e converter para int
df['Volume_Negociacoes'] = df['Volume_Negociacoes'].str.replace('.', '', regex=False).astype(int)

# Preco_Acao: já está no formato correto (100.00), apenas converter para float
df['Preco_Acao'] = df['Preco_Acao'].astype(float)

print("Dados carregados e limpos:")
print(df.head())
print(f"\nColunas disponíveis: {df.columns.tolist()}")
print(f"\nTipos de dados:\n{df.dtypes}")

x = df[['Volume_Negociacoes']]
y = df['Preco_Acao']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("\n" + "="*50)
print("CONJUNTOS DE TREINO E TESTE")
print("="*50)
print(f"\nDados de treino (X): {len(x_train)} amostras")
print(x_train)
print(f"\nDados de teste (X): {len(x_test)} amostras")
print(x_test)
print(f"\nPreços de treino (y): {len(y_train)} amostras")
print(y_train)
print(f"\nPreços de teste (y): {len(y_test)} amostras")
print(y_test)

print("\n" + "="*50)
print("TREINAMENTO DO MODELO DE REGRESSÃO LINEAR")
print("="*50)

modelo_regressao = LinearRegression()
modelo_regressao.fit(x_train, y_train)

coef_incli = modelo_regressao.coef_[0]
inter = modelo_regressao.intercept_

print(f"\n📊 Coeficiente Angular (inclinação): {coef_incli:.10f}")
print(f"📊 Intercepto: {inter:.2f}")
print(f"\n📈 Equação da reta: Preco_Acao = {coef_incli:.10f} * Volume_Negociacoes + {inter:.2f}")

prev = modelo_regressao.predict(x_test)
mse = mean_squared_error(y_test, prev)
r2 = r2_score(y_test, prev)

print("MSE = ", mse)
print("R² = ", r2)
