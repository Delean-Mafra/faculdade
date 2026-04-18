# Gera um arquivo CSV com 1000 linhas no mesmo padrão do fraudes.csv fornecido

import csv
import random
import numpy as np

# Configurações
N = 1000
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

# Probabilidades aproximadas para Local
p_local = {
    "Local_A": 0.35,
    "Local_B": 0.33,
    "Local_C": 0.32
}

p_fraude = 0.48

# Parâmetros para gerar "Valor" (média e desvio padrão aproximados do arquivo)
valor_mean = 1000.0
valor_std = 200.0
valor_min = 300.0
valor_max = 1800.0

def sample_local():
    r = random.random()
    if r < p_local["Local_A"]:
        return "Local_A"
    elif r < p_local["Local_A"] + p_local["Local_B"]:
        return "Local_B"
    else:
        return "Local_C"

def sample_valor():
    # Amostra de uma normal truncada entre valor_min e valor_max
    while True:
        v = np.random.normal(loc=valor_mean, scale=valor_std)
        if valor_min <= v <= valor_max:
            return float(v)

def sample_fraude():
    return 1 if random.random() < p_fraude else 0

# Nome do arquivo de saída
output_file = "fraudes.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Cabeçalho igual ao do arquivo original
    writer.writerow(["Valor", "Local", "Fraude"])
    for _ in range(N):
        valor = sample_valor()
        local = sample_local()
        fraude = sample_fraude()
        # Formata Valor com muitas casas decimais, similar ao CSV original
        writer.writerow([f"{valor:.16f}", local, fraude])

print(f"Arquivo gerado: {output_file} ({N} linhas, mais o cabeçalho)")
