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


def formulario_incial():
    nome_propriedade = input_texto_dinamico(texto="Digite o nome da propriedade")
    proprietario = input_texto_dinamico(texto="Digite o nome do proprietário")
    matricula = input_texto_dinamico(texto="Digite a matrícula")
    cidade = input_texto_dinamico(texto="Digite a cidade - estado")

    Text_infos.proprietario = proprietario
    Text_infos.matricula = matricula
    Text_infos.cidade_uf = cidade
    Text_infos.nome_propriedade = nome_propriedade
