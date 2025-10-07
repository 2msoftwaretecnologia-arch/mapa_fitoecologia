import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.Windows.abrir_documentos import *
from scripts.ajustar_quadrados import *
from buildkite.interfaces.multiplas_opcoes import *
from buildkite.functions_pyautogui.funcoes_teclado_mouse import *
from buildkite.functions_tkinter.interfaces import *


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
    apertar_Tab(3, tempo_espera=0.01)
    escrever_texto("6,5")
    esperar(0.3)
    enter(tempo=0.5)
    esperar(1)

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
    espaco_branco_coordenadas = get_or_set_coordinate(2,"aperte no espaço em branco pra eu saber onde fica")
    ponto_incial_coordenadas = get_or_set_coordinate(9,"clique sobre texto para eu enteder onde fica")
    click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1],tempo=0.1) # clica “em nada”
    esperar(0.5)
    colar()
    esperar(1.5)
    click(ponto_incial_coordenadas[0],ponto_incial_coordenadas[1],botao="right")#lugar no arcgis que as coisas vão quando são coladas
    esperar(0.5)
    apertar_ctrl_end(tempo=0.2)
    enter()
    esperar(0.5)
    janela_dinamica("Desative o 'preserve aspect radio' se estiver ativo")
    size_position_coordenadas = get_or_set_coordinate(11,"clique em 'size and position' pra eu entender como fica")
    esperar(0.3)
    # "Size and Position"
    click(size_position_coordenadas[0],size_position_coordenadas[1], clicks_quant=3)
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