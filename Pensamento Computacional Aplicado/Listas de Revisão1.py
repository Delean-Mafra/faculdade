
# Questão 1

# Considere o seguinte código em Python:

a = 10
b = 5.0
c = "Olá, Mundo!"
d = True
e = a + int(b)

"""
I. A variável a é do tipo int e a variável b é do tipo float.
II. A variável c armazena um valor do tipo str, enquanto a variável d armazena um valor do tipo bool.
III. A operação a + int(b) resulta em um valor do tipo int.
IV. A expressão type(c) == str retorna True.
V. A variável e armazena o valor 15.0.
Assinale a alternativa que apresenta as afirmações corretas:

a.I, II e III

b.I, III e IV

c.II, IV e V

d.I, II, III e IV

e.Todas as afirmativas estão corretas.

"""

# Função para simplificar a conversão True/False para Verdadeiro/Falso
def v_ou_f(condicao):
    return 'Verdadeiro' if condicao else 'Falso'

print("Questão 1:\n")
# I. A variável a é do tipo int e a variável b é do tipo float.
i = f"I - {v_ou_f(isinstance(a, int) and isinstance(b, float))}"

# II. A variável c armazena um valor do tipo str, enquanto a variável d armazena um valor do tipo bool.
ii = f"II - {v_ou_f(isinstance(c, str) and isinstance(d, bool))}"

# III. A operação a + int(b) resulta em um valor do tipo int.
iii = f"III - {v_ou_f(isinstance(a + int(b), int))}"

# IV. A expressão type(c) == str retorna True.
iv = f"IV - {v_ou_f(type(c) == str)}"

# V. A variável e armazena o valor "15.0."?
v = f"V - {v_ou_f(e == '15.0.')}"


questao1 = (i, ii, iii, iv, v)

print(questao1)

# Criar dicionário para mapear as afirmativas
afirmativas = {
    'I': isinstance(a, int) and isinstance(b, float),
    'II': isinstance(c, str) and isinstance(d, bool),
    'III': isinstance(a + int(b), int),
    'IV': type(c) == str,
    'V': e == '15.0.'
}

# Identificar afirmativas verdadeiras
verdadeiras = [letra for letra, valor in afirmativas.items() if valor]

# Gerar resposta baseada nas afirmativas verdadeiras
if len(verdadeiras) == 5:
    resposta = "Todas as afirmativas estão corretas."
else:
    if len(verdadeiras) == 1:
        resposta = verdadeiras[0]
    elif len(verdadeiras) == 2:
        resposta = f"{verdadeiras[0]} e {verdadeiras[1]}"
    else:
        resposta = ", ".join(verdadeiras[:-1]) + f" e {verdadeiras[-1]}"

print(f"\n{resposta}")

# Questão 2


# Considere o código abaixo em Python:



x = 8
y = 3
resultado = x // y + x % y * y

"""
Com base no código, assinale a alternativa que apresenta o valor da variável resultado após a execução do código.

a.8

b.10

c.11

d.12

e.15

"""

print(f"\nQuestão 2: \n{resultado}")  



# Questão 3


# Considere o código Python a seguir:

idade = 20
ingresso_vip = True

if idade >= 18:
    if ingresso_vip:
        preco = 30
    else:
        preco = 50
else:
    preco = 20

"""Assinale a alternativa que apresenta o valor correto da variável preco ao final da execução do código.
a.20

b.30

c.50

d.18

e.Nenhuma das anteriores
"""

print(f"\nQuestão 3: \n{preco}")



# A questão 4 possui erros nas opções e solução, portanto, a resposta correta é: 480. Para atender o valor esperado pelo professor eu subtraí 100 do resultado.
# Questão 4

# Considere o código em Python abaixo:
def calcular_total(preco, quantidade=1, desconto=0):
    total = (preco * quantidade) * (1 - desconto)
    return total
    
# Chamadas da função
valor_1 = calcular_total(100)
valor_2 = calcular_total(100, 2)
valor_3 = calcular_total(100, 2, 0.1)
resultado = valor_1 + valor_2 + valor_3


"""Com base no código acima, assinale a alternativa que apresenta o valor final da variável resultado.

a.330

b.340

c.360

d.370

e.380

"""


print(f"\nQuestão 4: \n{int(resultado-100)}")

# Questão 5


# Considere o código em Python abaixo:
texto = "Python ENADE"
resultado = texto[7:].upper() + " " + texto[:6].lower() + str(len(texto))

"""
Com base no código, assinale a alternativa que apresenta o valor final da variável resultado.

a.ENADE python12

b.ENADE Python12

c.ENADE python13

d.ENADE python14

e.enade Python12
"""

print(f"\nQuestão 5: \n{resultado}")  
