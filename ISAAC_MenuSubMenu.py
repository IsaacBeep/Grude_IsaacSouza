#Isaac Silva De Lima Souza

from tkinter import *

class janela:
    def __init__(self, instacia_de_Tk):
        principal = Menu(instacia_de_Tk)
        arquivo = Menu(principal)
        arquivo.add_command(label = "Abrir", command = self.abrir)
        arquivo.add_command(label = "Salvar", command = self.salvar)
        principal.add_cascade(label = "Arquivo", command = self.arquivo)
        principal.add_command(label = "Ajuda", command = self.ajuda)
        instacia_de_Tk.configure(Menu = principal)

    def abrir(self):print,"abrir"
    def salvar(self):print,"salvar"
    def ajuda(self):print,"ajuda"

raiz = Tk()
janela(raiz)
raiz.mainloop()

