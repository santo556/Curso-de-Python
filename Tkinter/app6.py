# Centrar o formulário do screen
from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Título")

# dimensões da janela
largura = 500
altura = 300

# resolução do nosso sistema
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()

# posição da janela
posx = largura_screen / 2 - largura / 2
posy = altura_screen /2 - altura / 2

# definir a geometry
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

print(largura_screen, altura_screen)

menu_inicial.mainloop()