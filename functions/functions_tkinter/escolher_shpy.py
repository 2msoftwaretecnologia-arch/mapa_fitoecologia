import tkinter as tk
from tkinter import filedialog

def escolher_shp(title):
    """Abre uma janela para selecionar um arquivo SHP e retorna o caminho."""
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    
    caminho_arquivo = filedialog.askopenfilename(
        title=title,
        filetypes=[("Shapefile", "*.shp")]
    )
    
    root.destroy()  # Fecha a janela do Tkinter
    return caminho_arquivo if caminho_arquivo else None


