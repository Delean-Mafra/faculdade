#!/usr/bin/env python
"""
Script para instalar corretamente os módulos necessários para conectar o Django ao MySQL
"""
import sys
import subprocess
import os

def run_command(command):
    """Executa um comando e retorna o resultado"""
    print(f"Executando: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode == 0

def main():
    print("\n=== Instalando os conectores MySQL necessários ===\n")
    
    # Lista de pacotes a serem instalados
    packages = [
        "pymysql",           # Driver Python puro para MySQL
        "mysql-connector-python",  # Conector oficial da Oracle
        "mysqlclient"        # Driver C para MySQL (preferido pelo Django)
    ]
    
    # Instalar cada pacote
    success = True
    for package in packages:
        print(f"\nInstalando {package}...")
        if not run_command([sys.executable, "-m", "pip", "install", "--upgrade", package]):
            success = False
            print(f"❌ Falha ao instalar {package}")
        else:
            print(f"✅ {package} instalado com sucesso")
    
    # Verificar as instalações
    print("\nVerificando instalações:")
    
    # Criar um pequeno script para verificar as importações
    test_script = """
import pymysql
import mysql.connector
try:
    import MySQLdb
    print("✅ MySQLdb importado com sucesso")
except ImportError as e:
    print("❌ Erro ao importar MySQLdb:", e)
print("✅ Todos os outros módulos importados com sucesso")
"""
    
    # Salvar o script em um arquivo temporário
    with open("test_mysql_imports.py", "w") as f:
        f.write(test_script)
    
    # Executar o script
    print("\nTestando importações...")
    run_command([sys.executable, "test_mysql_imports.py"])
    
    # Limpar o arquivo temporário
    try:
        os.remove("test_mysql_imports.py")
    except:
        pass
    
    # Configurar o PyMySQL como fallback para MySQLdb se necessário
    print("\nConfigurando PyMySQL como fallback para MySQLdb...")
    settings_path = os.path.join('descomplica', 'settings.py')
    
    with open(settings_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Adicionar código para usar PyMySQL como fallback
    pymysql_config = """
# Configurar PyMySQL como fallback para MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
"""
    
    if pymysql_config not in content:
        # Adicionar a configuração logo após as importações iniciais
        if "import os" in content:
            # Adicionar depois das importações padrão
            content = content.replace(
                "import os", 
                "import os\n" + pymysql_config
            )
        else:
            # Se não encontrar "import os", adiciona no início
            content = pymysql_config + "\n" + content
        
        with open(settings_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ PyMySQL configurado como fallback para MySQLdb em settings.py")
    else:
        print("✓ PyMySQL já está configurado como fallback")
    
    if success:
        print("\n✅ Instalação dos conectores MySQL concluída com sucesso!")
        print("\nAgora execute novamente o script de configuração MySQL:")
        print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe setup_mysql.py")
    else:
        print("\n⚠️ Alguns conectores não puderam ser instalados.")
        print("Tente executar o script setup_mysql.py mesmo assim.")

if __name__ == "__main__":
    main()