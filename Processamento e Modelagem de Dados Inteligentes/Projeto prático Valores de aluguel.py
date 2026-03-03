# Aula Projeto prático: Valores de aluguel


import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import urllib.request


# https://lib.stat.cmu.edu/datasets/boston

# Define features

boston_features = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

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

