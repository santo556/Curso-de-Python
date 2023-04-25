# Alterar cores e tipo de letra
from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Título")
menu_inicial.geometry("500x300")

label_1 = Label(menu_inicial, 
                text="Este é o label 1",
                bg="#ff8080")
label_1.pack()

menu_inicial.mainloop()