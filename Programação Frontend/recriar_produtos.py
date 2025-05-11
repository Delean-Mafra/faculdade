import os
import django
import random
import sys

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_projeto_django.settings')
django.setup()

from produtos.models import Produto
from faker import Faker

# Configura o Faker para usar o idioma português do Brasil
fake = Faker('pt_BR')

def recriar_produtos(quantidade=50):
    """Apaga os produtos existentes e cria novos com nomes em português"""
    
    print("Apagando todos os produtos existentes...")
    Produto.objects.all().delete()
    print("Produtos apagados com sucesso!")
    
    print(f"Criando {quantidade} novos produtos em português...")
    
    # Lista de categorias de produtos em português
    categorias = [
        "Eletrônico", "Eletrodoméstico", "Roupa", "Calçado", "Móvel", 
        "Decoração", "Ferramenta", "Brinquedo", "Livro", "Alimento"
    ]
    
    # Lista de adjetivos em português
    adjetivos = [
        "Novo", "Premium", "Digital", "Portátil", "Profissional", 
        "Moderno", "Avançado", "Básico", "Clássico", "Especial"
    ]
    
    # Lista de produtos em português por categoria
    produtos_por_categoria = {
        "Eletrônico": ["Celular", "Notebook", "Tablet", "Fone de Ouvido", "Mouse", "Teclado", "Monitor", "Câmera", "Smart TV", "Caixa de Som"],
        "Eletrodoméstico": ["Geladeira", "Fogão", "Micro-ondas", "Liquidificador", "Batedeira", "Cafeteira", "Aspirador", "Ventilador", "Ar Condicionado", "Máquina de Lavar"],
        "Roupa": ["Camiseta", "Calça", "Vestido", "Jaqueta", "Moletom", "Bermuda", "Blusa", "Casaco", "Meia", "Cueca"],
        "Calçado": ["Tênis", "Sapato", "Sandália", "Chinelo", "Bota", "Sapatilha", "Mocassim", "Chuteira", "Pantufa", "Tamanco"],
        "Móvel": ["Sofá", "Cadeira", "Mesa", "Armário", "Estante", "Cama", "Rack", "Poltrona", "Escrivaninha", "Guarda-roupa"],
        "Decoração": ["Quadro", "Tapete", "Luminária", "Vaso", "Espelho", "Almofada", "Cortina", "Abajur", "Relógio", "Estatueta"],
        "Ferramenta": ["Furadeira", "Martelo", "Chave de Fenda", "Alicate", "Serra", "Parafusadeira", "Trena", "Chave Inglesa", "Nível", "Estilete"],
        "Brinquedo": ["Boneca", "Carrinho", "Quebra-cabeça", "Bola", "Jogo de Tabuleiro", "Pelúcia", "Patinete", "Bicicleta", "Lego", "Pipa"],
        "Livro": ["Romance", "Aventura", "Biografia", "Autoajuda", "Técnico", "Infantil", "Ficção", "História", "Poesia", "Mangá"],
        "Alimento": ["Chocolate", "Biscoito", "Salgadinho", "Cereal", "Tempero", "Molho", "Conserva", "Café", "Chá", "Refrigerante"]
    }
    
    for _ in range(quantidade):
        # Seleciona uma categoria aleatória
        categoria = random.choice(categorias)
        
        # Seleciona um produto aleatório da categoria
        produto_base = random.choice(produtos_por_categoria[categoria])
        
        # Seleciona um adjetivo aleatório
        adjetivo = random.choice(adjetivos)
        
        # Cria o nome do produto (formato: Adjetivo + Produto + "de" + Categoria)
        nome = f"{adjetivo} {produto_base} {categoria}"
        
        # Gera descrição, preço e estoque
        descricao = fake.paragraph(nb_sentences=3)
        preco = round(random.uniform(10, 5000), 2)
        estoque = random.randint(0, 100)
        
        # Cria o produto no banco de dados
        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            estoque=estoque
        )
    
    print(f"{quantidade} produtos criados com sucesso!")

if __name__ == "__main__":
    print("Iniciando recriação de produtos com nomes em português...")
    recriar_produtos(50)
    print("Processo finalizado!")
