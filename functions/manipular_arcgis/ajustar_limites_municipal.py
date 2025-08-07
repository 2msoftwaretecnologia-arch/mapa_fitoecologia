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



def fazer_ajuste_limites_municipais():
    janela_dinamica("Como as camadas atualizaram vou precisar me atualizar das camadas")
    obter_lista(primeiro_uso=False)
    click(coordinates.x_camada, coordinates.y_camada,tempo=0.1)
    destino = encontrar_index(Text_infos.lista_camadas, "Limites Municipais - SEPLAN (2012)")
    manipulacao_layers(destino)
    esperar(0.2)
    encontrar_cor_e_mover_mouse()
    pyautogui.click(button='right')
    esperar(0.5)
    pressionar_tecla("c",tempo=1)
    apertar_ctrl_home()
    encontrar_cor_e_mover_mouse()
    pyautogui.click(button='right')
    esperar(0.5)
    pressionar_tecla("p",tempo=1)
    janela_dinamica("Espere o processamento ser concluído")
    janela_de_protecao()
    encontrar_cor_e_mover_mouse()
    pyautogui.click(button='right')
    esperar(0.5)
    pressionar_tecla("l",tempo=1)
    encontrar_cor_e_mover_mouse()
    pyautogui.click(button='right')
    esperar(0.5)
    apertar_ctrl_home()
    esperar(0.2)
    apertar_pra_baixo(11)
    enter(tempo=1)
    janela_dinamica("Ative as duas opções depois em clique em OK")
    janela_de_protecao()
    encontrar_cor_e_mover_mouse()
    pyautogui.click()
    enter()
    janela_dinamica("espere a janela de propriedades abrir e aperte OK")
    x_random, y_random = capturar_clique("clique na aba inicial pra eu saber onde fica")
    click(x_random, y_random,tempo=0.1,clicks_quant=3)
    direita(7)
    esperar(0.2)
    apertar_Tab(3,tempo_espera=0.1)
    escrever_texto("no")
    apertar_Tab(2,tempo_espera=0.1)
    escrever_texto("times")
    esperar(0.2)
    apertar_Tab(1,tempo_espera=0.1)
    enter()
    janela_dinamica("depois de fechar clique em OK, se não fechou feche manualemnte")
    janela_de_protecao()

