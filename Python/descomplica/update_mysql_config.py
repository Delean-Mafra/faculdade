#!/usr/bin/env python
"""
Script para atualizar as credenciais do MySQL e preparar o banco de dados
"""
import os
import sys
import subprocess
import mysql.connector
from mysql.connector import errorcode

# Novas configurações do MySQL
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'DB_EMPRESA'
}

def update_settings_file():
    """Atualiza o arquivo settings.py com as novas credenciais do MySQL"""
    settings_path = os.path.join('descomplica', 'settings.py')
    
    try:
        with open(settings_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Procura e substitui as credenciais do banco de dados
        if "'PASSWORD':" in content:
            # Substitui a senha antiga pela nova
            content = content.replace(
                "'PASSWORD': 'Brasil101@'", 
                f"'PASSWORD': '{MYSQL_CONFIG['password']}'"
            )
            
            # Se a senha Brasil101@ não for encontrada, tenta substituir qualquer senha
            if "'PASSWORD': 'Brasil101@'" not in content:
                import re
                pattern = r"'PASSWORD':\s*'[^']*'"
                content = re.sub(pattern, f"'PASSWORD': '{MYSQL_CONFIG['password']}'", content)
            
            with open(settings_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print("✅ Credenciais do MySQL atualizadas no settings.py")
            return True
        else:
            print("❌ Não foi possível encontrar a configuração do banco de dados no settings.py")
            return False
    
    except Exception as e:
        print(f"❌ Erro ao atualizar o arquivo settings.py: {str(e)}")
        return False

def test_mysql_connection():
    """Testa a conexão com o MySQL usando as novas credenciais"""
    print(f"\nTestando conexão com MySQL ({MYSQL_CONFIG['host']}, usuário: {MYSQL_CONFIG['user']})...")
    
    try:
        # Tenta conectar sem especificar o banco de dados
        conn = mysql.connector.connect(
            host=MYSQL_CONFIG['host'],
            user=MYSQL_CONFIG['user'],
            password=MYSQL_CONFIG['password']
        )
        
        print("✅ Conexão com MySQL estabelecida com sucesso!")
        
        # Verifica se o banco de dados existe
        cursor = conn.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{MYSQL_CONFIG['database']}'")
        result = cursor.fetchone()
        
        if result:
            print(f"✓ Banco de dados '{MYSQL_CONFIG['database']}' já existe")
        else:
            print(f"⚠️ Banco de dados '{MYSQL_CONFIG['database']}' não existe, criando...")
            cursor.execute(f"CREATE DATABASE {MYSQL_CONFIG['database']} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"✅ Banco de dados '{MYSQL_CONFIG['database']}' criado com sucesso")
        
        cursor.close()
        conn.close()
        return True
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("❌ Acesso negado: verifique nome de usuário e senha")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"❌ Banco de dados '{MYSQL_CONFIG['database']}' não existe e não foi possível criá-lo")
        else:
            print(f"❌ Erro ao conectar ao MySQL: {err}")
        return False

def run_migrations():
    """Executa as migrações do Django no banco de dados"""
    print("\nAplicando migrações ao banco de dados...")
    
    result = subprocess.run(
        [sys.executable, "manage.py", "migrate"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✅ Migrações aplicadas com sucesso")
        return True
    else:
        print(f"❌ Erro ao aplicar migrações: {result.stderr}")
        return False

def main():
    print("\n=== Atualizando configuração do MySQL ===\n")
    
    # Atualiza o arquivo settings.py
    if not update_settings_file():
        print("\n❌ Falha na atualização das credenciais")
        return
    
    # Testa a conexão com o MySQL
    if not test_mysql_connection():
        print("\n❌ Falha na conexão com o MySQL")
        print("Verifique se o servidor MySQL está em execução e se as credenciais estão corretas.")
        return
    
    # Executa as migrações
    if not run_migrations():
        print("\n❌ Falha ao aplicar as migrações")
        return
    
    print("\n✅ Configuração do MySQL atualizada com sucesso!")
    print("\nAgora você pode popular o banco de dados com dados fictícios executando:")
    print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe populate_mysql.py")
    print("\nOu iniciar o servidor Django:")
    print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe manage.py runserver")

if __name__ == "__main__":
    main()