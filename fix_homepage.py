import os

def fix_homepage():
    """Adiciona uma página inicial ao projeto"""
    urls_path = 'descomplica/urls.py'
    
    try:
        # Ler o conteúdo atual do arquivo
        with open(urls_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Verificar se já tem um redirecionamento para a página inicial
        if 'RedirectView.as_view' not in content:
            # Substitui o conteúdo do arquivo para incluir um redirecionamento
            new_content = '''"""
URL configuration for descomplica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('bookapp.urls')),
    # Redirecionar a URL raiz para a página de livros
    path('', RedirectView.as_view(url='books/', permanent=True)),
]
'''
            with open(urls_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"✓ URL raiz configurada para redirecionar para /books/")
            return True
        else:
            print("A URL raiz já está configurada para redirecionamento.")
            return True
            
    except Exception as e:
        print(f"❌ Erro ao corrigir o arquivo {urls_path}: {str(e)}")
        return False

if __name__ == "__main__":
    success = fix_homepage()
    if success:
        print("\nAgora reinicie o servidor e acesse http://127.0.0.1:8000/")
        print("\nPara criar um superusuário, siga os passos:")
        print("1. Digite o nome de usuário (ou pressione ENTER para usar seu nome atual)")
        print("2. Digite um endereço de email (opcional)")
        print("3. Digite uma senha e confirme-a")
    else:
        print("\nOcorreu um erro ao configurar a página inicial.")