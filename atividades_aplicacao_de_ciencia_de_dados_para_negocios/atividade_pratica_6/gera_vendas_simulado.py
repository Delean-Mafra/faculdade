import csv
import random
import numpy as np

# Configurações
N = 1000
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

# Parâmetros para "Vendas"
vendas_mean = 200.0    # média aproximada observada no arquivo
vendas_std = 60.0      # desvio padrão aproximado
vendas_min = 50.0
vendas_max = 320.0

# Probabilidade de Evento = 1 
p_evento = 0.48

def sample_vendas():
    # Amostra de uma normal truncada entre vendas_min e vendas_max
    while True:
        v = np.random.normal(loc=vendas_mean, scale=vendas_std)
        if vendas_min <= v <= vendas_max:
            return round(float(v), 2)

def sample_evento():
    return 1 if random.random() < p_evento else 0

output_file = "vendas.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Cabeçalho igual ao do arquivo original
    writer.writerow(["Meses", "Vendas", "Eventos"])
    for i in range(1, N + 1):
        meses = i
        vendas = sample_vendas()
        evento = sample_evento()
        writer.writerow([meses, f"{vendas:.2f}", evento])

print(f"Arquivo gerado: {output_file} ({N} linhas, mais o cabeçalho)")
