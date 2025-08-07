

from abc import ABC, abstractmethod

# Aula 1

# Herança em Python
class Aeronave:
    def decolar(self):
        print("Aeronave está decolando.")

class Aviao(Aeronave):
    def servir_refeicao(self):
        print("Servindo refeição aos passageiros.")


# Outra classe derivada de Aeronave
class Helicoptero(Aeronave):
    def pairar(self):
        print("O Helicóptero está pairando no ar.")

# Classe base
class InstrumentoMusical:
    def __init__(self, nome):
        self.nome = nome
    def tocar(self):
        print(f"O {self.nome} está tocando.")

# Subclasse Guitarra
class Guitarra(InstrumentoMusical):
    def __init__(self, nome, numero_de_cordas):
        super().__init__(nome)
        self.numero_de_cordas = numero_de_cordas
    def afinar(self):
        print(f"Afinando a guitarra com {self.numero_de_cordas} cordas.")

# Subclasse Piano
class Piano(InstrumentoMusical):
    def __init__(self, nome, numero_de_teclas):
        super().__init__(nome)
        self.numero_de_teclas = numero_de_teclas
    def abrir_tampa(self):
        print(f"Abrindo a tampa do piano com {self.numero_de_teclas} teclas.")



# Código para testar
guitarra = Guitarra("Guitarra Fender", 6)
piano = Piano("Piano Yamaha", 88)

guitarra.tocar()   # Saída: O Guitarra Fender está tocando.
guitarra.afinar()  # Saída: Afinando a guitarra com 6 cordas.
piano.tocar()      # Saída: O Piano Yamaha está tocando.

# Aula 2

# Classe abstrata em Python
class Turismo(ABC):
    @abstractmethod
    def planejar_viagem(self):
        pass

    @abstractmethod
    def reservar_hotel(self):
        pass

