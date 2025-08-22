# import pyautogui


# pyautogui.click(892,745)#clica na janela do arcgis

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
abrir_margen_pagina_Word(3)
esperar(0.5)
apertar_Tab(3,tempo_espera=0.1)
escrever_texto("5")
esperar(0.3)
enter(tempo=0.5)
esperar(0.5)
selecionar_tudo_Word()
escolher_fonte_Word()
escrever_texto("Times New Roman",)
esperar(0.3)
enter(tempo=0.5)    