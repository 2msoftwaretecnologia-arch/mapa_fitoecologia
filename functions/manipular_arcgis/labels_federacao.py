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

def ajustar_labels():
    obter_lista()
    esperar(0.5)
    destino = encontrar_index(Text_infos.lista_camadas, "Unidades da Federação - IBGE (2022)")
    manipulacao_layers(destino)
    esperar(0.5)
    enter(1)
    janela_dinamica("espere abrir a janela de propriedades depos aperte 'OK'")
    localizar_e_clicar('img/labels.png',"labels não encontrado por favor va para a janela de labels")
    apertar_Tab(3,0.1)
    esperar(0.5)
    escrever_texto("SI")
    esperar(0.5)
    apertar_Tab(2,0.1)
    escrever_texto("TIMES")
    apertar_Tab(1,0.1)
    escrever_texto("8")
    apertar_Tab(11,0.1)
    enter(1)
    janela_dinamica("por favor negrite depois aperte 'OK'")
    janela_de_protecao()
    encontrar_cor_e_mover_mouse()
    pyautogui.click(button='right')
    esperar(1)
    pressionar_tecla('l')
    encontrar_cor_e_mover_mouse()
    pyautogui.click(button='right')
    esperar(1)
    apertar_ctrl_home()
    apertar_pra_baixo(11)
    enter()
    esperar(1)
    janela_dinamica("ative as duas opções apos isso aperte 'OK'")
    janela_de_protecao()





    


