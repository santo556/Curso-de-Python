import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Interface Completa")

        self.label = tk.Label(master, text="Esta é a nossa interface completa!")
        self.label.pack()

        self.greet_button = tk.Button(master, text="Cumprimentar", command=self.greet)
        self.greet_button.pack()

        self.close_button = tk.Button(master, text="Fechar", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Saudações!")

root = tk.Tk()
my_app = App(root)
root.mainloop()