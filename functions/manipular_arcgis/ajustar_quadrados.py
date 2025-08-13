import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.tkinter.input_Texto_dinamico import *
from functions.tkinter.campo_dinamico_opcoes import *
from functions.tkinter.alerta_dinamico import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.pyaytogui.localizacao import *
from functions.pyaytogui.protecao import *
from configs.substituir_textos_config import *
from functions.pyaytogui.encontrar_cor import * 
from functions.manipular_arcgis.listar_camadas import *
from functions.manipular_arcgis.manipular_camadas import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_windos.abrir_documentos import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.manipular_textos.manipular_textos import *
from functions.outras_funcoes.coordenadas import *
from functions.outras_funcoes.helpers import *
from functions.tkinter.alerta_simples import *

janela_dinamica()
click(1249,311)
insert(2)
esperar(0.5)
x_retangulo, y_retangulo = capturar_clique("Clique na seta do retangulo")
pressionar_tecla('r')
x_desenhar_quadradro, y_desenhar_quadradro = capturar_clique("Clique em um lugar para desenhar o quadrado")
desenhar_quadrado(x_desenhar_quadradro,y_desenhar_quadradro,largura=80)
esperar(0.5)
click(x_desenhar_quadradro+10,y_desenhar_quadradro+10,clicks_quant=2)
x_symbol, y_symbol = capturar_clique("Clique em 'symbol'")
click(x_symbol,y_symbol,tempo=0.1, clicks_quant=3)
direita(2)


