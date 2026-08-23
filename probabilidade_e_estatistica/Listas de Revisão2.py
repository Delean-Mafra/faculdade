"""Problema:
Em um campeonato de futebol participaram 16 times. Quantos resultados são possíveis para os três primeiros lugares?

Raciocínio:
Queremos o número de maneiras distintas (ordenadas) de escolher 1º, 2º e 3º lugares dentre 16 times.
Isso é uma permutação de 16 elementos tomados 3 a 3: P(16,3) = 16 * 15 * 14 = 3360.

Abaixo calculamos de três formas: direta, usando math.perm (Python 3.8+) e conferindo com itertools.permutations.
"""

from math import perm
from itertools import permutations

def resultados_primeiros_tres(times: int, k: int = 3) -> int:
	"""Retorna o número de resultados possíveis (ordem importa) para os k primeiros lugares.

	Fórmula: P(n,k) = n! / (n-k)!  (aqui aplicamos via multiplicação direta para clareza)
	"""
	if k > times or times < 0 or k < 0:
		raise ValueError("Parâmetros inválidos: k deve ser <= times e ambos não negativos.")
	# Cálculo direto iterativo evita usar factorial completo.
	resultado = 1
	for i in range(times, times - k, -1):
		resultado *= i
	return resultado

def main():
	n_times = 16
	k = 3
	calculo_direto = resultados_primeiros_tres(n_times, k)
	calculo_math_perm = perm(n_times, k)  # Usa função da biblioteca padrão
	# Verificação opcional (cuidado: gera lista grande, então só contamos). Aqui não gera lista inteira, apenas conta.
	calculo_itertools = sum(1 for _ in permutations(range(n_times), k))

	print(f"Número de resultados possíveis para os {k} primeiros lugares entre {n_times} times:")
	print(f"  Cálculo direto:      {calculo_direto}")
	print(f"  math.perm:           {calculo_math_perm}")
	print(f"  itertools (contagem): {calculo_itertools}")
	assert calculo_direto == 3360, "Valor esperado 3360"

if __name__ == "__main__":
	main()


# -------------------------------------------------------------
# Segunda questão:
# "A permutação das letras da palavra ROMA são:"
# Vamos gerar todas as permutações distintas (como todas as letras são diferentes,
# teremos 4! = 24 permutações) e exibir.

def permutacoes_palavra(palavra: str) -> list[str]:
	"""Retorna lista com todas as permutações (ordem importa) das letras da palavra."""
	return [''.join(p) for p in permutations(palavra)]

if __name__ == "__main__":  # Reaproveitamos o mesmo guard para executar também esta parte
	palavra = "ROMA"
	perms = permutacoes_palavra(palavra)
	print("\nA permutação das letras da palavra ROMA são:")
	# Exibe em linhas de forma organizada (6 por linha)
	for i, p in enumerate(perms, start=1):
		end_char = "\n" if i % 6 == 0 else "\t"
		print(p, end=end_char)
	if len(perms) % 6 != 0:
		print()  # quebra final se necessário
	print(f"Total de permutações: {len(perms)}")


	# -------------------------------------------------------------
	# Terceira questão:
	# "No lançamento de dois dados a probabilidade de termos soma maior que 8 é?"
	# Vamos calcular todas as combinações possíveis e contar as que têm soma > 8.

	def probabilidade_soma_maior_que_8():
		total = 0
		favoraveis = 0
		for d1 in range(1, 7):
			for d2 in range(1, 7):
				soma = d1 + d2
				total += 1
				if soma > 8:
					favoraveis += 1
		prob = favoraveis / total
		print("\nNo lançamento de dois dados, a probabilidade de termos soma maior que 8 é:")
		print(f"Casos favoráveis: {favoraveis}")
		print(f"Casos possíveis:  {total}")
		print(f"Probabilidade:    {favoraveis}/{total} = {prob:.4f} ({prob*100:.2f}%)")

	if __name__ == "__main__":
		probabilidade_soma_maior_que_8()

		# -------------------------------------------------------------
		# Quarta questão:
		# "A moda de Czuber é um método de estimativa da moda em uma distribuição contínua."
		# Qual das seguintes expressões descreve corretamente o cálculo da moda de Czuber?
		#
		# Fórmula clássica (forma 1):
		#   Moda = L + ((f1 - f0) / (2f1 - f0 - f2)) * h
		# Definindo:
		#   D1 = f1 - f0 (diferença entre a frequência da classe modal e a anterior)
		#   D2 = f1 - f2 (diferença entre a frequência da classe modal e a posterior)
		# Temos a forma (equivalente) usada nas alternativas (forma 2):
		#   Moda = L + (D1 / (D1 + D2)) * h
		# Onde:
		#   L  = limite inferior da classe modal
		#   f1 = frequência da classe modal
		#   f0 = frequência da classe anterior
		#   f2 = frequência da classe posterior
		#   h  = amplitude da classe (largura do intervalo)
		#
		# Ambas as formas geram o mesmo valor. A alternativa correta nas opções dadas é:
		#   Moda = (D1 / (D1 + D2)) * Intervalo de classe + Limite inferior da classe modal

		def moda_czuber(L: float, f0: float, f1: float, f2: float, h: float) -> float:
			"""Calcula a moda de Czuber usando a fórmula original.
			Parâmetros já descritos acima.
			"""
			numerador = (f1 - f0)
			denominador = (2 * f1 - f0 - f2)
			if denominador == 0:
				return float('nan')
			return L + (numerador / denominador) * h

		def moda_czuber_d1d2(L: float, D1: float, D2: float, h: float) -> float:
			"""Calcula a moda usando a forma com D1 e D2."""
			if (D1 + D2) == 0:
				return float('nan')
			return L + (D1 / (D1 + D2)) * h

		if __name__ == "__main__":
			# Exemplo: classe modal [10,15), L=10, h=5, f0=8, f1=15, f2=6
			L, f0, f1, f2, h = 10, 8, 15, 6, 5
			D1 = f1 - f0  # 7
			D2 = f1 - f2  # 9
			moda_forma1 = moda_czuber(L, f0, f1, f2, h)
			moda_forma2 = moda_czuber_d1d2(L, D1, D2, h)
			print("\nModa de Czuber (estimativa para distribuição contínua):")
			print("Forma 1: Moda = L + ((f1 - f0) / (2f1 - f0 - f2)) * h")
			print("Forma 2: Moda = L + (D1 / (D1 + D2)) * h  (equivalente)")
			print(f"Valores: L={L}, f0={f0}, f1={f1}, f2={f2}, h={h}, D1={D1}, D2={D2}")
			print(f"Moda (forma 1): {moda_forma1:.4f}")
			print(f"Moda (forma 2): {moda_forma2:.4f}")
			if abs(moda_forma1 - moda_forma2) < 1e-10:
				print("As duas formas coincidem (OK). Valor final: %.4f" % moda_forma1)
			print("Resposta conceitual: usar as diferenças D1=f1-f0 e D2=f1-f2: Moda = L + (D1/(D1+D2)) * h.")

			# -------------------------------------------------------------
			# Quinta questão:
			# "Quartil é uma medida separatriz que divide um conjunto de dados em 4 partes iguais.
			#  Como você calcularia o 3º quartil (Q3) de um conjunto de dados?"
			#
			# Existem vários métodos aceitos. Dois bem usados:
			#  - Método (Tukey / inclusive): posição p = 0.75 * (n + 1)
			#  - Método (Excel/Minitab recente / exclusive): p = 0.75 * (n - 1) + 1
			# Ambos depois fazem interpolação linear se a posição não é inteira.
			# Aqui implementamos uma função genérica com ambos os métodos.

			from math import floor

			def quartil3(dados, metodo: str = "inclusive") -> float:
				"""Calcula o 3º quartil (Q3) de uma lista numérica.

				Parâmetros:
				  dados  : iterável de números
				  metodo : 'inclusive' (Tukey) ou 'exclusive' (método tipo Excel Q3)

				Retorna:
				  valor numérico de Q3
				"""
				valores = sorted(dados)
				n = len(valores)
				if n == 0:
					raise ValueError("Lista vazia")
				metodo = metodo.lower()
				if metodo == "inclusive":
					# p = 0.75 * (n + 1)
					pos = 0.75 * (n + 1)
				elif metodo == "exclusive":
					# p = 1 + 0.75 * (n - 1)
					pos = 1 + 0.75 * (n - 1)
				else:
					raise ValueError("Método desconhecido. Use 'inclusive' ou 'exclusive'.")

				# Interpolação: se pos é inteiro, retorna diretamente; se não, interpola.
				# Nota: pos está em base 1 (porque usamos (n+1) ou adicionamos 1). Ajustar para índice 0.
				if pos < 1:  # segurança (não ocorre nos métodos acima para n>=1)
					return valores[0]
				if pos > n:
					return valores[-1]

				baixo = floor(pos)
				acima = baixo + 1
				frac = pos - baixo
				# Converter para índices 0-based
				idx_baixo = baixo - 1
				if frac == 0 or acima > n:  # posição inteira ou extrapolação limite
					return float(valores[idx_baixo])
				idx_acima = acima - 1
				return float(valores[idx_baixo] + frac * (valores[idx_acima] - valores[idx_baixo]))

			# Exemplo de uso:
			dados_exemplo = [4, 7, 2, 9, 5, 12, 15, 3, 8]
			q3_inclusive = quartil3(dados_exemplo, "inclusive")
			q3_exclusive = quartil3(dados_exemplo, "exclusive")
			print("\nCálculo do 3º Quartil (Q3):")
			print("Definição conceitual: ordenar o conjunto de dados e localizar o valor (ou interpolação) que separa os 75% inferiores dos 25% superiores.")
			print("Dados ordenados:", sorted(dados_exemplo))
			print(f"Q3 (método inclusive/Tukey):  {q3_inclusive:.4f}")
			print(f"Q3 (método exclusive/Excel):  {q3_exclusive:.4f}")
			print("Ambos seguem a mesma ideia: achar a posição de 0,75 da distribuição após ordenar.")



# Número de resultados possíveis para os 3 primeiros lugares entre 16 times:
#   Cálculo direto:      3360
#   math.perm:           3360
#   itertools (contagem): 3360

# A permutação das letras da palavra ROMA são:
# ROMA    ROAM    RMOA    RMAO    RAOM    RAMO
# ORMA    ORAM    OMRA    OMAR    OARM    OAMR
# MROA    MRAO    MORA    MOAR    MARO    MAOR
# AROM    ARMO    AORM    AOMR    AMRO    AMOR
# Total de permutações: 24

# No lançamento de dois dados, a probabilidade de termos soma maior que 8 é:
# Casos favoráveis: 10
# Casos possíveis:  36
# Probabilidade:    10/36 = 0.2778 (27.78%)

# Moda de Czuber (estimativa para distribuição contínua):
# Forma 1: Moda = L + ((f1 - f0) / (2f1 - f0 - f2)) * h
# Forma 2: Moda = L + (D1 / (D1 + D2)) * h  (equivalente)
# Valores: L=10, f0=8, f1=15, f2=6, h=5, D1=7, D2=9
# Moda (forma 1): 12.1875
# Moda (forma 2): 12.1875
# As duas formas coincidem (OK). Valor final: 12.1875
# Resposta conceitual: usar as diferenças D1=f1-f0 e D2=f1-f2: Moda = L + (D1/(D1+D2)) * h.

# Cálculo do 3º Quartil (Q3):
# Definição conceitual: ordenar o conjunto de dados e localizar o valor (ou interpolação) que separa os 75% inferiores dos 25% superiores.
# Dados ordenados: [2, 3, 4, 5, 7, 8, 9, 12, 15]
# Q3 (método inclusive/Tukey):  10.5000
# Q3 (método exclusive/Excel):  9.0000
# Ambos seguem a mesma ideia: achar a posição de 0,75 da distribuição após ordenar.
