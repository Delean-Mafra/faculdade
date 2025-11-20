def obter_valor():
    try:
        r = float(input('Informe o valor em reais(R$): '))
        if r <= 0:
            print('Informe um valor maior que zero')
            return obter_valor()
        return r
    except ValueError:
        print('Informe um valor valido')
        return obter_valor()
r = obter_valor()
us = 5.33
valor_convertido = r / us
print(f'O valor em dolar(US$) da entrega é US${valor_convertido:.2f}')
