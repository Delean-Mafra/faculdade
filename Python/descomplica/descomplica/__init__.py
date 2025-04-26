try:
    import pymysql
    pymysql.install_as_MySQLdb()
    print("PyMySQL instalado como MySQLdb")
except ImportError:
    print("PyMySQL não está disponível, usando outro backend")
