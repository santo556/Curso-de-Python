import tkinter as tk

root = tk.Tk()
root.title("Janela Simples")

label = tk.Label(root, text="Olá, mundo!")
label.pack()

root.mainloop()