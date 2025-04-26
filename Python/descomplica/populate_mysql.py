#!/usr/bin/env python
"""
Este script popula o banco de dados MySQL com dados fictícios para o sistema de cadastro de livros.
"""
import os
import sys
import django
import random
import datetime
from faker import Faker

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'descomplica.settings')
django.setup()

# Importa os modelos após configurar o ambiente Django
from bookapp.models import Author, Book

def check_faker():
    try:
        print("✓ Faker instalado")
        return True
    except ImportError:
        print("❌ Faker não está instalado")
        
        # Tenta instalar o módulo
        print("\nInstalando faker...")
        import subprocess
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "faker"],
            capture_output=True, 
            text=True
        )
        
        if result.returncode == 0:
            print("✅ Faker instalado com sucesso")
            return True
        else:
            print(f"❌ Falha ao instalar Faker: {result.stderr}")
            return False

def generate_authors(n=10):
    """Gera n autores fictícios"""
    print(f"\nGerando {n} autores fictícios...")
    
    fake = Faker('pt_BR')
    authors_created = 0
    
    for _ in range(n):
        name = fake.name()
        # Gera uma data de nascimento entre 1920 e 2000
        birth_date = fake.date_of_birth(minimum_age=20, maximum_age=100)
        
        try:
            author = Author.objects.create(
                name=name,
                birth_date=birth_date
            )
            authors_created += 1
            print(f"  ✓ Autor criado: {name} ({birth_date})")
        except Exception as e:
            print(f"  ❌ Erro ao criar autor {name}: {str(e)}")
    
    return authors_created

def generate_books(n=30):
    """Gera n livros fictícios"""
    print(f"\nGerando {n} livros fictícios...")
    
    fake = Faker('pt_BR')
    books_created = 0
    
    # Gêneros comuns de livros
    genres = [
        "Romance", "Ficção Científica", "Fantasia", "Thriller", 
        "Mistério", "Horror", "Biografia", "História", "Autoajuda",
        "Negócios", "Infantil", "Aventura", "Poesia", "Drama",
        "Técnico", "Educacional", "Filosofia", "Política"
    ]
    
    # Editoras comuns no Brasil
    publishers = [
        "Companhia das Letras", "Record", "Planeta", "Rocco",
        "Intrínseca", "Sextante", "Nova Fronteira", "Globo Livros",
        "Aleph", "Arqueiro", "Darkside", "Suma", "Atlas", "Moderna",
        "FTD", "Saraiva", "Leya", "Martin Claret", "Zahar"
    ]
    
    # Obter todos os autores do banco de dados
    authors = list(Author.objects.all())
    if not authors:
        print("  ❌ Nenhum autor encontrado. Por favor, crie autores primeiro.")
        return 0
    
    for i in range(n):
        title = fake.catch_phrase()
        
        # Gera um ISBN único válido (13 dígitos)
        isbn = f"978{fake.numerify('#########')}"
        
        # Escolhe um autor aleatório da lista
        author = random.choice(authors)
        
        # Escolhe uma editora aleatória
        publisher = random.choice(publishers)
        
        # Ano de publicação entre 1990 e o ano atual
        current_year = datetime.datetime.now().year
        publication_year = random.randint(1990, current_year)
        
        # Número de páginas entre 80 e 1200
        page_count = random.randint(80, 1200)
        
        # Gênero aleatório
        genre = random.choice(genres)
        
        try:
            book = Book.objects.create(
                title=title,
                isbn=isbn,
                author=author,
                publisher=publisher,
                publication_year=publication_year,
                page_count=page_count,
                genre=genre
            )
            books_created += 1
            print(f"  ✓ Livro criado: {title} ({isbn})")
        except Exception as e:
            print(f"  ❌ Erro ao criar livro {title}: {str(e)}")
    
    return books_created

def main():
    print("\n=== Populando o banco de dados MySQL com dados fictícios ===\n")
    
    # Verifica se o Faker está instalado
    if not check_faker():
        print("\n❌ Falha na instalação do Faker, necessário para gerar dados fictícios")
        return
    
    # Pergunta ao usuário quantos registros deseja criar
    try:
        num_authors = int(input("Quantos autores você deseja criar? [10]: ") or "10")
        num_books = int(input("Quantos livros você deseja criar? [30]: ") or "30")
    except ValueError:
        print("❌ Por favor, insira apenas números.")
        num_authors = 10
        num_books = 30
    
    # Gera autores fictícios
    authors_created = generate_authors(num_authors)
    print(f"\n✅ {authors_created} autores criados com sucesso!")
    
    # Gera livros fictícios
    books_created = generate_books(num_books)
    print(f"\n✅ {books_created} livros criados com sucesso!")
    
    print("\n=== Resumo da população do banco de dados ===")
    print(f"Autores criados: {authors_created}")
    print(f"Livros criados: {books_created}")
    print("\nAgora você pode iniciar o servidor Django e visualizar os dados:")
    print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe manage.py runserver")

if __name__ == "__main__":
    main()