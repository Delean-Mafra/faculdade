import sqlite3


# Exemplo de Introdução aos padrões de projeto para persistência de dados em Python
# Definindo o decorator
def meu_decorator(funcao):
    def wrapper():
        print("Executando algo antes da função original.")
        funcao()
        print("Executando algo depois da função original.")
    return wrapper

# Usando o decorator em uma função
@meu_decorator
def minha_funcao():
    print("Esta é a função original.")

# Chamando a função decorada
minha_funcao()



# Exemplo de Implementação de padrões de projeto

class UsuarioDAO:
    def __init__(self, db_file):
        self.db_file = db_file

    def conectar(self):
        return sqlite3.connect(self.db_file)

    def criar_usuario(self, nome, email):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        conn.close()

    def obter_usuario(self, usuario_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (usuario_id,))
        usuario = cursor.fetchone()
        conn.close()
        return usuario

    def atualizar_usuario(self, usuario_id, nome, email):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (nome, email, usuario_id))
        conn.commit()
        conn.close()

    def deletar_usuario(self, usuario_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
        conn.commit()
        conn.close()


# Instancia o DAO
usuario_dao = UsuarioDAO('exemplo.db')

# Cria um novo usuário
usuario_dao.criar_usuario('Alice', 'alice@exemplo.com')

# Obtém os dados de um usuário
usuario = usuario_dao.obter_usuario(1)
print(usuario)  # Output: (1, 'Alice', 'alice@exemplo.com')

# Atualiza os dados do usuário
usuario_dao.atualizar_usuario(1, 'Alice Silva', 'alice.silva@exemplo.com')

# Deleta um usuário
usuario_dao.deletar_usuario(1)
