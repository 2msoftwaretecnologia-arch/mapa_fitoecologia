import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.input_Texto_dinamico import *
from functions.interfaces.campo_dinamico_opcoes import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.localizacao import *
from functions.pyaytogui.encontrar_cor import * 
from functions.manipular_arcgis.listar_camadas import *
from functions.manipular_arcgis.manipular_camadas import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.outras_funcoes.coordenadas import *


def janela_de_protecao():
    confirmacao = input_texto_dinamico("Essa e uma janla de proteção ao usuario\npor favor, digite 'pronto' para continuar")
    while confirmacao.lower() != "pronto":
        confirmacao = input_texto_dinamico("Essa e uma janla de proteção ao usuario\n, por favor, digite 'pronto' para continuar")