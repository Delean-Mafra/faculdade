#!/usr/bin/env python
"""
Este script configura o projeto Django para usar MySQL como banco de dados.
Ele cria o banco de dados MySQL, modifica settings.py e aplica as migrações.
"""
import os
import sys
import subprocess
import time
import mysql.connector
from mysql.connector import errorcode

# Configurações do MySQL
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'DB_EMPRESA'
}

def check_mysql():
    """Verifica se o módulo mysql-connector está instalado"""
    try:
        import mysql.connector
        print("✓ MySQL Connector instalado")
        return True
    except ImportError:
        print("❌ MySQL Connector não está instalado")
        
        # Tenta instalar o módulo
        print("\nInstalando mysql-connector-python...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "mysql-connector-python"],
            capture_output=True, 
            text=True
        )
        
        if result.returncode == 0:
            print("✅ MySQL Connector instalado com sucesso")
            return True
        else:
            print(f"❌ Falha ao instalar MySQL Connector: {result.stderr}")
            return False

def check_mysqlclient():
    """Verifica se o módulo mysqlclient está instalado (necessário para Django)"""
    try:
        
        print("✓ mysqlclient já está instalado")
        return True
    except ImportError:
        print("❌ mysqlclient não está instalado")
        
        # Tenta instalar o módulo
        print("\nInstalando mysqlclient...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "mysqlclient"],
            capture_output=True, 
            text=True
        )
        
        if result.returncode == 0:
            print("✅ mysqlclient instalado com sucesso")
            return True
        else:
            print(f"❌ Falha ao instalar mysqlclient: {result.stderr}")
            print("\nVocê pode precisar instalar bibliotecas de desenvolvimento do MySQL.")
            print("No Windows, tente instalar: pip install mysqlclient")
            print("No Linux, execute: sudo apt-get install python3-dev default-libmysqlclient-dev build-essential")
            return False

def create_database():
    """Cria o banco de dados MySQL se ele não existir"""
    try:
        # Primeiro tenta se conectar sem especificar o banco de dados
        conn = mysql.connector.connect(
            host=MYSQL_CONFIG['host'],
            user=MYSQL_CONFIG['user'],
            password=MYSQL_CONFIG['password']
        )
        cursor = conn.cursor()
        
        # Verifica se o banco de dados já existe
        cursor.execute(f"SHOW DATABASES LIKE '{MYSQL_CONFIG['database']}'")
        result = cursor.fetchone()
        
        if result:
            print(f"✓ Banco de dados '{MYSQL_CONFIG['database']}' já existe")
        else:
            # Cria o banco de dados
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

def update_settings_file():
    """Atualiza o arquivo settings.py para usar MySQL"""
    settings_path = os.path.join('descomplica', 'settings.py')
    
    with open(settings_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Localiza a seção DATABASES e substitui por configuração MySQL
    sqlite_config = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""
    
    mysql_config = f"""DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{MYSQL_CONFIG['database']}',
        'USER': '{MYSQL_CONFIG['user']}',
        'PASSWORD': '{MYSQL_CONFIG['password']}',
        'HOST': '{MYSQL_CONFIG['host']}',
        'PORT': '3306',
        'OPTIONS': {{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }},
    }}
}}"""
    
    if sqlite_config in content:
        content = content.replace(sqlite_config, mysql_config)
        
        with open(settings_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print("✅ Configuração do banco de dados atualizada para MySQL no settings.py")
        return True
    else:
        print("❌ Não foi possível encontrar a configuração padrão do SQLite no settings.py")
        print("Por favor, atualize manualmente o arquivo settings.py para usar MySQL")
        return False

def migrate_database():
    """Aplica as migrações ao banco de dados MySQL"""
    print("\nAplicando migrações ao banco de dados MySQL...")
    
    # Espera um pouco para garantir que o mysqlclient seja carregado corretamente
    time.sleep(1)
    
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
    print("\n=== Configurando MySQL para o projeto Django ===\n")
    
    # Verifica e instala dependências
    if not check_mysql() or not check_mysqlclient():
        print("\n❌ Falha na instalação das dependências necessárias")
        return
    
    # Cria o banco de dados
    if not create_database():
        print("\n❌ Falha na criação do banco de dados")
        return
    
    # Atualiza o arquivo settings.py
    if not update_settings_file():
        print("\n❌ Falha na atualização do arquivo settings.py")
        return
    
    # Aplica migrações
    if not migrate_database():
        print("\n❌ Falha ao aplicar as migrações")
        return
    
    print("\n✅ Configuração do MySQL concluída com sucesso!")
    print("\nAgora você pode popular o banco de dados com dados fictícios executando:")
    print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe populate_mysql.py")

if __name__ == "__main__":
    main()