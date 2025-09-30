import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.input_Texto_dinamico import *
from functions.interfaces.campo_dinamico_opcoes import *

from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.protecao import *
from functions.manipular_arcgis.listar_camadas import *
from functions.manipular_arcgis.manipular_camadas import *
from functions.manipular_arcgis.comandos_basicos import *
from functions.manipular_arcgis.helpers_arcgis import *
from functions.manipular_arcgis.ajustar_quadrados import *
from functions.manipular_windos.manipular_windos import *
from functions.manipular_windos.capturar_click import *
from functions.manipular_windos.abrir_documentos import *
from functions.manipular_textos.manipular_textos import *
from functions.outras_funcoes.coordenadas import *
from functions.interfaces.alerta_simples import *
from functions.outras_funcoes.outras_infos import *
from functions.tkinter.aviso_checbox import *



def fazer_parte_legenda():
    if Text_infos.tipo_mapa == 'Fitoecologia':
        itens_mapa_atual = criar_interface_opcoes(opcoes_disponiveis=regioes_fitoecologias)
        Text_infos.itens_atuais = itens_mapa_atual
                

    if Text_infos.tipo_mapa == 'Geologia':
        itens_mapa_atual = criar_interface_opcoes(opcoes_disponiveis=Regioes_geologicas)
        Text_infos.itens_atuais = itens_mapa_atual
        

    Text_infos.quantidade_necessario_mapa_atual = len(Text_infos.itens_atuais)
    
    
    abrir_documento(caminho_word_nota_tecnica)
    esperar(0.5)
    clicar_centro_tela()
    esperar(0.5)
    abrir_margen_pagina_Word(4)
    #colocar a borda no word
    apertar_Tab(3, tempo_espera=0.1)
    escrever_texto("6,5")
    esperar(0.3)
    enter(tempo=0.5)
    esperar(0.5)

    #colocar a fonte da letra no word
    selecionar_tudo_Word()
    escolher_fonte_Word()
    escrever_texto("Times New Roman")
    esperar(0.3)
    enter(tempo=0.3)

    janela_dinamica("Faça a descrição do seu texto entre 1100 e 1200 caractes")
    abrir_checkbox_saida()
    clicar_centro_tela()
    esperar(0.2)
    selecionar_tudo_Word()
    copiar()
    esperar(0.2)

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
    janela_dinamica("Desative o 'preserve aspect radio' se estiver ativo")
    x_size_position,y_size_position = capturar_clique("clique em 'size and position' pra eu entender como fica")
    esperar(0.3)
    coordinates.x_size_position = x_size_position
    coordinates.y_size_position = y_size_position
    # "Size and Position"
    click(coordinates.x_size_position,coordinates.y_size_position, clicks_quant=3)
    apertar_Tab(tempo_espera=0.1)

    escrever_texto("22,8838")
    apertar_Tab(tempo_espera=0.1)
    escrever_texto("4,7244")
    apertar_Tab(3, tempo_espera=0.1)
    escrever_texto("6,4500")
    apertar_Tab(tempo_espera=0.1)
    esperar(0.3)
    selecionar_tudo()
    escrever_texto("7,2859")
    enter(tempo=0.5)