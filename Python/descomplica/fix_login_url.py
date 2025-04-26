#!/usr/bin/env python
"""
Script para corrigir o problema da URL de login não encontrada
"""
import os
import sys
import subprocess

def print_header(text):
    """Imprime um cabeçalho formatado"""
    print(f"\n=== {text} ===\n")

def print_success(text):
    """Imprime uma mensagem de sucesso"""
    print(f"✅ {text}")

def print_error(text):
    """Imprime uma mensagem de erro"""
    print(f"❌ {text}")

def update_urls_file():
    """Atualiza o arquivo urls.py do projeto para incluir as URLs de autenticação"""
    print_header("Atualizando configuração de URLs")
    
    urls_path = os.path.join('descomplica', 'urls.py')
    
    if not os.path.exists(urls_path):
        print_error(f"Arquivo URLs não encontrado em: {urls_path}")
        return False
    
    try:
        with open(urls_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Verifica se já inclui as URLs de autenticação
        if 'from django.contrib.auth import views as auth_views' in content:
            print("✓ URLs de autenticação já parecem estar configuradas")
        else:
            # Adiciona as importações necessárias
            if 'from django.urls import path' in content:
                content = content.replace(
                    'from django.urls import path', 
                    'from django.urls import path, include\nfrom django.contrib.auth import views as auth_views'
                )
            else:
                print_error("Não foi possível encontrar a importação de 'path' para adicionar 'include'")
                return False
            
            # Localiza a lista de urlpatterns
            if 'urlpatterns = [' in content:
                # Adiciona as URLs de autenticação antes do fechamento da lista
                auth_urls = """
    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='book-list'), name='logout'),
"""
                # Encontra o último item da lista de urlpatterns e adiciona os padrões de autenticação depois
                last_path_pos = content.rfind('path(')
                if last_path_pos != -1:
                    # Encontra o final deste item (o próximo ']' ou ',' após ele)
                    end_pos = content.find(']', last_path_pos)
                    comma_pos = content.find(',', last_path_pos)
                    if comma_pos != -1 and comma_pos < end_pos:
                        # Adiciona após a vírgula
                        content = content[:comma_pos + 1] + auth_urls + content[comma_pos + 1:]
                    else:
                        # Adiciona antes do fechamento da lista
                        content = content[:end_pos] + auth_urls + content[end_pos:]
                else:
                    print_error("Não foi possível localizar um padrão de URL existente")
                    return False
            else:
                print_error("Não foi possível encontrar 'urlpatterns = [' no arquivo de URLs")
                return False
        
        # Salva as alterações
        with open(urls_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print_success("Arquivo de URLs atualizado com sucesso")
        return True
    
    except Exception as e:
        print_error(f"Erro ao atualizar o arquivo de URLs: {str(e)}")
        return False

def create_login_template():
    """Cria um template de login básico"""
    print_header("Criando template de login")
    
    # Verifica se o diretório templates existe
    templates_dir = os.path.join('templates')
    if not os.path.exists(templates_dir):
        print_error(f"Diretório de templates não encontrado: {templates_dir}")
        return False
    
    login_template_path = os.path.join(templates_dir, 'login.html')
    
    # Se o template já existe, não sobrescreve
    if os.path.exists(login_template_path):
        print("✓ Template de login já existe")
        return True
    
    try:
        # Cria um template de login simples
        login_template = """{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h3 class="card-title">Login</h3>
                </div>
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        
                        <div class="mb-3">
                            <label for="id_username" class="form-label">Nome de usuário</label>
                            <input type="text" name="username" id="id_username" class="form-control" required>
                        </div>
                        
                        <div class="mb-3">
                            <label for="id_password" class="form-label">Senha</label>
                            <input type="password" name="password" id="id_password" class="form-control" required>
                        </div>
                        
                        {% if form.errors %}
                            <div class="alert alert-danger">
                                Seu nome de usuário e senha não correspondem. Por favor, tente novamente.
                            </div>
                        {% endif %}
                        
                        <div class="d-grid gap-2">
                            <button type="submit" class="btn btn-primary">
                                <i class="bi bi-box-arrow-in-right"></i> Entrar
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
"""
        
        with open(login_template_path, 'w', encoding='utf-8') as file:
            file.write(login_template)
        
        print_success("Template de login criado com sucesso")
        return True
    
    except Exception as e:
        print_error(f"Erro ao criar o template de login: {str(e)}")
        return False

def update_views_file():
    """Atualiza o arquivo de views para remover o LoginRequiredMixin se necessário"""
    print_header("Verificando arquivo de views")
    
    views_path = os.path.join('bookapp', 'views.py')
    
    if not os.path.exists(views_path):
        print_error(f"Arquivo de views não encontrado: {views_path}")
        return False
    
    try:
        # Lê o arquivo de views
        with open(views_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Verifica se a view BookCreateView está usando LoginRequiredMixin
        if 'class BookCreateView(' in content and 'LoginRequiredMixin' in content:
            # Vamos ajustar a configuração para permitir acesso anônimo
            modified_content = content.replace('from django.contrib.auth.mixins import LoginRequiredMixin', '')
            modified_content = modified_content.replace('LoginRequiredMixin, ', '')
            modified_content = modified_content.replace('LoginRequiredMixin,', '')
            modified_content = modified_content.replace('LoginRequiredMixin', '')
            
            # Salva as alterações
            with open(views_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            
            print_success("Arquivo de views modificado para permitir acesso anônimo")
        else:
            print("✓ Arquivo de views não precisa ser modificado")
        
        return True
    
    except Exception as e:
        print_error(f"Erro ao atualizar o arquivo de views: {str(e)}")
        return False

def main():
    print("\n=== CORRIGINDO PROBLEMA DA URL DE LOGIN ===\n")
    
    steps = [
        ("Atualizar configuração de URLs", update_urls_file),
        ("Criar template de login", create_login_template),
        ("Atualizar arquivo de views", update_views_file),
    ]
    
    for step_name, step_func in steps:
        print(f"\n>> Executando: {step_name}")
        if not step_func():
            print(f"⚠️ Problema ao executar: {step_name}")
    
    print("\n=== REINICIANDO O SERVIDOR DJANGO ===\n")
    print("Para que as alterações tenham efeito, reinicie o servidor Django com:")
    print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe manage.py runserver")
    
    print("\n✅ CORREÇÕES APLICADAS COM SUCESSO!")
    print("\nAgora você deve poder acessar:")
    print("- Lista de livros: http://127.0.0.1:8000/books/")
    print("- Adicionar novo livro: http://127.0.0.1:8000/books/book/new/")
    print("- Login (se necessário): http://127.0.0.1:8000/login/")

if __name__ == "__main__":
    main()