import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.tkinter.input_Texto_dinamico import *
from functions.tkinter.campo_dinamico_opcoes import *
from functions.tkinter.alerta_dinamico import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.localizacao import *
from functions.pyaytogui.protecao import *
from functions.pyaytogui.encontrar_cor import * 
from functions.manipular_arcgis.listar_camadas import *
from functions.manipular_arcgis.manipular_camadas import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_windos.abrir_documentos import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.manipular_textos.manipular_textos import *
from functions.outras_funcoes.coordenadas import *
from functions.manipular_arcgis.scritpts_leves import *
from functions.tkinter.alerta_simples import *
from text.regioes_fitoecologicas import *


abrir_documento(caminho_legenda_fitoecologia)
janela_dinamica("espere o word abrir e aperte em OK")
clicar_centro_tela()
esperar(0.5)
selecionar_tudo_Word()
esperar(0.5)
escrever_texto(tamanhos_regioes_fito_ecologias["Floresta Estacional"]["1 vez"],velocidade=0.001)
x,y = capturar_clique("clique na janela do arcgis apenas pra eu saber onde fica")
