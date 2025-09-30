import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.campo_dinamico_opcoes import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.outras_funcoes.coordenadas import *
from functions.interfaces.alerta_simples import *



def ajustar_escala():

    refazer_escala = pyautogui.confirm(text="Deseja substituir a escala?", buttons=["sim", "não"])
    if refazer_escala == "sim":
        x_escala, y_escala = capturar_clique("clique em escala para eu saber onde fica")
        coordinates.x_escala = x_escala
        coordinates.y_escala = y_escala
        clicar_centro_tela(1)
        fazer_novamente = None

        while fazer_novamente != "não":
            ajuste_escala = input_texto_dinamico(texto="digite sua escla\nse voce não digitar nada e confirmar com 'ok' ou 'enter'\nvamos confirmar que voce não quer mais ajustar\na escala")
            if ajuste_escala.strip() == "":
                fazer_novamente = "não"
            else:
                esperar(1)
                click(coordinates.x_escala, coordinates.y_escala)
                selecionar_tudo()
                escrever_texto(str(ajuste_escala))
                enter(1)
                limpar_area_transferencia()
                esperar(1.5)
                clicar_centro_tela(1)

