from tkinter import *
# Tamanho máximo, mínimo e definição de ícone
menu_inicial = Tk()
menu_inicial.title("Terceira Aplicação")

menu_inicial.geometry("500x250+200+200")
menu_inicial.resizable(True, True)

# para a janela aparecer maxinizada
# menu_inicial.state("zoomed")

# adicionar ícone
# menu_inicial.state("iconic")
menu_inicial.iconbitmap("Tkinter/Imagens/internet-web-browser-icon.svg")

# menu_inicial.minsize(width = 500, height = 250)
# menu_inicial.maxsize(700, 400)

menu_inicial.mainloop()