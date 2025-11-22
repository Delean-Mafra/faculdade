# --- Listas Iniciais ---
nomes = ["Ana Silva", "João Santos", "Maria Oliveira", "Pedro Souza", "Lucas Pereira"]
medias_notas = [7.5, 4.2, 1.9, 9.0, 9.5]

MEDIA_MINIMA = 5.0
PONTO_BONUS = 1.0

# --- Processamento com WHILE ---

print("--- Resultado Final dos Alunos (usando WHILE) ---")

# Inicializa o índice de controle
i = 0 
numero_de_alunos = len(nomes) # Obtém o total de alunos na lista

# O loop WHILE executa enquanto 'i' for menor que o número total de alunos
while i < numero_de_alunos:
    
    # 1. Aplica o bônus e garante que não ultrapasse 10.0
    nova_media = medias_notas[i] + PONTO_BONUS
    if nova_media > 10.0:
        nova_media = 10.0
        
    # 2. Determina o status
    status = ""
    if nova_media >= MEDIA_MINIMA:
        status = "APROVADO"
    else:
        status = "REPROVADO"
        
    # 3. Imprime o resultado formatado
    print(f"Aluno: {nomes[i]:<15} | Média Final: {nova_media:.2f} | Status: {status}")
    
    # 4. PASSO CRÍTICO: Atualiza o índice
    # Se esquecermos desta linha, o loop se torna infinito!
    i += 1


print()

n = 0
while n < len(medias_notas): 
    medias_notas[n] = medias_notas[n] + 1.0
    if medias_notas[n] > 10.00:
        medias_notas[n] = 10.00
n = n + 1



print(medias_notas[len(medias_notas) -1]) # Acessa o ultimo elemento da lista
print(medias_notas[-1]) # Acessa o ultimo elemento da lista

print(medias_notas[1:3]) # da segunda até a terceira posição

print(medias_notas[0:]) # da primeira posição até a ultima  

print(medias_notas[:4]) # Até a 5° posição

medias_notas.append('Joana da Silva') # Adiciona um novo elemento ao final da lista


medias_notas.extend(['Paulo Silveira','Marcio Pereira']) # Adiciona múltiplos elementos ao final da lista

medias_notas.remove('Paulo Silveira') # Remove o elemento especificado da lista

medias_notas.pop(1) # Remove o elemento na posição especificada (índice 1)
