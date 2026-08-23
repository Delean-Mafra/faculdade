def soma(a, b):
    return a + b

def imprimir_numero(numero):
    print("O número é:", numero)

meu_numero = 25
# Chamando a função e passando o parâmetro
imprimir_numero(meu_numero)

def inverter_string(s):
    if len(s) == 0:
        return s
    else:
        return inverter_string(s[1:]) + s[0]

texto = "ab"
resultado = inverter_string(texto)
print(f"A string invertida de '{texto}' é '{resultado}'")

def somatorio(n):
    if n == 1:
        return 1
    else:
        return n + somatorio(n - 1)

numero = 5
resultado = somatorio(numero)
print(f"O somatório de 1 até {numero} é {resultado}")

class Calculadora:
    def somar(self, a, b, c=0):
        return a + b + c

calc = Calculadora()

print("Soma de 2 inteiros:", calc.somar(10, 20))
print("Soma de 3 inteiros:", calc.somar(10, 20, 30))
