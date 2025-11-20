# programa convertor de temperatura
celsius = float(input  ('Informe a temperatura: '))
fahrenheit = (celsius * 9/5) + 32
print(f'A temperatura de {celsius}°C corresponde a {fahrenheit}°F')

# Função para converter Celsius para Fahrenheit
def converter_c_para_f(celsius):
    return (celsius * 9 / 5) + 32

# Programa principal
print("Conversor de Temperatura: ºC para ºF")
try:
    c = float(input("Digite a temperatura em Celsius: "))
    f = converter_c_para_f(c)
    print("Temperatura em ºF:", round(f, 2), "ºF")
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
