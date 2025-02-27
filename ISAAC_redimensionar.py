from tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):
        top = Frame(); top.pack()
        a = Label(top, text = "A"); a.pack(side = "left", fill = "y")
        b = Label(top, text = "B"); b.pack(side = "bottom", fill = "x")
        c = Label(top, text = "C"); c.pack(side = "right")
        d = Label(top, text = "D"); d.pack(side = "top")

        for widget in (a,b,c,d):
            widget.configure(rellef = "groove", border = 10, font = "times 24 bold")

raiz = Tk()
Janela(raiz)
raiz.mainloop()
