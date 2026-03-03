# Aula Projeto prático: Valores de aluguel


import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import urllib.request
import matplotlib.pyplot as plt
import seaborn as sns  


# https://lib.stat.cmu.edu/datasets/boston

# Define features

boston_features = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

dados_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'

dir_local, hearder = urllib.request.urlretrieve(dados_url)



boston = pd.read_csv(dir_local, delimiter=r'\s+', names=boston_features)

boston.describe()

boston.corr()

boston.head()

boston.tail()

X = boston.iloc[:,:-1] # dados para  otreinamento

y = boston.iloc[:,-1]  # dados para  otreinamento

# Divisão dos dados em treino e teste

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo_gb = GradientBoostingRegressor()

modelo_gb.fit(X_train, y_train)


score = modelo_gb.score(X_test, y_test)

print("Score do modelo:", score)

# Prática de Machine Learning


# Previsão

# CRIM--ZN--INDUS--CHAS--NOX--RM--AGE--DIS--RAD--TAX--PTRATIO--B--LSTAT--MEDV
dados_entrada = [0.1, 20, 6.0, 0, 0.4, 6, 60, 4.4000, 18, 350, 12, 5, 10.0]
previsao = modelo_gb.predict([dados_entrada])

# visualização do resultado
print("Valor previsto para o aluguel:", previsao[0])


# Coleta de dados para Data Storytelling
mascara = np.zeros_like(boston.corr())
triangle_indices = np.triu_indices(mascara.shape[0])
mascara[triangle_indices] = True

plt.figure(figsize=(16,10))
sns.heatmap(boston.corr(), mask=mascara, annot=True, annot_kws={"size":14})
sns.set_style('white')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()



sns.set()
sns.set_context('talk')
sns.set_style('whitegrid')
sns.jointplot(x= boston['DIS'], y=boston['NOX'],size = 7, color = 'indigo', joint_kws={'alpha':0.5})
plt.show()



sns.set()
sns.set_context('talk')
sns.set_style('whitegrid')
sns.jointplot(x=boston['TAX'], y=boston['RAD'], height=7, color='darkred', joint_kws={'alpha':0.5})
plt.show()



sns.set()
sns.set_context('talk')
sns.set_style('whitegrid')
sns.jointplot(x=boston['DIS'], y=boston['NOX'], kind='hex', height=7, color='blue')
plt.show()



# Coleração entre as variáveis


sns.set()
sns.set_context('talk')
sns.set_style('whitegrid')
sns.jointplot(x=boston['AGE'], y=boston['MEDV'], kind='hex', height=7, color='blue')
plt.show()




sns.set()
sns.set_context('talk')
sns.set_style('whitegrid')
sns.jointplot(x=boston['PTRATIO'], y=boston['MEDV'], kind='hex', height=7, color='blue')
plt.show()




sns.lmplot(x='MEDV', y='RAD', data=boston, height=7)
plt.show()


sns.lmplot(x='TAX', y='RAD', data=boston, height=7)
plt.show()


sns.lmplot(x='RAD', y='MEDV', data=boston, height=7)
plt.show()


sns.lmplot(x='PTRATIO', y='MEDV', data=boston, height=7)
plt.show()


boston_menor_45 = boston.loc[boston['MEDV'] < 45]


filtro = boston.loc[(boston['MEDV'] > 45) & (boston['PTRATIO'] > 14)]


sns.lmplot(x='PTRATIO', y='MEDV', data=filtro, height=7)
plt.show()


rm_medv_corr = round(boston['RM'].corr(boston['MEDV']), 3)
print("Correlação entre RM e MEDV:", rm_medv_corr)

plt.figure(figsize=(9,6))
plt.scatter(x=boston['RM'], y=boston['MEDV'], alpha=0.6, s=80, color='skyblue')

plt.title(f'N de Quartos vs PREÇO (Correlação {rm_medv_corr})', fontsize=14)
plt.xlabel('RM - Mediano de Quartos', fontsize=14)
plt.ylabel('PREÇO - Preço da propriedade em milhares de dólares', fontsize=14)

