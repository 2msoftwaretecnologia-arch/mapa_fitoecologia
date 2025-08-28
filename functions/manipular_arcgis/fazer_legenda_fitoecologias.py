import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.kivy.input_Texto_dinamico import *
from functions.kivy.campo_dinamico_opcoes import *
from functions.kivy.alerta_dinamico import *
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
from functions.kivy.alerta_simples import *
from text.regioes_fitoecologicas import *
from functions.outras_funcoes.outras_infos import *




def fazer_parte_legenda():
    tamanho_numero = len(Text_infos.fito_ecologias)#quantidade de fitoecologias
    abrir_documento(caminho_word_nota_tecnica)
    esperar(0.5)
    clicar_centro_tela()
    esperar(0.5)
    abrir_margen_pagina_Word(4)
    
    apertar_Tab(3, tempo_espera=0.1)
    escrever_texto(tamanhos_regioes_fito_ecologias[Text_infos.fito_ecologias[0]][f"{tamanho_numero} time"]["borda"])
    esperar(0.3)
    enter(tempo=0.5)
    esperar(0.5)

    selecionar_tudo_Word()
    escolher_fonte_Word()
    escrever_texto("Times New Roman")
    esperar(0.3)
    enter(tempo=0.3)

    for ecolgia in Text_infos.fito_ecologias:
        escrever_texto(
            tamanhos_regioes_fito_ecologias[ecolgia][f"{tamanho_numero} time"]["descricao"],
            velocidade=0.001
        )
        # duas quebras de linha (ajuste se sua função aceitar 'vezes=')
        enter(quantidade=2,tempo=0.1)
    pressionar_tecla("backspace",quantidade=2)
    esperar(0.2)
    selecionar_tudo_Word()
    copiar()

    click(coordinates.x_arcgis,coordinates.y_arcgis)  # foca na janela do ArcGIS
    esperar(0.5)
    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco) # clica “em nada”
    esperar(0.5)
    colar()
    esperar(1)
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
