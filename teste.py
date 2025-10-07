<<<<<<< HEAD
from functions.interfaces.input_de_cidade import *
from functions.interfaces.formulario_inicial import *

formulario_incial()
=======
import tkinter as tk
from tkinter import filedialog
import os

def selecionar_pasta(pasta_inicial: str = None) -> str:
    """
    Abre uma janela para o usuário selecionar uma pasta.
    A janela será aberta já dentro da pasta_inicial (se existir).

    Parâmetros:
        pasta_inicial (str): Caminho inicial onde a janela abrirá.

    Retorna:
        str: Caminho completo da pasta selecionada com barra invertida no final.
    """
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter

    # Se não for informada uma pasta inicial, define padrão
    if pasta_inicial is None:
        pasta_inicial = "C:\\"

    # Abre o seletor de pastas
    caminho_pasta = filedialog.askdirectory(
        initialdir=pasta_inicial,
        title="Selecione uma pasta"
    )

    # Se o usuário cancelar, retorna string vazia
    if not caminho_pasta:
        return ""

    # Normaliza para barras invertidas e garante barra final
    caminho_pasta = os.path.normpath(caminho_pasta) + "\\"

    return caminho_pasta


# ========================
# Exemplo de uso
# ========================
if __name__ == "__main__":
    caminho_inicial = r"C:\Users"
    pasta_escolhida = selecionar_pasta(caminho_inicial)

    if pasta_escolhida:
        print(f"Pasta selecionada: {pasta_escolhida}")
    else:
        print("Nenhuma pasta selecionada.")
>>>>>>> 98712e991bac4f7fb6c5ca1b1565bf596d3285ae
