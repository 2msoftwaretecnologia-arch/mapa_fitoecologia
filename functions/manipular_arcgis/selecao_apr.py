import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.input_Texto_dinamico import *
from functions.interfaces.campo_dinamico_opcoes import *
from functions.interfaces.multiplas_opcoes import *
from functions.interfaces.alerta_simples import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.pyaytogui.protecao import * 
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
from functions.tkinter.escolher_shpy import *
from database.requests import *

def selecionar_apr():
    try:
        var_apr = escolher_shp("escolha o shp da apr")
        var_aii = esperar_aii(var_apr)
        var_apr = var_apr.replace("/","\\")
        var_aii = var_aii.replace("/","\\")
        camada_cordenadas = request("get",objeto_id=1)
        if camada_cordenadas == (0,0):
            x_camada, y_camada = capturar_clique("Clique na lista onde fica a Layer principal do mapa")
            request("set",objeto_id=1,x=x_camada,y=y_camada)
        else:
            esperar(0.3)
            click(camada_cordenadas[0],camada_cordenadas[1])
        esperar(0.5)
        apertar_ctrl_home()
        esperar(0.5)
        apertar_pra_baixo(1)
        esperar(0.2)
        enter()
        esperar(0.5)
        source_cordenadas = request("get",objeto_id=12)
        if source_cordenadas == (0,0):
            x_source, y_source = capturar_clique("Clique no botão 'Source'")
            request("set",objeto_id=12,x=x_source,y=y_source)
            esperar(0.2)
            click(x_source, y_source, clicks_quant=3)
            source_cordenadas = request("get",objeto_id=12)
        else:
            janela_dinamica("Espere a seleção ser concluída e aperte Entendi")
            click(source_cordenadas[0],source_cordenadas[1],clicks_quant=3)
        esperar(0.3)
        apertar_Tab(6,tempo_espera=0.01)
        enter()
        janela_dinamica("Espere a seleção ser concluída e aperte Entendi")
        esperar(0.3)
        escrever_texto(var_apr,velocidade=0.005)
        enter()
        esperar(0.2)
        apertar_Tab(1)
        esperar(0.2)
        enter()
        pressionar_tecla("f2",tempo=0.4)
        escrever_texto(f'{Text_infos.nome_propriedade} - A.P.R',velocidade=0.002)
        enter(tempo=0.5)
        apertar_pra_baixo(2)
        esperar(0.2)
        enter()
        janela_dinamica("Espere a seleção ser concluída e aperte Entendi")
        click(source_cordenadas[0],source_cordenadas[1],clicks_quant=3)
        esperar(0.5)
        apertar_Tab(6,tempo_espera=0.01)
        enter()
        esperar(0.5)
        escrever_texto(var_aii,velocidade=0.002)
        enter()
        esperar(0.2)
        apertar_Tab(1)
        esperar(0.2)
        enter()
        esperar(1)
        
        #modificando a camada de baixo
        if Text_infos.tipo_mapa == 'Fitoecologia':
            apertar_pra_baixo(16,tempo_espera=0.002)
        if Text_infos.tipo_mapa == 'Geologia':
            apertar_pra_baixo(8,tempo_espera=0.002)
        
        esperar(0.2)
        enter()
        janela_dinamica("Espere a seleção ser concluída e aperte Entendi")
        click(source_cordenadas[0],source_cordenadas[1],clicks_quant=3)
        esperar(0.5)
        apertar_Tab(6,tempo_espera=0.01)
        enter()
        esperar(1)
        escrever_texto(var_apr,velocidade=0.005)
        enter()
        esperar(0.2)
        apertar_Tab(1)
        esperar(0.2)
        enter()
        pressionar_tecla("f2",tempo=0.4)
        escrever_texto(f'{Text_infos.nome_propriedade} - A.P.R',velocidade=0.002)
        enter(tempo=0.5)
        apertar_pra_baixo(2)
        esperar(0.2)
        enter()
        janela_dinamica("Espere a seleção ser concluída e aperte Entendi")
        click(source_cordenadas[0],source_cordenadas[1],clicks_quant=3)
        esperar(0.2)
        apertar_Tab(6,tempo_espera=0.01)
        enter()
        esperar(0.5)
        escrever_texto(var_aii,velocidade=0.002)
        enter()
        esperar(0.2)
        apertar_Tab(1)
        esperar(0.2)
        enter()
        esperar(1)
        

    except Exception as e:
        print(f"Erro ao executar seleção: {e}")