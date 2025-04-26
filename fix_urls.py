#!/usr/bin/env python
"""
Script para corrigir o arquivo urls.py com erro de importação
"""
import os

def print_header(text):
    """Imprime um cabeçalho formatado"""
    print(f"\n=== {text} ===\n")

def print_success(text):
    """Imprime uma mensagem de sucesso"""
    print(f"✅ {text}")

def print_error(text):
    """Imprime uma mensagem de erro"""
    print(f"❌ {text}")

def fix_urls_file():
    """Corrige o arquivo urls.py"""
    print_header("Corrigindo arquivo urls.py")
    
    urls_path = os.path.join('descomplica', 'urls.py')
    
    if not os.path.exists(urls_path):
        print_error(f"Arquivo urls.py não encontrado em: {urls_path}")
        return False
    
    try:
        # Lê o conteúdo atual do arquivo
        with open(urls_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Verifica se há erro de importação
        if 'from django.contrib.auth import views as auth_views, include' in content:
            # Corrige a importação
            content = content.replace(
                'from django.contrib.auth import views as auth_views, include',
                'from django.urls import path, include\nfrom django.contrib.auth import views as auth_views'
            )
            
            # Salva o arquivo corrigido
            with open(urls_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print_success("Erro de importação corrigido em urls.py")
            return True
        
        # Se não encontrar o erro específico, cria um arquivo completamente novo
        new_urls_content = """from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('bookapp.urls')),
    
    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='book-list'), name='logout'),
]
"""
        
        # Salva o novo conteúdo
        with open(urls_path, 'w', encoding='utf-8') as file:
            file.write(new_urls_content)
        
        print_success("Arquivo urls.py reescrito com configuração correta")
        return True
        
    except Exception as e:
        print_error(f"Erro ao corrigir o arquivo urls.py: {str(e)}")
        return False

if __name__ == "__main__":
    print("\n=== CORRIGINDO ERRO DE IMPORTAÇÃO ===\n")
    
    if fix_urls_file():
        print("\n✅ ARQUIVO URLS.PY CORRIGIDO COM SUCESSO!")
        print("\nAgora reinicie o servidor Django com:")
        print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe manage.py runserver")
        print("\nVocê deverá poder acessar:")
        print("- Lista de livros: http://127.0.0.1:8000/books/")
        print("- Adicionar novo livro: http://127.0.0.1:8000/books/book/new/")
        print("- Login (se necessário): http://127.0.0.1:8000/login/")
    else:
        print("\n❌ FALHA AO CORRIGIR O ARQUIVO URLS.PY")