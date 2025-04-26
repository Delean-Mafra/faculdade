#!/usr/bin/env python
"""
Este script configura o PyMySQL como substituto para o MySQLdb no Django.
PyMySQL é uma implementação pura de Python do cliente MySQL, que funciona bem
quando há problemas com o mysqlclient (que é uma implementação em C).
"""
import os
import sys
import subprocess
import importlib.util

def install_package(package):
    """Instala um pacote Python usando pip"""
    print(f"Instalando {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print(f"✅ {package} instalado com sucesso")

def check_package(package_name):
    """Verifica se um pacote está instalado"""
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(f"❌ {package_name} não está instalado")
        return False
    print(f"✓ {package_name} está instalado")
    return True

def update_init_file():
    """
    Cria ou atualiza o arquivo __init__.py no diretório do projeto
    para configurar o PyMySQL como substituto do MySQLdb
    """
    init_path = os.path.join('descomplica', '__init__.py')
    pymysql_config = """import pymysql

# Configure PyMySQL como substituto para o MySQLdb
pymysql.install_as_MySQLdb()
"""
    
    # Verifica se o arquivo existe e tem o conteúdo necessário
    content = ""
    if os.path.exists(init_path):
        with open(init_path, 'r', encoding='utf-8') as file:
            content = file.read()
    
    if "pymysql.install_as_MySQLdb()" not in content:
        # Cria ou atualiza o arquivo
        with open(init_path, 'w', encoding='utf-8') as file:
            file.write(pymysql_config)
        print(f"✅ Arquivo {init_path} criado/atualizado com configuração PyMySQL")
    else:
        print(f"✓ Arquivo {init_path} já possui configuração PyMySQL")
    
    return True

def update_settings_file():
    """Verifica e atualiza o engine no settings.py"""
    settings_path = os.path.join('descomplica', 'settings.py')
    
    with open(settings_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Verifica se está usando o backend MySQL e atualiza para as configurações corretas
    if "'ENGINE': 'django.db.backends.mysql'" in content:
        # Já está configurado para MySQL
        print("✓ settings.py já está configurado para usar MySQL")

        # Atualiza as credenciais se necessário
        if "'PASSWORD':" in content and "'PASSWORD': 'root'" not in content:
            import re
            pattern = r"'PASSWORD':\s*'[^']*'"
            content = re.sub(pattern, "'PASSWORD': 'root'", content)
            
            with open(settings_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print("✅ Credenciais atualizadas no settings.py")
        
        return True
    else:
        # Precisamos configurar para MySQL
        print("❌ settings.py não está configurado para usar MySQL")
        print("Por favor, execute o script update_mysql_config.py depois")
        return False

def run_migrations():
    """Executa as migrações do Django"""
    print("\nAplicando migrações ao banco de dados...")
    
    try:
        result = subprocess.run(
            [sys.executable, "manage.py", "migrate"],
            check=True
        )
        print("✅ Migrações aplicadas com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao aplicar migrações: {e}")
        return False

def main():
    print("\n=== Configurando PyMySQL como substituto para MySQLdb ===\n")
    
    # Verificar e instalar PyMySQL se necessário
    if not check_package("pymysql"):
        try:
            install_package("pymysql")
        except Exception as e:
            print(f"❌ Erro ao instalar PyMySQL: {e}")
            return
    
    # Atualizar o arquivo __init__.py
    if not update_init_file():
        print("❌ Falha ao configurar PyMySQL no arquivo __init__.py")
        return
    
    # Verificar configuração do settings.py
    update_settings_file()
    
    # Executar migrações
    if run_migrations():
        print("\n✅ Configuração concluída com sucesso!")
        print("\nAgora você pode popular o banco de dados com dados fictícios:")
        print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe populate_mysql.py")
        print("\nOu iniciar o servidor Django:")
        print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe manage.py runserver")
    else:
        print("\n❌ Falha ao aplicar migrações")
        print("Mas a configuração do PyMySQL foi concluída. Tente executar as migrações manualmente:")
        print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe manage.py migrate")

if __name__ == "__main__":
    main()