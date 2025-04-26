#!/usr/bin/env python
"""
Script para adicionar J.R.R. Tolkien como autor no banco de dados
"""
import os
import sys
import django
from datetime import date

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'descomplica.settings')
django.setup()

# Agora podemos importar modelos Django
from bookapp.models import Author

def add_tolkien():
    """Adiciona J.R.R. Tolkien ao banco de dados"""
    print("\n=== Adicionando J.R.R. Tolkien como autor ===\n")
    
    # Verifica se o autor já existe
    existing_author = Author.objects.filter(name__icontains='tolkien').first()
    
    if existing_author:
        print(f"✅ Autor J.R.R. Tolkien já existe no banco de dados (ID: {existing_author.id})")
        return existing_author
    
    # Cria o autor
    tolkien = Author.objects.create(
        name="J.R.R. Tolkien",
        birth_date=date(1892, 1, 3)  # Data de nascimento real: 3 de janeiro de 1892
    )
    
    print(f"✅ Autor J.R.R. Tolkien criado com sucesso! (ID: {tolkien.id})")
    return tolkien

if __name__ == "__main__":
    try:
        author = add_tolkien()
        print("\n=== Resumo ===")
        print(f"Nome: {author.name}")
        print(f"Data de nascimento: {author.birth_date}")
        print(f"ID: {author.id}")
        print("\nVocê pode agora adicionar livros para este autor através do formulário: http://127.0.0.1:8000/books/book/new/")
    except Exception as e:
        print(f"\n❌ Erro ao adicionar autor: {str(e)}")