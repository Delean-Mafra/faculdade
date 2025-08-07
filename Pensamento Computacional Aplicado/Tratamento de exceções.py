try:
    resultado = 10 / 5
    print(resultado)

    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError as e:
    print(f"Erro: {e}")

try:
    with open('arquivo_inexistente.txt', 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError as e:
    print(f"Erro: {e}")

try:
    valor1 = 10
    valor2 = "10"
    print(valor1)
    print(valor2)

    resultado = valor1 + int(valor2)
    print(resultado)

    valor3 = "abc"
    resultado = valor1 + int(valor2) + int(valor3)
except ValueError as e:
    print(f"Erro: {e}")


class CircularListIndexError(Exception):
    def __init__(self, message):
        super().__init__(message)

class CircularList:
    def __init__(self, items):
        self.items = items

    def get_item(self, index):
        if index >= len(self.items) or index < -len(self.items):
            raise CircularListIndexError(f"Índice fora do intervalo: {index}")
        return self.items[index % len(self.items)]

try:
    clist = CircularList([1, 2, 3, 4])
    print(clist.get_item(4))  # Tentativa de acessar índice fora do intervalo
except CircularListIndexError as e:
    print(e)

# Definindo uma nova exceção
class MinhaExcecao(Exception):
    def __init__(self, mensagem, causa=None):
        super().__init__(mensagem)
        self.mensagem = mensagem
        self.causa = causa

    def __str__(self):
        return f"Minha Exceção: {self.mensagem}"

def metodo_que_lanca_excecao():
    try:
        resultado = 10 / 0  # Isso causará uma ZeroDivisionError
    except ZeroDivisionError as e:
        raise MinhaExcecao("Erro ao dividir por zero", e) from e

# Tratamento para ValueError
try:
    valor1 = 10
    valor2 = "10"
    valor3 = "abc"
    resultado = valor1 + int(valor2) + int(valor3)
except ValueError as e:
    print(f"Erro: {e}")

# Tratamento para índice fora do intervalo
try:
    clist = CircularList([1, 2, 3, 4])
    print(clist.get_item(4))
except CircularListIndexError as e:
    print(e)

# Tratamento para exceção customizada com causa
try:
    metodo_que_lanca_excecao()
except MinhaExcecao as e:
    print(f"{e} causado por {e.causa}")

# Definindo a exceção customizada
class CustomException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

try:
    # Código que pode gerar exceções
    pass
except ValueError as e:
    raise CustomException("Erro customizado") from e
except TypeError:
    # Tratamento específico para TypeError
    pass
except Exception as e:
    # Tratamento para outras exceções
    pass





