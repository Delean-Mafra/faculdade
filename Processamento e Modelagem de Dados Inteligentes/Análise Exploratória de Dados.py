import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns

# Load the diamonds dataset from seaborn
df_diamantes = sns.load_dataset('diamonds')
print(df_diamantes.shape)
print(df_diamantes.head())
print(df_diamantes.tail())
print(df_diamantes.describe())

print(df_diamantes[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].corr())

df_diamantes_grouped = df_diamantes[['carat', 'depth', 'table', 'price']].groupby('carat').agg(['mean', 'min', 'max'])
print(df_diamantes_grouped)

df_diamantes.sample(3)

print(df_diamantes.dtypes)

print(df_diamantes.columns)

print(df_diamantes.nunique())

print(df_diamantes.isnull().sum())
print(df_diamantes.info())

# Trenamento do modelo

X = df_diamantes[['carat','depth','table','x','y','z']]  # variáveis independentes
y = df_diamantes['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Avaliação do modelo:')
print(f"MSE: {mse:.2f}")
print(f"R²: {r2}")

novo_diamante = pd.DataFrame({
    'carat': [0.9,1.2,2.3],
    'depth': [62.1,60.5,63.2],
    'table': [57,63,61],
    'x': [5.1,6.78,8.3],
    'y': [5.15,6.82,8.35],
    'z': [3.18,4.1,5.12]
})


precos_novos_diamantes =  modelo.predict(novo_diamante)

print('O preço para os 3 diaamntes é:', precos_novos_diamantes)
contador = 1

for preco in precos_novos_diamantes:
    print(f'O preço previsto para o diamante{contador} é', preco)
    contador = contador + 1

