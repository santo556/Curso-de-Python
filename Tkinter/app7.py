# Label widget e como funciona o pack
from tkinter import *
menu_inicial = Tk()
menu_inicial.title("Título")

label_1 = Label(menu_inicial, text="Saudações. Olá, Mundo!")
label_2 = Label(menu_inicial, text="Estou aprendendo python.")
cmd = Button(menu_inicial, text="Executar")

# pack
cmd.pack()
label_2.pack()
label_1.pack()

menu_inicial.mainloop()
