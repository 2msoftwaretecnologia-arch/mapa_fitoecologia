import tkinter as tk

root = tk.Tk()
root.title("Janela Principal")

def abrir_janela2():
    win2 = tk.Toplevel(root)
    win2.title("Outra janela")
    tk.Label(win2, text="Sou a segunda janela").pack()

tk.Button(root, text="Abrir outra janela", command=abrir_janela2).pack()
root.mainloop()
