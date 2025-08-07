import tkinter as tk
from tkinter import messagebox

def janela_dinamica(texto='Pressione OK para continuar'):
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    messagebox.showinfo("Atenção", texto)
    root.destroy()  # Destroi a janela oculta após o alerta
