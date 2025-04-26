#!/usr/bin/env python
"""
Script para reconstruir completamente o arquivo urls.py
"""
import os

def print_success(text):
    """Imprime uma mensagem de sucesso"""
    print(f"✅ {text}")

def print_error(text):
    """Imprime uma mensagem de erro"""
    print(f"❌ {text}")

def fix_urls_file():
    """Recria completamente o arquivo urls.py com a configuração correta"""
    print("\n=== Reconstruindo arquivo urls.py ===\n")
    
    urls_path = os.path.join('descomplica', 'urls.py')
    
    # Conteúdo correto para o arquivo urls.py
    correct_content = """from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('bookapp.urls')),
    
    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='book-list'), name='logout'),
    
    # Redirecionar a raiz para /books/
    path('', RedirectView.as_view(url='books/', permanent=True)),
]
"""
    
    try:
        # Salva o arquivo com o conteúdo correto
        with open(urls_path, 'w', encoding='utf-8') as file:
            file.write(correct_content)
        
        print_success("Arquivo urls.py reconstruído com sucesso")
        return True
        
    except Exception as e:
        print_error(f"Erro ao reconstruir o arquivo urls.py: {str(e)}")
        return False

if __name__ == "__main__":
    print("\n=== CORREÇÃO DEFINITIVA DO ARQUIVO URLS.PY ===\n")
    
    if fix_urls_file():
        print("\n✅ ARQUIVO URLS.PY CORRIGIDO COM SUCESSO!")
        print("\nAgora reinicie o servidor Django com:")
        print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe manage.py runserver")
        print("\nVocê deverá poder acessar:")
        print("- Página inicial (redirecionamento): http://127.0.0.1:8000/")
        print("- Lista de livros: http://127.0.0.1:8000/books/")
        print("- Adicionar novo livro: http://127.0.0.1:8000/books/book/new/")
        print("- Login (se necessário): http://127.0.0.1:8000/login/")
    else:
        print("\n❌ FALHA AO CORRIGIR O ARQUIVO URLS.PY")