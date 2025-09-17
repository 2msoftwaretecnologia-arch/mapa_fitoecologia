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
    x_arcgis,y_arcgis = capturar_clique("clique na janela no arcgis para eu saber onde fica")
    coordinates.x_arcgis = x_arcgis
    coordinates.y_arcgis = y_arcgis
    formulario_incial()
    esperar(1)
    clicar_centro_tela(1)
    insert(2)
    
    #não sera mais necessario
    texto_apr = texto_config_Apr(Text_infos.nome_propriedade)
    esperar(1)
    abrir_console()
    x_janela_python, y_janela_python = capturar_clique("clique na janela do python para eu saber onde é a janela")
    coordinates.x_console_quadro = x_janela_python
    coordinates.y_console_quadro = y_janela_python
    copiar_para_area_transferencia(texto_apr)
    apertar_ctrl_end()
    esperar(0.5)
    colar()
    esperar(0.5)
    enter(3, tempo=0.1)
    limpar_area_transferencia()
    #click(x=coordinates.x_console_quadro, y=coordinates.y_console_quadro)
    x_fechar_console, y_fechar_console = capturar_clique("clique em fechar console pra eu saber onde fica!")
    coordinates.fechar_console_x = x_fechar_console
    coordinates.fechar_console_y = y_fechar_console