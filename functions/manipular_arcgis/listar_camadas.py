import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from functions.pyaytogui.funcoes_teclado_mouse import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.manipular_windos.capturar_click import *
from functions.outras_funcoes.coordenadas import *
from functions.outras_funcoes.outras_infos import *
import pyperclip
from functions.tkinter.alerta_simples import *

def obter_lista(primeiro_uso=True):
    if primeiro_uso == True:
        x_camada, y_camada = capturar_clique("clique na janela de camadas pra eu saber onde fica!")
        coordinates.x_camada = x_camada
        coordinates.y_camada = y_camada
    else:
        click(coordinates.x_camada, coordinates.y_camada)
    time.sleep(1)  # Espera 2 segundos antes de executar o código
    camada = []
    apertar_ctrl_end()
    
    while True:
        limpar_area_transferencia()
        renomear_arcgis()
        copiar()
        valor1 = pyperclip.paste()
        apertar_esc()
        if valor1 == "Layer Principal":
            camada.append(valor1)
            break
        if valor1 == "Miniatura 1":
            camada.append(valor1)
            cima()
        else:
            cima()
            renomear_arcgis()
            copiar()
            valor2 = pyperclip.paste()
            
            if valor1 == valor2:
                camada.append(valor1)
                camada.append('')
            if valor1 != valor2:
                camada.append(valor1)
                camada.append(valor2)
            
            apertar_esc()
            cima()
            limpar_area_transferencia()

    Text_infos.lista_camadas = camada

        




