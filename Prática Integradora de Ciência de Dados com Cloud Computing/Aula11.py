# !pip install tensorflow
import tensorflow as tf
print(tf.__version__)

import matplotlib.pyplot as plt
import yfinance as y
# baixar os dados do yf
def baixar_dados(acao, data_inicio, data_fim):
  dados_acao = yf.download(acao, start=data_inicio, end=data_fim)
  # média movel
  return dados_acao
def modelo_media_movel(dados, tamanho_janela):
  dados['Média Móvel'] = dados['Close'].rolling(window=tamanho_janela).mean()
  return dados
acao = input('informe sua ação: ')
data_inicio = '2020-01-01'
data_fim = '2020-12-31'
tamanho_janela = 20
dados = baixar_dados(acao, data_inicio, data_fim)
dados = modelo_media_movel(dados, tamanho_janela)
plt.plot(dados['Close'], label = 'atual')
plt.plot(dados['Média Móvel'], label = f'média móvel ({tamanho_janela} em dias)')
plt.title(f'preço da ação {acao}')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.show()
