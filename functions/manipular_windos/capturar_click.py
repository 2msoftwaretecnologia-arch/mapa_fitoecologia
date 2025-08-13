import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from pynput import mouse
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.funcoes_teclado_mouse import *
from functions.tkinter.alerta_simples import *


def capturar_clique(texto):
    janela_dinamica(texto)
    coordenadas = {}
    def on_click(x, y,pressed):
        if pressed:
            coordenadas['x'] = x
            coordenadas['y'] = y
            return False  # Encerra o listener

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    return coordenadas['x'], coordenadas['y']



