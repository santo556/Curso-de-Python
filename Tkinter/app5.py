# Associar evento a um botão
from tkinter import *

menu_inicial = Tk()
menu_inicial.title()
menu_inicial.geometry("500x300")

# está função vem antes do comando cmd_Click
def cmd_Click(mansagem):
    print(mansagem)

# botão
cmd = Button(menu_inicial, text="Executar", command=lambda: print('OK'))
cmd.pack()

cmd = Button(menu_inicial, text="Clicar", command=lambda: cmd_Click("Estou Aprendendo Python."))
cmd.pack()

menu_inicial.mainloop()