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



fazer = "sim"
borda = input_texto_dinamico("qual o tamaho da borda")
while fazer == "sim":
    abrir_documento(caminho_legenda_fitoecologia)
    esperar(0.3)
    #janela_dinamica("espere o word abrir e aperte em OK")
    clicar_centro_tela()
    esperar(0.5)
    abrir_margen_pagina_Word(4)
    
    apertar_Tab(3,tempo_espera=0.1)
    escrever_texto(borda)
    esperar(0.3)
    enter(tempo=0.5)
    esperar(0.5)
    selecionar_tudo_Word()
    escolher_fonte_Word()
    escrever_texto("Times New Roman",)
    esperar(0.3)
    enter(tempo=0.3)    
    for i in range(2):
        escrever_texto(tamanhos_regioes_fito_ecologias["Savana Gramíneo Lenhosa"]["2 vezes"]["descricao"],velocidade=0.001)
        enter(2)
    esperar(0.2)
    selecionar_tudo_Word()
    copiar()
    #x_arcgis,y_arcgis = capturar_clique("clique na janela do arcgis apenas pra eu saber onde fica")
    click(892,745)#clica na janela do arcgis
    esperar(0.5)
    click(1249,311)#clicar em nada
    esperar(0.5)
    colar()
    esperar(1)
    click(867,393,botao='right')
    esperar(0.5)
    apertar_ctrl_end(tempo=0.2)
    enter()
    esperar(0.5)
    #x_primeiro,y_primeiro = capturar_clique("clique em 'size and position' pra eu entender como fica")
    click(652,158,clicks_quant=3)
    apertar_Tab(tempo_espera=0.1)
    escrever_texto(tamanho2["x1"])
    apertar_Tab(tempo_espera=0.1)
    escrever_texto(tamanho2["y1"])
    apertar_Tab(3,tempo_espera=0.1)
    escrever_texto(tamanho2["tx"])
    apertar_Tab(tempo_espera=0.1)
    esperar(0.3)
    selecionar_tudo()
    escrever_texto(tamanho2["ty"])
    enter(tempo=0.5)
    pressionar_tecla("delete")
    fazer = selecionar_resposta("Deseja ajustar o grid?", ["sim", "não"])
    if fazer == "sim":
        borda = input_texto_dinamico(f"qual o tamaho da borda o valor \nque tava era {borda}")


print(borda)