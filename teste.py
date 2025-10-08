import tkinter as tk
from tkinter import filedialog
import os

def selecionar_pasta(pasta_inicial: str = None) -> str:
    """
    Abre uma janela para o usuário selecionar uma pasta.
    Caso o parâmetro seja um arquivo, o caminho será ajustado
    automaticamente para a pasta onde o arquivo está.

    Parâmetros:
        pasta_inicial (str): Caminho inicial (pode ser pasta ou arquivo).

    Retorna:
        str: Caminho completo da pasta selecionada com barra invertida no final.
    """
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter

    # Define pasta inicial padrão
    if not pasta_inicial:
        pasta_inicial = "C:\\"
    else:
        # Se for arquivo, converte para a pasta onde ele está
        if os.path.isfile(pasta_inicial):
            pasta_inicial = os.path.dirname(pasta_inicial)

    # Abre o seletor de pastas
    caminho_pasta = filedialog.askdirectory(
        initialdir=pasta_inicial,
        title="Selecione uma pasta"
    )

    # Se o usuário cancelar
    if not caminho_pasta:
        return ""

    # Normaliza para barras invertidas e garante barra final
    caminho_pasta = os.path.normpath(caminho_pasta) + "\\"

    return caminho_pasta
