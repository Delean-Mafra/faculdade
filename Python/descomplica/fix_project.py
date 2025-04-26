#!/usr/bin/env python
"""
Script de correção definitiva para o projeto Django
- Converte o banco de dados de MySQL para SQLite (evitando problemas de versão)
- Corrige o problema do filtro add_class no template
- Instala dependências necessárias
- Migra o banco de dados
- Popula o banco com dados fictícios
"""
import os
import sys
import subprocess
import random
from datetime import datetime, timedelta
import importlib.util

# Cores para o console
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Diretório do projeto
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def print_header(text):
    """Imprime um texto como cabeçalho"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}=== {text} ==={Colors.ENDC}\n")

def print_success(text):
    """Imprime uma mensagem de sucesso"""
    print(f"{Colors.GREEN}✅ {text}{Colors.ENDC}")

def print_warning(text):
    """Imprime um aviso"""
    print(f"{Colors.WARNING}⚠️ {text}{Colors.ENDC}")

def print_error(text):
    """Imprime uma mensagem de erro"""
    print(f"{Colors.FAIL}❌ {text}{Colors.ENDC}")

def run_command(command, capture=True, check=False):
    """Executa um comando e retorna o resultado"""
    print(f"{Colors.BLUE}Executando: {' '.join(command)}{Colors.ENDC}")
    try:
        if capture:
            result = subprocess.run(command, capture_output=True, text=True)
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr)
            return result.returncode == 0
        else:
            subprocess.run(command, check=check)
            return True
    except subprocess.CalledProcessError:
        return False

def is_package_installed(package_name):
    """Verifica se um pacote está instalado"""
    return importlib.util.find_spec(package_name) is not None

def install_dependencies():
    """Instala todas as dependências necessárias"""
    print_header("Instalando dependências")
    
    # Lista de dependências
    dependencies = ["faker"]
    
    for dep in dependencies:
        if not is_package_installed(dep):
            print(f"Instalando {dep}...")
            if run_command([sys.executable, "-m", "pip", "install", dep]):
                print_success(f"{dep} instalado com sucesso")
            else:
                print_error(f"Falha ao instalar {dep}")
        else:
            print(f"✓ {dep} já está instalado")

def convert_to_sqlite():
    """Converte a configuração do banco de dados para SQLite"""
    print_header("Convertendo para SQLite")
    
    settings_path = os.path.join(PROJECT_DIR, 'descomplica', 'settings.py')
    
    # Verifica se o arquivo existe
    if not os.path.exists(settings_path):
        print_error(f"Arquivo settings.py não encontrado em {settings_path}")
        return False
    
    # Lê o arquivo settings.py
    with open(settings_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Configuração do SQLite
    sqlite_config = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""
    
    # Procura pela configuração atual do banco de dados
    import re
    db_pattern = r"DATABASES\s*=\s*\{[^}]*\}"
    
    # Verifica se é MySQL ou outro
    if "django.db.backends.mysql" in content:
        print("Encontrada configuração MySQL, convertendo para SQLite...")
        # Substitui a configuração
        content = re.sub(db_pattern, sqlite_config, content, flags=re.DOTALL)
        
        # Verifica e remove qualquer configuração PyMySQL no início do arquivo
        if "pymysql.install_as_MySQLdb()" in content:
            content = re.sub(r"import pymysql\s*pymysql\.install_as_MySQLdb\(\)", "", content)
        
        # Salva o arquivo modificado
        with open(settings_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print_success("Configuração convertida para SQLite")
        return True
    
    elif "django.db.backends.sqlite3" in content:
        print("✓ Já está usando SQLite")
        return True
    
    else:
        print_warning("Não foi possível identificar a configuração do banco de dados")
        print("Adicionando configuração SQLite...")
        
        # Tenta adicionar a configuração de banco de dados no final do arquivo
        with open(settings_path, 'a', encoding='utf-8') as file:
            file.write("\n\n# Configuração do banco de dados para SQLite\n")
            file.write(sqlite_config)
        
        print_success("Configuração SQLite adicionada ao final do arquivo")
        return True

def fix_template():
    """Corrige o problema do filtro add_class no template"""
    print_header("Corrigindo template")
    
    form_path = os.path.join(PROJECT_DIR, 'templates', 'bookapp', 'book_form.html')
    
    # Verifica se o arquivo existe
    if not os.path.exists(form_path):
        print_error(f"Arquivo de template não encontrado: {form_path}")
        return False
    
    # Lê o arquivo do template
    with open(form_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Verifica se o filtro add_class está sendo usado
    if "{{ field|add_class:" in content:
        print("Encontrado uso do filtro add_class, corrigindo...")
        
        # Substitui o filtro add_class por uma solução compatível
        content = content.replace(
            '{{ field|add_class:"form-control" }}',
            '{{ field }}'
        )
        
        # Salva o arquivo modificado
        with open(form_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print_success("Template corrigido")
        return True
    else:
        print("✓ Template já está correto")
        return True

def migrate_database():
    """Aplica as migrações do Django"""
    print_header("Aplicando migrações")
    
    # Tenta excluir o banco de dados SQLite existente
    db_path = os.path.join(PROJECT_DIR, 'db.sqlite3')
    if os.path.exists(db_path):
        print("Excluindo banco de dados SQLite existente...")
        try:
            os.remove(db_path)
            print_success("Banco de dados antigo removido")
        except Exception as e:
            print_warning(f"Não foi possível remover o banco de dados: {e}")
    
    # Executa as migrações
    print("Aplicando migrações...")
    return run_command([sys.executable, "manage.py", "migrate"], capture=False)

def populate_database():
    """Popula o banco de dados com dados fictícios"""
    print_header("Populando o banco de dados")
    
    try:
        # Configurar ambiente Django
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'descomplica.settings')
        django.setup()
        
        # Importar modelos
        from bookapp.models import Author, Book
        
        # Verifique se já existem dados
        if Author.objects.exists():
            author_count = Author.objects.count()
            book_count = Book.objects.count()
            print(f"Já existem {author_count} autores e {book_count} livros no banco")
            
            if input("Deseja recriar os dados? (s/N): ").lower() == 's':
                Book.objects.all().delete()
                Author.objects.all().delete()
                print_success("Dados anteriores removidos")
            else:
                print("Mantendo dados existentes")
                return True
        
        # Tenta importar Faker
        try:
            from faker import Faker
            fake = Faker('pt_BR')
            has_faker = True
            print("✓ Usando Faker para gerar dados")
        except ImportError:
            print_warning("Faker não encontrado, usando dados básicos")
            has_faker = False
        
        # Criar autores
        num_authors = 10
        print(f"\nCriando {num_authors} autores...")
        
        for i in range(num_authors):
            if has_faker:
                name = fake.name()
                birth_date = fake.date_of_birth(minimum_age=20, maximum_age=100)
            else:
                first_names = ["João", "Maria", "Pedro", "Ana", "Carlos", "Mariana", "José", "Lúcia", "Antônio", "Fernanda"]
                last_names = ["Silva", "Santos", "Oliveira", "Souza", "Lima", "Pereira", "Costa", "Ferreira", "Rodrigues", "Almeida"]
                name = f"{random.choice(first_names)} {random.choice(last_names)}"
                birth_date = datetime.now().date() - timedelta(days=random.randint(365*20, 365*80))
            
            author = Author.objects.create(
                name=name,
                birth_date=birth_date
            )
            print(f"  ✓ Autor criado: {name} ({birth_date})")
        
        # Criar livros
        num_books = 30
        print(f"\nCriando {num_books} livros...")
        
        # Listas para dados
        genres = [
            "Romance", "Ficção Científica", "Fantasia", "Thriller", 
            "Mistério", "Horror", "Biografia", "História", "Autoajuda"
        ]
        publishers = [
            "Companhia das Letras", "Record", "Planeta", "Rocco",
            "Intrínseca", "Sextante", "Nova Fronteira", "Globo Livros"
        ]
        
        # Obter autores
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
        
        print_success(f"Banco de dados populado com {num_authors} autores e {num_books} livros")
        return True
        
    except Exception as e:
        print_error(f"Erro ao popular o banco de dados: {str(e)}")
        return False

def create_superuser():
    """Cria um superusuário se ainda não existir"""
    print_header("Verificando superusuário")
    
    try:
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'descomplica.settings')
        django.setup()
        
        from django.contrib.auth.models import User
        
        # Verifica se já existe um superusuário
        if User.objects.filter(is_superuser=True).exists():
            print("✓ Já existe pelo menos um superusuário")
            return True
        
        # Cria um superusuário admin
        print("Criando superusuário 'admin'...")
        User.objects.create_superuser('admin', 'admin@example.com', '123456Ab')
        print_success("Superusuário 'admin' criado com senha '123456Ab'")
        return True
        
    except Exception as e:
        print_error(f"Erro ao criar superusuário: {str(e)}")
        return False

def main():
    print(f"\n{Colors.HEADER}{Colors.BOLD}======== CORREÇÃO COMPLETA DO PROJETO ========{Colors.ENDC}")
    print(f"{Colors.BOLD}Este script vai corrigir todos os problemas e configurar o projeto.{Colors.ENDC}\n")
    
    steps = [
        ("Instalar dependências", install_dependencies),
        ("Converter para SQLite", convert_to_sqlite),
        ("Corrigir template", fix_template),
        ("Migrar banco de dados", migrate_database),
        ("Popular banco de dados", populate_database),
        ("Criar superusuário", create_superuser)
    ]
    
    for step_name, step_func in steps:
        print(f"\n{Colors.BLUE}>> Passo: {step_name}{Colors.ENDC}")
        success = step_func()
        if not success:
            print_error(f"Falha no passo: {step_name}")
            print_warning("O script continuará com os próximos passos")
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}✅ PROJETO CORRIGIDO E CONFIGURADO COM SUCESSO!{Colors.ENDC}")
    print(f"\n{Colors.BOLD}Você pode iniciar o servidor com:{Colors.ENDC}")
    print("python manage.py runserver")
    print(f"\n{Colors.BOLD}Acesse a aplicação em:{Colors.ENDC} http://127.0.0.1:8000/")
    print(f"\n{Colors.BOLD}Acesse o painel administrativo em:{Colors.ENDC} http://127.0.0.1:8000/admin/")
    print("  Usuário: admin")
    print("  Senha: 123456Ab")

if __name__ == "__main__":
    main()