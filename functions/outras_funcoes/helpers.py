import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import time

def esperar(segundos):
    """
    Função para pausar a execução do programa por um determinado número de segundos.
    
    Args:
        segundos (int): Número de segundos para pausar.
    """
    time.sleep(segundos)


def encontrar_index(lista, item):
    try:
        index = lista.index(item)
        print(f"Item '{item}' encontrado no índice: {index}")
        print(lista)
        return index
    except ValueError:
        return print(f"Item '{item}' não encontrado na lista.")

