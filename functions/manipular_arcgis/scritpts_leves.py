import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.input_Texto_dinamico import *
from functions.interfaces.campo_dinamico_opcoes import *
from functions.interfaces.formulario_inicial import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.localizacao import *
from functions.manipular_textos.manipular_textos import *
from configs.configs_apr import *
from functions.pyaytogui.encontrar_cor import * 
from functions.manipular_arcgis.listar_camadas import *
from functions.manipular_arcgis.manipular_camadas import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.manipular_arcgis.helpers_arcgis import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.outras_funcoes.coordenadas import *
from functions.interfaces.alerta_simples import *

def colar_scripts():
    formulario_incial()
    x_layer, y_layer = capturar_clique("Clique na região do layer principal")
    coordinates.x_layer_principal = x_layer
    coordinates.y_layer_principal = y_layer
    click(x_layer, y_layer)
    esperar(0.5)
    apertar_ctrl_home()
    esperar(0.2)
    apertar_pra_baixo(1)
    esperar(0.2)
    renomear_arcgis()
    esperar(0.2)
    escrever_texto(str(Text_infos.nome_propriedade))
    enter(1)
    esperar(0.2)