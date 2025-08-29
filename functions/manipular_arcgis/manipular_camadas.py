import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from configs.escala_config import *
from functions.interfaces.campo_dinamico_opcoes import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.pyaytogui.encontrar_cor import * 
from functions.outras_funcoes.helpers import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.manipular_arcgis.listar_camadas import *
from functions.outras_funcoes.coordenadas import *
from functions.outras_funcoes.outras_infos import *
from functions.interfaces.alerta_simples import *


def manipulacao_layers(posicao_final):    
    apertar_ctrl_home()
    
    # Percorre a lista de trás pra frente
    for _ in range(len(Text_infos.lista_camadas) - 1, posicao_final , -1):
        
        apertar_pra_baixo()
        # Aqui você pode colocar a lógica de manipulação do item


