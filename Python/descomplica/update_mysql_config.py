#!/usr/bin/env python
"""
Script para atualizar as credenciais do MySQL e preparar o banco de dados
"""
import os
import sys
import subprocess
import mysql.connector
from mysql.connector import errorcode
import re

# Novas configurações do MySQL (buscando de variáveis de ambiente para segurança)
MYSQL_CONFIG = {
    'host': os.environ.get('MYSQL_HOST', 'localhost'),
    'user': os.environ.get('MYSQL_USER', 'root'),
    'password': os.environ.get('MYSQL_PASSWORD', ''),
    'database': os.environ.get('MYSQL_DATABASE', 'DB_EMPRESA')
}

def update_settings_file():
    """Atualiza o arquivo settings.py com as novas credenciais do MySQL"""
    settings_path = os.path.join('descomplica', 'settings.py')
    try:
        with open(settings_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Garante que o os está importado para podermos injetar os.environ no settings.py
        if "import os" not in content:
            content = "import os\n" + content
            
        # Procura e substitui as credenciais do banco de dados
        if "'PASSWORD':" in content:
            # Substitui a senha antiga pela chamada à variável de ambiente, evitando texto claro no arquivo
            if "'PASSWORD': 'Brasil101@'" in content:
                content = content.replace("'PASSWORD': 'Brasil101@'", "'PASSWORD': os.environ.get('MYSQL_PASSWORD', '')")
            else:
                # Se a senha padrão não for encontrada, tenta substituir qualquer senha
                pattern = r"'PASSWORD':\s*'[^']*'"
                content = re.sub(pattern, r"'PASSWORD': os.environ.get('MYSQL_PASSWORD', '')", content)
        
        with open(settings_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print("✅ Credenciais do MySQL atualizadas no settings.py de forma segura")
        return True
    except Exception as e:
        print(f"❌ Erro ao atualizar settings.py: {e}")
        return False

def main():
    if not MYSQL_CONFIG['password']:
        print("⚠️ Aviso: A variável de ambiente MYSQL_PASSWORD não está definida. O script pode falhar ao conectar no banco.")
    update_settings_file()

if __name__ == "__main__":
    main()
