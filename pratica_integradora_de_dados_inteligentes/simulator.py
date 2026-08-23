#simulator.py
def calcular_prima(idade: int, valor_veiculo: float, perfil: str) -> float:
    """Calcula o prêmio de seguro com base em regras simples."""
    fator_idade = 1 + (idade - 18) * 0.01
    fator_veiculo = valor_veiculo * 0.02
    perfil_coef = {'basico': 1.0, 'intermediario': 1.2, 'premium': 1.5}
    return round(fator_veiculo * fator_idade * perfil_coef.get(perfil, 1.0), 2)

# Exemplo de uso
a_prima = calcular_prima(65, 50000.0, 'intermediario')
print(f"Prêmio calculado: R$ {a_prima}")
