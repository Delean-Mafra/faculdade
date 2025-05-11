from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'data_cadastro')
    search_fields = ('nome', 'descricao')
    list_filter = ('data_cadastro',)
    date_hierarchy = 'data_cadastro'
