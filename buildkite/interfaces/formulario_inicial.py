import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buildkite.interfaces.janela_input_propriedade import *
from buildkite.Windows.capturar_click import *
from database.coordenadas import *
from database.text_infos import *


def formulario_incial():
    campos = abrir_janela_input_propriedade()
    Text_infos.nome_propriedade = campos['nome_propriedade']
    Text_infos.proprietario = campos['proprietario']
    Text_infos.matricula = campos['matricula']
    Text_infos.cidade_uf = campos['cidade_uf']
    x_arcgis , y_arcgis = capturar_clique("clique no arcgis pra eu saber onde fica")

    coordinates.x_arcgis = x_arcgis
    coordinates.y_arcgis = y_arcgis
