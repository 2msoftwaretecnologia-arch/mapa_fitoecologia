import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from pynput import mouse
import threading
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.funcoes_teclado_mouse import *
from functions.kivy.alerta_simples import *


def capturar_clique(texto):
    # MOSTRAR ALERTA (main thread)
    janela_dinamica(texto).run()

    coordenadas = {}
    done = threading.Event()

    def on_click(x, y, pressed):
        if pressed:
            coordenadas['x'] = x
            coordenadas['y'] = y
            done.set()
            return False

    listener = mouse.Listener(on_click=on_click)
    listener.start()
    # Espera somente o evento, não mexe com Tk aqui
    done.wait()
    listener.stop()

    return coordenadas['x'], coordenadas['y']



