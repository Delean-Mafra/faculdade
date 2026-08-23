# api_v1/models.py (Exemplo inicial para Cliente)
from django.db import models
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    # ... outros campos necessários ...
