import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.tkinter.input_Texto_dinamico import *
from functions.tkinter.campo_dinamico_opcoes import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.localizacao import *
from functions.pyaytogui.protecao import *
from configs.limites_federacao_config import *
from functions.pyaytogui.encontrar_cor import * 
from functions.manipular_arcgis.listar_camadas import *
from functions.manipular_arcgis.manipular_camadas import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.outras_funcoes.coordenadas import *
from functions.outras_funcoes.outras_infos import *
from functions.tkinter.alerta_simples import *


def fazer_fitofisionomia(): 
    click(coordinates.x_camada, coordinates.y_camada,tempo=0.1)
    destino = encontrar_index(Text_infos.lista_camadas, "Regioes_Fitoecologicas")
    manipulacao_layers(destino)
    esperar(0.5)
    enter(1)
    janela_dinamica("espere abrir a janela de propriedades depos aperte 'OK'")
    x_random, y_random = capturar_clique("clique na aba inicial pra eu saber onde fica")
    click(x_random, y_random,tempo=0.1,clicks_quant=3)
    direita(4)
    apertar_Tab(2)
    esperar(0.5)
    enter(tempo=0.5)
    janela_dinamica("por favor importe onde esta localizado o estilo dessa regição fitoecologica")
    janela_de_protecao()
    click(coordinates.x_camada, coordinates.y_camada,tempo=0.1,clicks_quant=2)
    manipulacao_layers(destino)
    encontrar_cor_e_mover_mouse()
    esperar(0.5)
    pressionar_tecla("f2",tempo=0.5)
    escrever_texto("Regioes Fitoecologicas - SEPLAN (2012)")
    esperar(0.2)
    enter()
    pyautogui.click(button='right')
    esperar(0.5)
    pressionar_tecla("c")
    esperar(0.2)
    apertar_ctrl_home()
    esperar(0.2)
    encontrar_cor_e_mover_mouse()
    pyautogui.click(button='right')
    esperar(0.5)
    pressionar_tecla("p",tempo=1)
    encontrar_cor_e_mover_mouse()
    pyautogui.click(button='right')
    esperar(0.5)
    pressionar_tecla("l",tempo=1)
    pyautogui.click(button='right')
    esperar(0.5)
    apertar_pra_baixo(12,tempo_espera=0.1)
    enter()
    esperar(0.5)
    janela_dinamica("selecione as duas opções e aperrte em converter")
    janela_de_protecao()
    
    encontrar_cor_e_mover_mouse()
    pyautogui.click()
    esperar(0.2)
    enter(tempo=0.5)
    janela_dinamica("esperere a janela de propriedades abrir e clique em 'OK' para continuar")
    click(x_random, y_random,tempo=0.1,clicks_quant=3)
    direita(7)
    apertar_Tab(3,tempo_espera=0.1)
    escrever_texto("de")
    apertar_Tab(2,tempo_espera=0.1)
    escrever_texto("times")
    apertar_Tab(1,tempo_espera=0.1)
    janela_dinamica("por favor coloque em negrito e depois em italico \n apos isso aperte 'OK' para continuar")
    janela_de_protecao()


