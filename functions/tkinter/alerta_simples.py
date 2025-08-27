import tkinter as tk
from tkinter import messagebox

def janela_dinamica(texto='Pressione OK para continuar'):
    # Deve ser chamado na main thread
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Atenção", texto, parent=root)  # parent ajuda a evitar janelas “soltas”
    root.destroy()


