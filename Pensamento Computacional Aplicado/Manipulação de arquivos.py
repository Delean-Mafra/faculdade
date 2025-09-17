import os
import pickle



# Dados para serializar
dados = {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}

# Serialização
with open('dados.pickle', 'wb') as arquivo:
    pickle.dump(dados, arquivo)

# Definindo o caminho do arquivo
caminho_do_arquivo = 'dados.pickle'

# Abrindo e lendo o arquivo
with open(caminho_do_arquivo, 'rb') as arquivo:
    conteudo = pickle.load(arquivo)

# Desserialização
with open('dados.pickle', 'rb') as arquivo:
    dados_carregados = pickle.load(arquivo)

print(dados_carregados)

# Caminho relativo do arquivo
caminho_relativo = "dados.pickle"

# Verifica se o arquivo existe
if os.path.exists(caminho_relativo):
    # Retorna o tamanho do arquivo
    tamanho = os.path.getsize(caminho_relativo)
    print(f"O arquivo existe e tem {tamanho} bytes.")
else:
    print("O arquivo não existe.")



print(conteudo)

# Dicionário original com informações turísticas
dados_turisticos = {
    'cidade': 'Rio de Janeiro',
    'pontos_turisticos': ['Cristo Redentor', 'Pão de Açúcar', 'Praia de Copacabana'],
    'atividades_recomendadas': ['Trilha', 'Mergulho', 'Passeio de barco']
}

# Serialização do dicionário
dados_serializados = pickle.dumps(dados_turisticos)

# Desserialização do dicionário
dados_desserializados = pickle.loads(dados_serializados)

# Impressão dos dados para comparação
print("Dados Originais:", dados_turisticos)

print("Dados Serializados:", dados_serializados)

print("Dados Desserializados:", dados_desserializados)

import pickle

class CarroClassico:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
    
    def __str__(self):
        return f'CarroClassico(modelo={self.modelo}, ano={self.ano})'

def serializar_carros():
    carro1 = CarroClassico("Ford Mustang", 1967)
    carro2 = CarroClassico("Chevrolet Camaro", 1969)
    with open('carros_classicos.pkl', 'wb') as file:
        pickle.dump([carro1, carro2], file)
    print("Objetos foram serializados e salvos em carros_classicos.pkl")

serializar_carros()

def desserializar_carros():
    with open('carros_classicos.pkl', 'rb') as file:
        carros = pickle.load(file)
    print("Objetos foram desserializados:")
    for carro in carros:
        print(carro)

desserializar_carros()

