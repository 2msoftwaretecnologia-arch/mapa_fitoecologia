import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.Windows.manipular_windos import *
from buildkite.interfaces.janelas_dinamicas import *
from pynput import mouse
import threading


def capturar_clique(texto):
    # MOSTRAR ALERTA (main thread)
    janela_dinamica(texto)

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
    esperar(0.5)  # Pequena espera para garantir que o listener pare completamente
    return coordenadas['x'], coordenadas['y']



