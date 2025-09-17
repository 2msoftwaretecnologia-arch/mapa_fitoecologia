import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import time
from functions.interfaces.alerta_simples import *


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


def esperar_aii(shp_path: str,) -> str:
    """
    Fica verificando até encontrar 'aii.shp' na mesma pasta do shapefile informado.

    Parâmetros:
        shp_path (str): Caminho de um shapefile qualquer.
        intervalo (int): Intervalo em segundos entre cada verificação. (default = 5)

    Retorna:
        str: Caminho completo do 'aii.shp' quando for encontrado.
    """
    pasta = os.path.dirname(shp_path)
    caminho_aii = os.path.join(pasta, "aii.shp")

    print(f"Aguardando o arquivo 'aii.shp' aparecer em: {pasta}")

    while not os.path.isfile(caminho_aii):
        janela_dinamica("O 'AII.shp' não foi encontrado ja pasta \nconfirme se ele esta em caixa alta ou contido na pasta antes de apertar em 'ok")  # espera X segundos antes de checar de novo

    print("Arquivo encontrado:", caminho_aii)
    return caminho_aii