from turtle import color
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


# Ler CSV com separador de ponto e vírgula e remover espaços extras
df = pd.read_csv('dadosAuda8.csv', sep=';', skipinitialspace=True)

print("Dados carregados:")
print(df.head())
print(f"\nColunas disponíveis: {df.columns.tolist()}")
print(f"\nTipos de dados:\n{df.dtypes}\n")

x = df[['Horas_de_Jogo']]
y = df['Pontuacao']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


print("="*50)
print("TREINAMENTO DO MODELO")
print("="*50)

modelo = LinearRegression()
modelo.fit(x_train, y_train)

print(f"\n✅ Modelo treinado com sucesso!")
print(f"📊 Coeficiente Angular: {modelo.coef_[0]:.4f}")
print(f"📊 Intercepto: {modelo.intercept_:.4f}")
print(f"📈 Equação: Pontuacao = {modelo.coef_[0]:.4f} * Horas_de_Jogo + {modelo.intercept_:.4f}")

print("\n" + "="*50)
print("AVALIAÇÃO DO MODELO")
print("="*50)

y_prev = modelo.predict(x_test)
mse = mean_squared_error(y_test, y_prev)
r2 = r2_score(y_test, y_prev)

print(f"\n📉 MSE (Erro Quadrático Médio): {mse:.2f}")
print(f"📊 R² Score (Coeficiente de Determinação): {r2:.4f}")

print("\n" + "="*50)
print("COMPARAÇÃO: VALORES REAIS vs PREVISTOS")
print("="*50)
print("\nDados de teste:")
comparacao = pd.DataFrame({
    'Horas_de_Jogo': x_test['Horas_de_Jogo'].values,
    'Pontuacao_Real': y_test.values,
    'Pontuacao_Prevista': y_prev.round(2),
    'Diferenca': (y_test.values - y_prev).round(2)
})
print(comparacao.to_string(index=False))

print("\n" + "="*50)
print("INTERPRETAÇÃO DOS RESULTADOS")
print("="*50)
if r2 < 0:
    print("\n⚠️  R² negativo indica que o modelo está muito ruim!")
    print("    Isso significa que usar apenas 'Horas_de_Jogo' não é suficiente")
    print("    para prever a pontuação. O modelo está pior que usar a média.")
    print("\n💡 Sugestão: Tente usar múltiplas variáveis (regressão múltipla):")
    print("    - Nível_Experiencia")
    print("    - Tempo_Online")
    print("    - Combinação de todas as features")
elif r2 < 0.5:
    print("\n⚠️  R² baixo - modelo fraco. Considere adicionar mais variáveis.")
elif r2 < 0.8:
    print("\n✅ R² moderado - modelo razoável, mas pode melhorar.")
else:
    print("\n🎉 R² alto - modelo muito bom!")


print("\n" + "="*50)
print("GRÁFICO DE RESÍDUOS")
print("="*50)

residuos = y_test - y_prev

# Criar figura com subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: Resíduos vs Valores Previstos
axes[0].scatter(y_prev, residuos, color='red', alpha=0.6, edgecolors='black', s=100)
axes[0].axhline(y=0, color='blue', linestyle='--', linewidth=2, label='Linha de base (erro = 0)')
axes[0].set_xlabel('Valores Previstos (Pontuação)', fontsize=12)
axes[0].set_ylabel('Resíduos (Erro)', fontsize=12)
axes[0].set_title('Resíduos vs Valores Previstos', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Gráfico 2: Valores Reais vs Valores Previstos
axes[1].scatter(y_test, y_prev, color='green', alpha=0.6, edgecolors='black', s=100, label='Dados')
# Linha diagonal perfeita (onde real = previsto)
min_val = min(y_test.min(), y_prev.min())
max_val = max(y_test.max(), y_prev.max())
axes[1].plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Previsão perfeita')
axes[1].set_xlabel('Valores Reais (Pontuação)', fontsize=12)
axes[1].set_ylabel('Valores Previstos (Pontuação)', fontsize=12)
axes[1].set_title('Real vs Previsto', fontsize=14, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n📊 Gráficos gerados com sucesso!")


plt.hist(residuos, color='green')

plt.xlabel('Residuos')
plt.ylabel('freq')
plt.title('Histograma')
plt.show()


# import statsmodels.api as sm


# sm.qqplot(residuos, line='s')
# plt.show()

print("\n" + "="*50)
print("EXEMPLO 1: REGRESSÃO MÚLTIPLA")
print("Prevendo 'Pontuacao' usando TODAS as features")
print("="*50)

x = df[['Horas_de_Jogo', 'Tempo_Online', 'Nível_Experiencia']]
y = df['Pontuacao']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
modelo_multiplo = LinearRegression()
modelo_multiplo.fit(x_train, y_train)

y_prev_multiplo = modelo_multiplo.predict(x_test)
mse_multiplo = mean_squared_error(y_test, y_prev_multiplo)
r2_multiplo = r2_score(y_test, y_prev_multiplo)

print(f"\n✅ Modelo Múltiplo treinado!")
print(f"📉 MSE: {mse_multiplo:.2f}")
print(f"📊 R² Score: {r2_multiplo:.4f}")
print(f"\n📈 Coeficientes:")
for feature, coef in zip(x.columns, modelo_multiplo.coef_):
    print(f"   {feature}: {coef:.4f}")
print(f"   Intercepto: {modelo_multiplo.intercept_:.4f}")


print("\n" + "="*50)
print("EXEMPLO 2: REGRESSÃO MÚLTIPLA")
print("Prevendo 'Nível_Experiencia' usando Horas e Tempo")
print("="*50)

x = df[['Horas_de_Jogo', 'Tempo_Online']]
y = df['Nível_Experiencia']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
modelo2 = LinearRegression()
modelo2.fit(x_train, y_train)

y_prev2 = modelo2.predict(x_test)
mse2 = mean_squared_error(y_test, y_prev2)
r2_2 = r2_score(y_test, y_prev2)

print(f"\n✅ Modelo 2 treinado!")
print(f"📉 MSE: {mse2:.2f}")
print(f"📊 R² Score: {r2_2:.4f}")


print("\n" + "="*50)
print("EXEMPLO 3: REGRESSÃO SIMPLES")
print("Prevendo 'Nível_Experiencia' usando apenas Horas")
print("="*50)

x = df[['Horas_de_Jogo']]
y = df['Nível_Experiencia']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
modelo3 = LinearRegression()
modelo3.fit(x_train, y_train)

y_prev3 = modelo3.predict(x_test)
mse3 = mean_squared_error(y_test, y_prev3)
r2_3 = r2_score(y_test, y_prev3)

print(f"\n✅ Modelo 3 treinado!")
print(f"📉 MSE: {mse3:.2f}")
print(f"📊 R² Score: {r2_3:.4f}")

print("\n" + "="*50)
print("COMPARAÇÃO DOS MODELOS")
print("="*50)
print(f"\n📊 Modelo 1 (Múltiplo - 3 features → Pontuacao):")
print(f"   MSE: {mse_multiplo:.2f} | R²: {r2_multiplo:.4f}")
print(f"\n📊 Modelo 2 (Múltiplo - 2 features → Nível_Experiencia):")
print(f"   MSE: {mse2:.2f} | R²: {r2_2:.4f}")
print(f"\n📊 Modelo 3 (Simples - 1 feature → Nível_Experiencia):")
print(f"   MSE: {mse3:.2f} | R²: {r2_3:.4f}")





print("\n✨ Script finalizado com sucesso!")

