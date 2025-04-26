#!/usr/bin/env python
"""
Script completo para configurar e resolver todos os problemas do projeto
- Instala todas as dependências necessárias
- Configura o banco de dados (MySQL ou SQLite)
- Cria os templates necessários
- Popula o banco de dados com dados fictícios
"""
import os
import sys
import subprocess
import time
import importlib
import random
from datetime import datetime, timedelta

# Diretório do projeto
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_command(command, capture=True, check=False):
    """Executa um comando e retorna o resultado"""
    print(f"Executando: {' '.join(command)}")
    if capture:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result.returncode == 0
    else:
        try:
            subprocess.run(command, check=check)
            return True
        except subprocess.CalledProcessError:
            return False

def install_dependencies():
    """Instala todas as dependências necessárias"""
    print("\n=== Instalando dependências necessárias ===\n")
    
    dependencies = [
        "pymysql",         # Driver Python puro para MySQL
        "faker",           # Biblioteca para gerar dados fictícios
    ]
    
    pip_command = [sys.executable, "-m", "pip", "install", "--upgrade"]
    
    for dep in dependencies:
        print(f"\nInstalando {dep}...")
        if not run_command(pip_command + [dep]):
            print(f"❌ Falha ao instalar {dep}")
        else:
            print(f"✅ {dep} instalado com sucesso")

def setup_django_pymysql():
    """Configura o PyMySQL como backend para o Django"""
    print("\n=== Configurando PyMySQL para Django ===\n")
    
    # Cria ou atualiza o __init__.py do projeto
    init_path = os.path.join(PROJECT_DIR, 'descomplica', '__init__.py')
    pymysql_config = """try:
    import pymysql
    pymysql.install_as_MySQLdb()
    print("PyMySQL instalado como MySQLdb")
except ImportError:
    print("PyMySQL não está disponível, usando outro backend")
"""
    
    with open(init_path, 'w', encoding='utf-8') as file:
        file.write(pymysql_config)
    
    print("✅ Configuração PyMySQL adicionada ao arquivo __init__.py")

def update_settings_for_sqlite():
    """Atualiza settings.py para usar SQLite como banco de dados"""
    print("\n=== Configurando SQLite como banco de dados ===\n")
    
    settings_path = os.path.join(PROJECT_DIR, 'descomplica', 'settings.py')
    
    with open(settings_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Localiza a seção DATABASES
    if "'ENGINE': 'django.db.backends.mysql'" in content:
        sqlite_config = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""
        
        # Substitui toda a configuração de banco de dados
        import re
        pattern = r"DATABASES\s*=\s*\{[^}]*\}"
        content = re.sub(pattern, sqlite_config, content, flags=re.DOTALL)
        
        with open(settings_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print("✅ Configuração do banco de dados atualizada para SQLite")
    else:
        print("✓ Configuração do banco de dados já está usando SQLite")

def update_template_form():
    """Atualiza o template de formulário para não usar o filtro add_class"""
    print("\n=== Corrigindo template de formulário ===\n")
    
    form_path = os.path.join(PROJECT_DIR, 'templates', 'bookapp', 'book_form.html')
    
    if not os.path.exists(form_path):
        print(f"❌ Template não encontrado: {form_path}")
        return False
    
    with open(form_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Corrige o problema do filtro add_class
    if "{{ field|add_class:" in content:
        content = content.replace(
            '{{ field|add_class:"form-control" }}', 
            '{{ field }}'
        )
        
        with open(form_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print("✅ Template atualizado para remover filtro add_class")
    else:
        print("✓ Template já está corrigido")
    
    return True

def run_migrations():
    """Executa as migrações do Django"""
    print("\n=== Aplicando migrações ao banco de dados ===\n")
    
    # Executa as migrações sem capturar a saída para ver erros em tempo real
    success = run_command([sys.executable, "manage.py", "migrate"], capture=False)
    
    if success:
        print("\n✅ Migrações aplicadas com sucesso")
    else:
        print("\n❌ Falha ao aplicar migrações")
    
    return success

def populate_database():
    """Popula o banco de dados com dados fictícios"""
    print("\n=== Populando banco de dados com dados fictícios ===\n")
    
    # Tenta importar os módulos necessários
    try:
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'descomplica.settings')
        django.setup()
        
        from bookapp.models import Author, Book
        
        # Verifica se já existem dados no banco
        if Author.objects.exists() and Book.objects.exists():
            print("✓ Banco de dados já contém dados")
            authors_count = Author.objects.count()
            books_count = Book.objects.count()
            print(f"  - {authors_count} autores")
            print(f"  - {books_count} livros")
            
            # Pergunta se deseja recriar os dados
            recreate = input("\nDeseja recriar os dados? (s/N): ").lower() == 's'
            if not recreate:
                print("Mantendo os dados existentes")
                return True
            else:
                # Limpa os dados existentes
                Book.objects.all().delete()
                Author.objects.all().delete()
                print("Dados anteriores removidos")
        
        # Importa o Faker ou cria uma função alternativa se não estiver disponível
        try:
            from faker import Faker
            fake = Faker('pt_BR')
            has_faker = True
        except ImportError:
            print("⚠️ Faker não encontrado, utilizando dados básicos")
            has_faker = False
            
            # Função alternativa para gerar nomes
            def generate_name():
                first_names = ["João", "Maria", "Pedro", "Ana", "Carlos", "Mariana", "José", "Lúcia", "Antônio", "Fernanda"]
                last_names = ["Silva", "Santos", "Oliveira", "Souza", "Lima", "Pereira", "Costa", "Ferreira", "Rodrigues", "Almeida"]
                return f"{random.choice(first_names)} {random.choice(last_names)}"
            
            # Função alternativa para gerar datas
            def generate_date():
                return datetime.now() - timedelta(days=random.randint(365*20, 365*80))
        
        # Gera autores
        num_authors = 10
        print(f"\nGerando {num_authors} autores...")
        
        for i in range(num_authors):
            if has_faker:
                name = fake.name()
                birth_date = fake.date_of_birth(minimum_age=20, maximum_age=100)
            else:
                name = generate_name()
                birth_date = generate_date().date()
            
            author = Author.objects.create(
                name=name,
                birth_date=birth_date
            )
            print(f"  ✓ Autor criado: {name} ({birth_date})")
        
        # Gera livros
        num_books = 30
        print(f"\nGerando {num_books} livros...")
        
        # Gêneros e editoras
        genres = ["Romance", "Ficção Científica", "Fantasia", "Thriller", "Mistério", "Horror", "Biografia", "História"]
        publishers = ["Companhia das Letras", "Record", "Rocco", "Intrínseca", "Sextante", "Nova Fronteira", "Globo"]
        
        # Obter todos os autores
        authors = list(Author.objects.all())
        
        for i in range(num_books):
            if has_faker:
                title = fake.catch_phrase()
                isbn = f"978{fake.numerify('#########')}"
            else:
                words = ["O", "A", "Um", "Uma", "Grande", "Pequeno", "Novo", "Antigo", "Último", "Primeiro"]
                nouns = ["Livro", "História", "Aventura", "Mistério", "Segredo", "Viagem", "Caminho", "Herói", "Lenda", "Saga"]
                title = f"{random.choice(words)} {random.choice(nouns)} {random.randint(1, 99)}"
                isbn = f"978{random.randint(100000000, 999999999)}"
            
            author = random.choice(authors)
            publisher = random.choice(publishers)
            publication_year = random.randint(1990, datetime.now().year)
            page_count = random.randint(80, 1200)
            genre = random.choice(genres)
            
            book = Book.objects.create(
                title=title,
                isbn=isbn,
                author=author,
                publisher=publisher,
                publication_year=publication_year,
                page_count=page_count,
                genre=genre
            )
            print(f"  ✓ Livro criado: {title} ({isbn})")
        
        print(f"\n✅ Dados fictícios criados com sucesso!")
        print(f"  - {num_authors} autores")
        print(f"  - {num_books} livros")
        return True
    
    except Exception as e:
        print(f"\n❌ Erro ao popular o banco de dados: {str(e)}")
        return False

def main():
    print("\n====== CONFIGURAÇÃO COMPLETA DO PROJETO ======\n")
    print("Este script vai resolver todos os problemas e configurar o projeto.")
    
    # 1. Instalar dependências
    install_dependencies()
    
    # 2. Configurar PyMySQL para Django
    setup_django_pymysql()
    
    # 3. Usar SQLite em vez de MySQL para evitar problemas de compatibilidade
    update_settings_for_sqlite()
    
    # 4. Corrigir template
    update_template_form()
    
    # 5. Aplicar migrações
    run_migrations()
    
    # 6. Popular banco de dados
    populate_database()
    
    print("\n✅ Configuração do projeto concluída!")
    print("\nAgora você pode iniciar o servidor com:")
    print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe manage.py runserver")
    print("\nAcesse a aplicação em: http://127.0.0.1:8000/")
    print("\nAcesse o painel administrativo em: http://127.0.0.1:8000/admin/")
    print("  Usuário: admin")
    print("  Senha: 123456Ab")

if __name__ == "__main__":
    main()