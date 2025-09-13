import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.input_Texto_dinamico import *
from functions.interfaces.campo_dinamico_opcoes import *

from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.localizacao import *
from functions.pyaytogui.protecao import *
from functions.pyaytogui.encontrar_cor import * 
from functions.manipular_arcgis.listar_camadas import *
from functions.manipular_arcgis.manipular_camadas import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.manipular_arcgis.scritpts_leves import *
from functions.manipular_arcgis.helpers_arcgis import *
from functions.manipular_arcgis.ajustar_quadrados import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_windos.abrir_documentos import *
from functions.manipular_textos.manipular_textos import *
from functions.outras_funcoes.coordenadas import *
from functions.interfaces.alerta_simples import *
from text.tamanhos_e_descricoes import *
from functions.outras_funcoes.outras_infos import *




def fazer_parte_legenda(mapa):
    apagar_size_edge = pyautogui.prompt("qual o tamanho da borda")
    tamanho_numero = Text_infos.quantidade_necessario_mapa_atual #quantidade de itens do mapa atual
    abrir_documento(caminho_word_nota_tecnica)
    esperar(0.5)
    clicar_centro_tela()
    esperar(0.5)
    abrir_margen_pagina_Word(4)
    
    #colocar a borda no word
    apertar_Tab(3, tempo_espera=0.1)
    if mapa == 'Fitoecologia':
        escrever_texto(tamanhos_regioes_fito_ecologias[Text_infos.fito_ecologias[0]][f"{tamanho_numero} time"][apagar_size_edge])
    if mapa == 'Geologia':
        escrever_texto(tamanhos_geologicos[Text_infos.geologias[0]][f"{tamanho_numero} time"][apagar_size_edge])
    esperar(0.3)
    enter(tempo=0.5)
    esperar(0.5)

    #colocar a fonte da letra no word
    selecionar_tudo_Word()
    escolher_fonte_Word()
    escrever_texto("Times New Roman")
    esperar(0.3)
    enter(tempo=0.3)

    if mapa == 'Fitoecologia':
        #escrever a descrição da legenda
        for ecolgia in Text_infos.fito_ecologias:
            escrever_texto(
                tamanhos_regioes_fito_ecologias[ecolgia][f"{tamanho_numero} time"]["descricao"],
                velocidade=0.001
            )
            # duas quebras de linha (ajuste se sua função aceitar 'vezes=')
            enter(quantidade=2,tempo=0.1)
    
    if mapa == 'Geologia':
        #escrever a descrição da legenda
        for Geologia in Text_infos.fito_ecologias:
            escrever_texto(
                tamanhos_geologicos[Geologia][f"{tamanho_numero} time"]["descricao"],
                velocidade=0.001
            )
            # duas quebras de linha (ajuste se sua função aceitar 'vezes=')
            enter(quantidade=2,tempo=0.1)

    #apertar pra apgar duas ves no final e copiar a legenda
    pressionar_tecla("backspace",quantidade=2)
    esperar(0.2)
    selecionar_tudo_Word()
    copiar()


    click(coordinates.x_arcgis,coordinates.y_arcgis)  # foca na janela do ArcGIS
    esperar(0.5)
    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco) # clica “em nada”
    esperar(0.5)
    colar()
    esperar(1.5)
    click(coordinates.x_incio,coordinates.y_incio, botao='right')#lugar no arcgis que as coisas vão quando são coladas
    esperar(0.5)
    apertar_ctrl_end(tempo=0.2)
    enter()
    esperar(0.5)

    # "Size and Position"
    click(coordinates.x_size_position,coordinates.y_size_position, clicks_quant=3)
    apertar_Tab(tempo_espera=0.1)

    sel = tamanhos[tamanho_numero]  # usa o tamanho correspondente
    escrever_texto(str(sel["x1"]))
    apertar_Tab(tempo_espera=0.1)
    escrever_texto(str(sel["y1"]))
    apertar_Tab(3, tempo_espera=0.1)
    escrever_texto(str(sel["tx"]))
    apertar_Tab(tempo_espera=0.1)
    esperar(0.3)
    selecionar_tudo()
    escrever_texto(str(sel["ty"]))
    enter(tempo=0.5)
    pressionar_tecla("delete")
    print(apagar_size_edge)

x_arcgis,y_arcgis = 1249,1049
coordinates.x_arcgis = x_arcgis
coordinates.y_arcgis = y_arcgis
x_espaco_Branco,y_espaco_Branco = 535,445
coordinates.x_espaco_Branco = x_espaco_Branco
coordinates.y_espaco_Branco = y_espaco_Branco
x_incio,y_incio = 1170,568
coordinates.x_incio = x_incio
coordinates.y_incio = y_incio
x_size_position,y_size_position = 918,262
coordinates.x_size_position = x_size_position
coordinates.y_size_position = y_size_position


itens_mapa_atual = criar_interface_opcoes(opcoes_disponiveis=["Cráton Amazônico","Faixa Brasília","Grupo Bambuí","Bacia do Parnaíba","Coberturas Cenozóicas","Província Aurífera","Províncias de Níquel e Cromo","Depósitos de Fosfato e Calcário"])
Text_infos.fito_ecologias = itens_mapa_atual
estilo_atual = estilos_regioes_geologicas
Text_infos.descricao_mapa_atual = tamanhos_geologicos

Fechar = pyautogui.confirm(title="Confirmação",text="recomeçar??",buttons=["sim","Não"])

while Fechar != "Não":
    fazer_parte_legenda('Geologia')