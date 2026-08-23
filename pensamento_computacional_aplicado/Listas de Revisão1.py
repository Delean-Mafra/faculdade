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

# V. A variável e armazena o valor 15.0?
v = f"V - {v_ou_f(e == 15.0 and type(e) == type(15.0))}"


questao1 = (i, ii, iii, iv, v)

print(questao1)

# Criar dicionário para mapear as afirmativas
afirmativas = {
    'I': isinstance(a, int) and isinstance(b, float),
    'II': isinstance(c, str) and isinstance(d, bool),
    'III': isinstance(a + int(b), int),
    'IV': type(c) == str,
    'V': e == (15.0) and type(e) == type(15.0)
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
