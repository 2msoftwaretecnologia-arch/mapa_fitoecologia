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
from functions.manipular_arcgis.scritpts_leves import *
from functions.tkinter.alerta_simples import *
from ia.agente import *


def fazer_legenda_com_ia():
    solo_predominante = input_texto_dinamico("digite qual  e a fitoecologia predominante")
    texto_ia = Ask_AI(f"me fale sobre a Fitoecologia {solo_predominante}")
    Text_infos.tipo_dominante = solo_predominante
    abrir_documento(caminho_word_ia)
    janela_dinamica("espere o word abrir e aperte em OK")
    clicar_centro_tela()
    esperar(0.5)
    selecionar_tudo_Word()
    esperar(0.5)
    escrever_texto(texto_ia,velocidade=0.002)
    selecionar_tudo_Word()
    escolher_fonte_Word()
    escrever_texto("Times New Roman")
    enter()
    esperar(0.5)
    copiar()
    janela_dinamica("abra o arcgis")
    janela_de_protecao()
    clicar_centro_tela()
    esperar(0.5)
    colar()
    show_alert_dinamic("Va nas propriedades da legenda em\n'size and Position' e desative todas as checkbox")
    janela_de_protecao()
    x_random, y_random = capturar_clique("clique no eixo 'x' pra eu saber onde e")
    esperar(0.5)
    selecionar_tudo(tempo=0.5)
    escrever_texto('22,693')
    apertar_Tab()
    escrever_texto('5,6894')
    apertar_Tab(3,tempo_espera=0.1)
    escrever_texto('6,4607')
    apertar_Tab()
    escrever_texto('6,2557')
    enter()
    limpar_area_transferencia()