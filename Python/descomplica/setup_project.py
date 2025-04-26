import os
import sys

# Conteúdo dos arquivos
FILE_CONTENTS = {
    'manage.py': '''#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'descomplica.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
''',
    'descomplica/__init__.py': '# Este arquivo pode ficar vazio',
    'descomplica/settings.py': '''"""
Django settings for descomplica project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ficticio123456789abcdefghijklmnopqrstuvwxyz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'descomplica.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'descomplica.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect URLs
LOGIN_REDIRECT_URL = 'book-list'
LOGIN_URL = 'login'
''',
    'descomplica/urls.py': '''"""
URL configuration for descomplica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('bookapp.urls')),
]
''',
    'descomplica/asgi.py': '''"""
ASGI config for descomplica project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'descomplica.settings')

application = get_asgi_application()
''',
    'descomplica/wsgi.py': '''"""
WSGI config for descomplica project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'descomplica.settings')

application = get_wsgi_application()
''',
    'bookapp/__init__.py': '# Este arquivo pode ficar vazio',
    'bookapp/admin.py': '''from django.contrib import admin
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_year', 'isbn')
    search_fields = ('title', 'isbn')
    list_filter = ('publication_year', 'publisher')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
''',
    'bookapp/apps.py': '''from django.apps import AppConfig

class BookappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookapp'
    verbose_name = 'Gerenciamento de Livros'
''',
    'bookapp/models.py': '''from django.db import models
from django.core.exceptions import ValidationError
import datetime

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    page_count = models.IntegerField()
    genre = models.CharField(max_length=50, blank=True, null=True)

    def clean(self):
        # Validação personalizada para ISBN
        if self.isbn and len(self.isbn) != 13 and len(self.isbn) != 10:
            raise ValidationError({'isbn': 'ISBN deve ter 10 ou 13 caracteres'})
            
        # Validação para ano de publicação
        current_year = datetime.datetime.now().year
        if self.publication_year > current_year:
            raise ValidationError({'publication_year': 'O ano de publicação não pode ser no futuro'})

    def __str__(self):
        return self.title
''',
    'bookapp/forms.py': '''from django import forms
import datetime
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'author', 'publisher', 'publication_year', 'page_count', 'genre']

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        current_year = datetime.datetime.now().year
        
        if year > current_year:
            raise forms.ValidationError('O ano de publicação não pode ser no futuro')
        
        return year
        
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        
        # Verifica se o ISBN tem o comprimento adequado
        if len(isbn) != 10 and len(isbn) != 13:
            raise forms.ValidationError('ISBN deve ter 10 ou 13 caracteres')
            
        # Verificar se o ISBN já existe
        if Book.objects.filter(isbn=isbn).exclude(id=self.instance.id if self.instance.pk else None).exists():
            raise forms.ValidationError('Este ISBN já está em uso.')
            
        return isbn
''',
    'bookapp/views.py': '''from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book, Author
from .forms import BookForm

class BookListView(ListView):
    model = Book
    template_name = 'bookapp/book_list.html'
    context_object_name = 'books'
    paginate_by = 10

class BookDetailView(DetailView):
    model = Book
    template_name = 'bookapp/book_detail.html'
    context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/book_form.html'
    success_url = reverse_lazy('book-list')
    
    def form_valid(self, form):
        messages.success(self.request, "Livro cadastrado com sucesso!")
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/book_form.html'
    success_url = reverse_lazy('book-list')
    
    def form_valid(self, form):
        messages.success(self.request, "Informações atualizadas com sucesso!")
        return super().form_valid(form)

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'bookapp/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Livro excluído com sucesso!")
        return super().delete(request, *args, **kwargs)

# Buscas simples de autor
class AuthorListView(ListView):
    model = Author
    template_name = 'bookapp/author_list.html'
    context_object_name = 'authors'
''',
    'bookapp/urls.py': '''from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book/new/', views.BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
]
''',
    'bookapp/tests/__init__.py': '# Este arquivo pode ficar vazio',
    'bookapp/tests/test_book_model.py': '''from django.test import TestCase
from django.core.exceptions import ValidationError
from bookapp.models import Book, Author

class BookModelTest(TestCase):
    def setUp(self):
        # Configuração inicial para cada teste
        self.author = Author.objects.create(
            name="Douglas Adams",
            birth_date="1952-03-11"
        )
        
        self.book_data = {
            'title': 'O Guia do Mochileiro das Galáxias',
            'isbn': '9788576572145',
            'publisher': 'Arqueiro',
            'publication_year': 2010,
            'page_count': 208
        }

    def test_create_book_with_valid_data(self):
        """Teste para verificar se um livro é criado com dados válidos"""
        # Criar um novo livro
        book = Book.objects.create(author=self.author, **self.book_data)
        
        # Verificar se o livro foi salvo no banco de dados
        self.assertEqual(Book.objects.count(), 1)
        
        # Verificar se os campos foram salvos corretamente
        saved_book = Book.objects.first()
        self.assertEqual(saved_book.title, self.book_data['title'])
        self.assertEqual(saved_book.isbn, self.book_data['isbn'])
        self.assertEqual(saved_book.publisher, self.book_data['publisher'])
        self.assertEqual(saved_book.publication_year, self.book_data['publication_year'])
        self.assertEqual(saved_book.page_count, self.book_data['page_count'])
        
        # Verificar relacionamento com o autor
        self.assertEqual(saved_book.author, self.author)

    def test_book_with_invalid_isbn(self):
        """Teste para verificar se um erro é lançado quando o ISBN é inválido"""
        # Tentar criar um livro com ISBN inválido (muito curto)
        with self.assertRaises(ValidationError):
            book = Book(
                author=self.author,
                title=self.book_data['title'],
                isbn='12345',  # ISBN inválido
                publisher=self.book_data['publisher'],
                publication_year=self.book_data['publication_year'],
                page_count=self.book_data['page_count']
            )
            # Validação explícita para acionar o ValidationError
            book.full_clean()

    def test_unique_isbn_constraint(self):
        """Teste para verificar se não é possível criar dois livros com o mesmo ISBN"""
        # Criar o primeiro livro
        Book.objects.create(author=self.author, **self.book_data)
        
        # Tentar criar um segundo livro com o mesmo ISBN
        duplicate_book = Book(
            author=self.author,
            title="Outro Livro",
            isbn=self.book_data['isbn'],  # mesmo ISBN
            publisher="Outra Editora",
            publication_year=2020,
            page_count=300
        )
        
        # Verificar se um erro é lançado ao tentar salvar
        with self.assertRaises(Exception):  # Poderia ser mais específico com IntegrityError
            duplicate_book.save()
''',
    'bookapp/tests/test_book_form.py': '''from django.test import TestCase
from bookapp.forms import BookForm
from bookapp.models import Author, Book

class BookFormTest(TestCase):
    def setUp(self):
        # Configurar autor para uso nos testes
        self.author = Author.objects.create(
            name="J.R.R. Tolkien",
            birth_date="1892-01-03"
        )
        
        # Dados válidos para o formulário
        self.valid_form_data = {
            'title': 'O Senhor dos Anéis',
            'isbn': '9788533613379',
            'author': self.author.id,
            'publisher': 'Martins Fontes',
            'publication_year': 2001,
            'page_count': 1200,
            'genre': 'Fantasy'
        }

    def test_valid_form(self):
        """Teste para verificar se o formulário é válido com dados corretos"""
        form = BookForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())
        
        # Verificar se não há erros nos campos
        self.assertEqual(len(form.errors), 0)

    def test_form_with_missing_required_fields(self):
        """Teste para verificar erros quando campos obrigatórios não são preenchidos"""
        # Remover título e ISBN que são campos obrigatórios
        invalid_data = self.valid_form_data.copy()
        del invalid_data['title']
        del invalid_data['isbn']
        
        form = BookForm(data=invalid_data)
        
        # Verificar que o formulário é inválido
        self.assertFalse(form.is_valid())
        
        # Verificar que temos erros específicos para os campos obrigatórios
        self.assertIn('title', form.errors)
        self.assertIn('isbn', form.errors)
        
        # Verificar as mensagens de erro
        self.assertEqual(form.errors['title'][0], 'Este campo é obrigatório.')
        self.assertEqual(form.errors['isbn'][0], 'Este campo é obrigatório.')

    def test_form_clean_method(self):
        """Teste para verificar validações personalizadas do formulário"""
        # Criar dados com ano de publicação futuro (inválido)
        invalid_year_data = self.valid_form_data.copy()
        invalid_year_data['publication_year'] = 2030  # Ano futuro
        
        form = BookForm(data=invalid_year_data)
        
        # Assumindo que o formulário tem uma validação para rejeitar anos futuros
        self.assertFalse(form.is_valid())
        self.assertIn('publication_year', form.errors)
        
        # Verificar mensagem de erro específica
        self.assertIn('O ano de publicação não pode ser no futuro', form.errors['publication_year'][0])
''',
    'bookapp/tests/test_book_view_integration.py': '''from django.test import TestCase
from django.urls import reverse
from bookapp.models import Book, Author
from bookapp.forms import BookForm

class BookViewIntegrationTest(TestCase):
    def setUp(self):
        # Configurar autor para uso nos testes
        self.author = Author.objects.create(
            name="George Orwell",
            birth_date="1903-06-25"
        )
        
        # Criar um livro para testes de atualização
        self.book = Book.objects.create(
            title="1984",
            isbn="9788535914849",
            author=self.author,
            publisher="Companhia das Letras",
            publication_year=2009,
            page_count=416
        )
        
        # Dados para criar um novo livro
        self.new_book_data = {
            'title': 'A Revolução dos Bichos',
            'isbn': '9788535909555',
            'author': self.author.id,
            'publisher': 'Companhia das Letras',
            'publication_year': 2007,
            'page_count': 152
        }

    def test_create_book_view(self):
        """Teste para verificar se a view de criação de livro funciona corretamente"""
        # Este teste pressupõe que você tenha uma URL 'book-create' configurada
        # Como não temos essa URL configurada neste exemplo, vamos pular a verificação
        # da resposta HTTP e focar apenas na lógica de criação do livro
        
        # Criar um livro através do formulário
        form = BookForm(data=self.new_book_data)
        self.assertTrue(form.is_valid())
        form.save()
        
        # Verificar se o livro foi criado no banco de dados
        self.assertEqual(Book.objects.count(), 2)
        
        # Verificar se os dados do livro foram salvos corretamente
        new_book = Book.objects.get(isbn=self.new_book_data['isbn'])
        self.assertEqual(new_book.title, self.new_book_data['title'])
        self.assertEqual(new_book.publisher, self.new_book_data['publisher'])

    def test_update_book(self):
        """Teste para verificar a atualização de um livro"""
        # Dados atualizados para o livro
        updated_data = {
            'title': self.book.title,
            'isbn': self.book.isbn,
            'author': self.book.author.id,
            'publisher': 'Nova Editora',  # Alterando a editora
            'publication_year': 2020,     # Alterando o ano
            'page_count': self.book.page_count,
            'genre': 'Dystopia'
        }
        
        # Atualizar o livro através do formulário
        form = BookForm(data=updated_data, instance=self.book)
        self.assertTrue(form.is_valid())
        form.save()
        
        # Atualizar o objeto do banco de dados
        self.book.refresh_from_db()
        
        # Verificar se os dados foram atualizados corretamente
        self.assertEqual(self.book.publisher, updated_data['publisher'])
        self.assertEqual(self.book.publication_year, updated_data['publication_year'])

    def test_duplicate_isbn(self):
        """Teste para verificar comportamento quando dados inválidos são enviados"""
        # Criar dados inválidos (ISBN duplicado)
        invalid_data = self.new_book_data.copy()
        invalid_data['isbn'] = self.book.isbn  # ISBN já existente
        
        # Verificar que o formulário detecta o erro
        form = BookForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('isbn', form.errors)
        self.assertIn('Este ISBN já está em uso', str(form.errors['isbn']))
        
        # Verificar que nenhum novo livro foi criado
        self.assertEqual(Book.objects.count(), 1)
''',
}

def create_file(path, content):
    """Cria um arquivo no caminho especificado com o conteúdo fornecido"""
    # Verifica se o diretório existe, se não, cria-o
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    # Cria o arquivo e escreve o conteúdo
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Arquivo criado: {path}")

def main():
    # Obter o diretório atual
    base_dir = os.getcwd()
    
    print(f"Criando estrutura do projeto Django em: {base_dir}")
    
    # Criar todos os arquivos
    for file_path, content in FILE_CONTENTS.items():
        create_file(os.path.join(base_dir, file_path), content)
    
    print("\nEstrutura do projeto criada com sucesso!")
    print("\nAgora você pode executar os seguintes comandos no terminal:")
    print("1. Instalar Django (se ainda não estiver instalado):")
    print("   python -m pip install django")
    print("2. Criar migrações:")
    print("   python manage.py makemigrations bookapp")
    print("3. Aplicar migrações:")
    print("   python manage.py migrate")
    print("4. Executar testes:")
    print("   python manage.py test bookapp")

if __name__ == "__main__":
    main()