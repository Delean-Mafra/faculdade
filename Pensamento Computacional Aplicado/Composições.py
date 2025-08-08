# Exemplo 1: Motor e Carro

class Motor:
    def ligar(self):
        print("Motor ligado.")

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar_carro(self):
        self.motor.ligar()
        print("Carro ligado.")

if __name__ == "__main__":
    carro = Carro()
    carro.ligar_carro()

# Exemplo 2: Coração e Corpo

class Coracao:
    def bater(self):
        print("Coração batendo.")

class Corpo:
    def __init__(self):
        self.coracao = Coracao()

    def viver(self):
        self.coracao.bater()
        print("Corpo está vivo.")

if __name__ == "__main__":
    corpo = Corpo()
    corpo.viver()

# Exemplo 3: PlacaMae e Computador

class PlacaMae:
    def iniciar(self):
        print("Placa-mãe iniciada.")

class Computador:
    def __init__(self):
        self.placa_mae = PlacaMae()

    def ligar(self):
        self.placa_mae.iniciar()
        print("Computador ligado.")

computador = Computador()
computador.ligar()

# Exemplo 4: Departamento e Empresa

class Departamento:
    def __init__(self, nome):
        self.nome = nome

class Empresa:
    def __init__(self):
        self.departamentos = [Departamento("RH"), Departamento("TI")]
    
    def mostrar_departamentos(self):
        for departamento in self.departamentos:
            print(departamento.nome)

empresa = Empresa()
empresa.mostrar_departamentos()

# Composição por atribuição direta
class Motor:
    def __init__(self, modelo_motor):
        self.modelo = modelo_motor

class Carro:
    def __init__(self, modelo_motor):
        self.motor = Motor(modelo_motor)

# Exemplo de uso
carro = Carro("V8")
print(carro.motor.modelo)

# Composição por criação interna
class Motor:
    def __init__(self, modelo):
        self.modelo = modelo
    
    def get_modelo(self):
        return self.modelo

class Carro:
    def __init__(self):
        self.iniciar_motor()
    
    def iniciar_motor(self):
        self.motor = Motor("V8")
    
    def get_motor(self):
        return self.motor

# Composição por interface
from abc import ABC, abstractmethod

class Motor(ABC):
    @abstractmethod
    def get_modelo(self):
        pass

class MotorV8(Motor):
    def __init__(self):
        self.modelo = "V8"
    
    def get_modelo(self):
        return self.modelo

class Carro:
    def __init__(self, motor):
        self.motor = motor
    
    def get_motor(self):
        return self.motor

motor = MotorV8()
carro = Carro(motor)

# Composição por inicialização tardia
class Motor:
    def __init__(self, modelo):
        self.modelo = modelo
    
    def get_modelo(self):
        return self.modelo

class Carro:
    def __init__(self):
        self.motor = None
    
    def get_motor(self):
        if self.motor is None:
            self.motor = Motor("V8")
        return self.motor

# Composição por injeção de dependência
from dataclasses import dataclass
from typing import Optional

@dataclass
class Motor:
    modelo: str = "V8"
    
    def get_modelo(self):
        return self.modelo

@dataclass
class Carro:
    motor: Motor
    
    def get_motor(self):
        return self.motor

# Exemplo de lista heterogênea em Python
# Em Python, listas podem naturalmente conter diferentes tipos de dados
heterogeneo = []
heterogeneo.append("texto")
heterogeneo.append(5)
heterogeneo.append(3.14)
heterogeneo.append(True)

# Iterando sobre a lista heterogênea
for item in heterogeneo:
    print(item)

# Exemplo de dicionário heterogêneo em Python
# Em Python, usamos dict ao invés de HashMap
heterogeneo = {}
heterogeneo["texto"] = 42        # String -> int
heterogeneo[3.14] = True        # float -> bool
heterogeneo["A"] = "Caractere"  # String -> String

# Iterando sobre o dicionário heterogêneo
for chave, valor in heterogeneo.items():
    print(f"{chave} : {valor}")

# Classe Item em Python
class Item:
    def __init__(self, nome: str, quantidade: int, preco: float):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def __str__(self) -> str:
        return f"Item[nome='{self.nome}', quantidade={self.quantidade}, preco={self.preco}]"

# Exemplos de uso
item1 = Item("Maçã", 10, 2.99)
item2 = Item("Laranja", 5, 1.99)
print(item1)
print(item2)

# Classe Par genérica usando TypeVar do Python
from typing import TypeVar, Generic

K = TypeVar('K')  # Tipo genérico para chave
V = TypeVar('V')  # Tipo genérico para valor

class Par(Generic[K, V]):
    def __init__(self, chave: K, valor: V):
        self.chave = chave
        self.valor = valor
    
    def get_chave(self) -> K:
        return self.chave
    
    def get_valor(self) -> V:
        return self.valor
    
    def __str__(self) -> str:
        return f"Par[chave={self.chave}, valor={self.valor}]"

# Exemplos de uso com diferentes tipos
par1 = Par[str, int]("idade", 30)
par2 = Par[str, float]("peso", 68.5)
par3 = Par[int, bool](1, True)

print(par1)
print(par2)
print(par3)

# Interface Animal usando ABC (Abstract Base Class)
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Latido")

class Gato(Animal):
    def emitir_som(self):
        print("Miau")

# Exemplo com lista de animais
animais = []  # Em Python, usamos lista normal ao invés de ArrayList
animais.append(Cachorro())
animais.append(Gato())

# Iterando sobre a lista de animais
for animal in animais:
    animal.emitir_som()

# Exemplo de matriz heterogênea
matriz = [
    ["texto", 42],
    [1.5, True],
    ["A", "Caractere"]
]

# Iterando sobre a matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # Nova linha após cada linha da matriz

# Exemplo de lista com diferentes tipos de dados
lista = []  # Em Python, usamos lista built-in ao invés de ArrayList
lista.append("A")
lista.append(3.14)
lista.append(True)

# Iterando sobre a lista
for item in lista:
    print(item)

# Exemplo record Pessoa convertido para Python
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    altura: float
    empregado: bool

if __name__ == "__main__":
    pessoa = Pessoa("Alice", 30, 1.65, True)
    print(pessoa.nome)
    print(pessoa.idade)
    print(pessoa.altura)
    print(pessoa.empregado)

# Definindo uma lista heterogênea
dados = [
    {"nome": "João", "idade": 30, "salario": 5000.0},
    {"nome": "Maria", "idade": 25, "salario": 6000.0},
    {"nome": "Pedro", "idade": 35, "salario": 7000.0}
]

# Função para calcular a média dos salários
def calcular_media_salarios(dados):
    total_salario = sum(item["salario"] for item in dados)
    return total_salario / len(dados)

# Função para encontrar a pessoa mais velha
def encontrar_mais_velho(dados):
    return max(dados, key=lambda x: x["idade"])

# Função para aumentar o salário de todos em uma porcentagem
def aumentar_salarios(dados, porcentagem):
    for item in dados:
        item["salario"] += item["salario"] * (porcentagem / 100)

# Exibindo os dados originais
print("Dados originais:")
for item in dados:
    print(item)

# Calculando a média dos salários
media_salarios = calcular_media_salarios(dados)
print(f"Média dos salários: {media_salarios:.2f}")

# Encontrando a pessoa mais velha
mais_velho = encontrar_mais_velho(dados)
print(f"Pessoa mais velha: {mais_velho['nome']} ({mais_velho['idade']} anos)")

# Aumentando os salários em 10%
aumentar_salarios(dados, 10)

# Exibindo os dados após o aumento de salário
print("\nDados após o aumento de salário:")
for item in dados:
    print(item)

# Exemplo de classe com acesso direto aos atributos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Alice", 30)
print(pessoa.nome)   # Acessa diretamente o atributo 'nome'
print(pessoa.idade)  # Acessa diretamente o atributo 'idade'

# Exemplo de classe com getters e setters usando property
class Pessoa:
    def __init__(self, nome):
        self._nome = nome
    
    # Getter para nome
    @property
    def nome(self):
        return self._nome
    
    # Setter para nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

# Exemplo de classe com método de exibição de informações
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

pessoa = Pessoa("João", 30)
pessoa.mostrar_info()

# Exemplo de classe com propriedade somente leitura
class Circulo:
    def __init__(self, raio):
        self._raio = raio
    
    @property
    def raio(self):
        return self._raio
    
    @property
    def area(self):
        return 3.14159 * (self._raio ** 2)

# Uso
c = Circulo(5)
print(c.raio)  # Acessa o raio
# c.raio = 10  # Isso geraria um erro, pois não há setter
print(c.area)  # Calcula a área com base no raio inicial

# Exemplo de método estático e atributo de classe
class Exemplo:
    contador = 0

    @staticmethod
    def incrementar_contador():
        Exemplo.contador += 1

# Uso
Exemplo.incrementar_contador()
print(Exemplo.contador)  # Saída: 1

# Exemplo de composição de objetos
class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

endereco = Endereco("Rua A", "Cidade B")
pessoa = Pessoa("João", endereco)

print(pessoa.endereco.rua)  # Acessando subobjeto



