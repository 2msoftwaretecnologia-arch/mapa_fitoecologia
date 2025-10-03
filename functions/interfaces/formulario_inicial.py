import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipular_windos.capturar_click import *
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
