class MinhaClasse:
    def __init__(self):
        self.__atributo_privado = 42

    def mostrar_atributo(self):
        print(self.__atributo_privado)

obj = MinhaClasse()
obj.mostrar_atributo()
print(obj._MinhaClasse__atributo_privado)
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro:
    """
    Classe Carro simplificada.
    """

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando...")

    def virar(self, direcao):
        print(f"Virando para {direcao}...")

    def abastecer(self, litros):
        print(f"Abastecendo {litros} litros...")





class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def dizer_ola(self):
        print(f"Olá, meu nome é {self.nome}")

pessoa1 = Pessoa("Douglas")

pessoa1.dizer_ola()  # Saída: Olá, meu nome é Douglas

# Exemplo de atributos público, protegido e privado
class Exemplo:
    def __init__(self):
        self.publico = "Eu sou público"
        self._protegido = "Eu sou protegido"
        self.__privado = "Eu sou privado"

# Criando uma instância da classe
obj = Exemplo()

print(obj.publico)        # Saída: Eu sou público
print(obj._protegido)     # Saída: Eu sou protegido
print(obj._Exemplo__privado)  # Saída: Eu sou privado

# Exemplo de atributos públicos, protegidos e privados, e métodos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade
        self.__senha = "1234"

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self._idade}")

    def __mostrar_senha(self):
        print(f"Senha: {self.__senha}")

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def mostrar_dados_funcionario(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}.")

func = Funcionario("Douglas", "Desenvolvedor")

print(func.nome)  # Saída: Douglas
print(func.cargo)  # Saída: Desenvolvedor

try:
    print(func.__senha)  # Tentativa de acessar atributo privado
except AttributeError:
    print("Erro: Atributo privado não acessível diretamente")

# print(func.__senha)  # Erro: Atributo privado não acessível diretamente
func.mostrar_dados_funcionario()  # Saída: Nome: Douglas, Cargo: Desenvolvedor.

# Exemplo de método de classe
class Contador:
    contador = 0

    @classmethod
    def incrementar(cls):
        cls.contador += 1

# Chamada de método de classe
Contador.incrementar()
print(Contador.contador)  # Saída: 1

# Exemplo de método de instância e método estático
class MinhaClasse:
    def metodo_instancial(self):
        print("Este é um método de instância")

    @staticmethod
    def metodo_estatico():
        print("Este é um método estático.")

objeto = MinhaClasse()

objeto.metodo_instancial()
# Este é um método de instância

MinhaClasse.metodo_estatico()
# Este é um método estático.

MinhaClasse.metodo_instancial(objeto)





