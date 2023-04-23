# Alterar propriedades e adicionar um botão

from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Título")
menu_inicial['bg']  = "black"
menu_inicial.geometry("500x300")

# botão
btn = Button(menu_inicial, text="Executar")
btn.pack()

menu_inicial.mainloop()