# api_v1/serializers.py (Exemplo para Simulação)
from rest_framework import serializers
class SimulacaoRequestSerializer(serializers.Serializer):
    idade = serializers.IntegerField(min_value=18)
    valorVeiculo = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    historico = serializers.ChoiceField(choices=['limpo', 'com_sinistros'])
class SimulacaoResponseSerializer(serializers.Serializer):
    valorSeguro = serializers.DecimalField(max_digits=10, decimal_places=2)
    descontoAposentado = serializers.CharField(max_length=5)
