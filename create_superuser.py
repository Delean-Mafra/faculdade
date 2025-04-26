#!/usr/bin/env python
"""
Script para criar um superusuário automaticamente com uma senha predefinida.
Para uso apenas em ambiente de desenvolvimento/teste.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'descomplica.settings')
django.setup()

from django.contrib.auth.models import User
from django.db import IntegrityError

def create_superuser(username, email, password):
    try:
        # Verifica se o usuário já existe
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            print(f"\n✓ A senha do usuário '{username}' foi atualizada.")
        else:
            # Cria um novo superusuário
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"\n✓ Superusuário '{username}' criado com sucesso.")
        
        print(f"\nAgora você pode fazer login em http://127.0.0.1:8000/admin/ com:")
        print(f"Usuário: {username}")
        print(f"Senha: {password}")
        return True
    
    except IntegrityError:
        print(f"\n❌ Erro: O usuário '{username}' já existe, mas houve um problema ao atualizar a senha.")
        return False
    
    except Exception as e:
        print(f"\n❌ Erro ao criar superusuário: {str(e)}")
        return False

if __name__ == "__main__":
    # Dados do superusuário para teste
    username = 'admin'  # Nome de usuário padrão
    email = 'admin@example.com'  # Email padrão
    password = '123456Ab'  # Senha padrão para teste (NÃO use em produção!)
    
    print("\n====== CRIANDO SUPERUSUÁRIO PARA TESTE ======")
    print("\nATENÇÃO: Este script cria um superusuário com senha padrão.")
    print("Isso é adequado APENAS para ambientes de teste/desenvolvimento.")
    print("NUNCA use este script ou senhas simples em produção!")
    
    # Se o usuário quiser personalizar os dados
    custom = input("\nDeseja personalizar os dados? (s/N): ").strip().lower()
    
    if custom == 's' or custom == 'sim':
        input_username = input(f"Nome de usuário [{username}]: ").strip()
        if input_username:
            username = input_username
            
        input_email = input(f"Email [{email}]: ").strip()
        if input_email:
            email = input_email
    
    create_superuser(username, email, password)