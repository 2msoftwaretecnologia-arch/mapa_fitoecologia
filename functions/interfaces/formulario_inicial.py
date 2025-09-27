import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.input_Texto_dinamico import *
from functions.interfaces.campo_dinamico_opcoes import *
from functions.interfaces.input_de_cidade import *
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
from functions.outras_funcoes.outras_infos import *
from functions.interfaces.janela_input_propriedade import *


def formulario_incial():
    campos = abrir_janela_input_propriedade()
    Text_infos.nome_propriedade = campos['nome_propriedade']
    Text_infos.proprietario = campos['proprietario']
    Text_infos.matricula = campos['matricula']
    Text_infos.cidade_uf = campos['cidade_uf']
    x_arcgis , y_arcgis = capturar_clique("clique no arcgis pra eu saber onde fica")

    coordinates.x_arcgis = x_arcgis
    coordinates.y_arcgis = y_arcgis
