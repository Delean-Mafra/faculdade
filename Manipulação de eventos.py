import tkinter as tk
from tkinter import messagebox

# Criando a janela principal
root = tk.Tk()
root.title("Modelo de Eventos")
root.geometry("300x200")

# Definindo a função que será chamada quando o botão for clicado
def action_performed():
    print("Botão foi clicado!")
    messagebox.showinfo("Evento", "Botão foi clicado!")

# Criando o botão (equivalente ao JButton)
button = tk.Button(root, text="Clique aqui", command=action_performed)

# Posicionando o botão na janela
button.pack(pady=50)

# Iniciando o loop de eventos da interface gráfica
if __name__ == "__main__":
    root.mainloop()

import tkinter as tk

# Definir a função que será o manipulador
def quando_clicar():
    print("O botão foi clicado!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Ouvinte")

# Criar um botão com o texto "Clique!" e associar o ouvinte
botao = tk.Button(janela, text="Clique!", command=quando_clicar)
botao.pack(pady=20)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
