import pyautogui
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.input_Texto_dinamico import *
from functions.interfaces.campo_dinamico_opcoes import *
from functions.interfaces.multiplas_opcoes import *
from functions.interfaces.alerta_simples import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.pyaytogui.localizacao import *
from functions.pyaytogui.protecao import *
from functions.pyaytogui.encontrar_cor import * 
from functions.manipular_arcgis.listar_camadas import *
from functions.manipular_arcgis.manipular_camadas import *
from functions.manipular_arcgis.helpers_arcgis import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_windos.abrir_documentos import *
from functions.manipular_textos.manipular_textos import *
from functions.outras_funcoes.coordenadas import *
from functions.outras_funcoes.outras_infos import *
from functions.outras_funcoes.helpers import *
from functions.manipular_windos.capturar_click import capturar_clique
from functions.outras_funcoes.coordenadas import *
from functions.interfaces.alerta_simples import janela_dinamica

def selecionar_apr():
    try:
        var_apr = r"C:\Users\Daniel Menezes\Documents\projeto-envimap\shps\Propriedade\apr\APR.shp"
        var_aii = r"C:\Users\Daniel Menezes\Documents\projeto-envimap\shps\Propriedade\aii\AII.shp"
        x, y = capturar_clique("Clique na lista onde fica a Layer principal do mapa")
        click(x, y)
        esperar(0.5)

        apertar_ctrl_home()
        esperar(0.5)

        apertar_pra_baixo(1)
        esperar(0.2)

        enter()
        esperar(0.5)

        x_source, y_source = capturar_clique("Clique no botão 'Source'")
        click(x_source, y_source, clicks_quant=3)
        esperar(0.5)

        apertar_Tab(6,tempo_espera=0.2)

        enter()
        
        x_write, y_write = capturar_clique("Clique no campo para escrever o caminho do arquivo")
        click(x_write, y_write)
        esperar(0.5)
        escrever_texto(var_apr)
        enter()
        
        esperar(0.2)
        apertar_Tab(1)
        esperar(0.2)
        enter()
        
        apertar_pra_baixo(2)
        esperar(0.2)
            
        click(x, y)
        esperar(0.5)
        
        enter()
        janela_dinamica("Espere a seleção ser concluída e aperte Entendi")

        x_source, y_source = capturar_clique("Clique no botão 'Source'")
        click(x_source, y_source, clicks_quant=3)
        esperar(0.5)

        apertar_Tab(6,tempo_espera=0.2)

        enter()
        
        x_write, y_write = capturar_clique("Clique no campo para escrever o caminho do arquivo")
        click(x_write, y_write)
        esperar(0.5)
        escrever_texto(var_aii)
        enter()
        
        esperar(0.2)
        apertar_Tab(1)
        esperar(0.2)
        enter()

    except Exception as e:
        print(f"Erro ao executar seleção: {e}")
