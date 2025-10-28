import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buildkite.functions_pyautogui.funcoes_teclado_mouse import (clicar_centro_tela,salvar_mxj,salvar_export_mapa,
                                                                 click,escrever_texto,selecionar_tudo,enter,apertar_Tab,pressionar_tecla)
from buildkite.interfaces.janelas_dinamicas import janela_pausa
from buildkite.functions_tkinter.interfaces import abrir_checkbox_saida,selecionar_pasta
from buildkite.Windows.manipular_windos import esperar
from database.requests import get_or_set_coordinate
from database.text_infos import Text_infos

def salvar_mapas():
    abrir_checkbox_saida()
    clicar_centro_tela()
    salvar_mxj(tempo=1)
    pasta_salvar = selecionar_pasta(Text_infos.caminho_mapa_atual)
    input_fild_salvar_mxd_coordenadas = get_or_set_coordinate(15,"Clique onde digita o caminho pra eu entender onde fica")
    espaco_branco_coordenadas = get_or_set_coordinate(2,"clique em um espaço vazio fora do mapa para eu saber onde fica")
    click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1])
    esperar(0.2)
    click(input_fild_salvar_mxd_coordenadas[0],input_fild_salvar_mxd_coordenadas[1])
    selecionar_tudo(tempo=0.3)
    escrever_texto(pasta_salvar,velocidade=0.002)
    esperar(0.2)
    if Text_infos.tipo_mapa == 'Pedologia':
        escrever_texto("Mapa A4- Fitofisionomias.mxd")
    if Text_infos.tipo_mapa == 'Geologia':
        escrever_texto("Mapa A4- Geofomologia.mxd")
    if Text_infos.tipo_mapa == 'Fitofisionomias':
        escrever_texto("Mapa A4- Fitofisionomias.mxd")
    if Text_infos.tipo_mapa == 'Regioes_climaticas':
        escrever_texto("Mapa A4- Regioes Climaticas.mxd")
    if Text_infos.tipo_mapa == 'Declividade':
        escrever_texto("Mapa A4- Declividade.mxd")
    if Text_infos.tipo_mapa == 'Erodibilidade':
        escrever_texto("Mapa A4- Erodibilidade.mxd")
    enter()
    janela_pausa("espere o globo no canto esquerdo finalizar e aperte ok")
    salvar_export_mapa()
    janela_pausa("espere abrir e aperte ok")
    input_fild_salvar_pdf_jpeg_coordenadas = get_or_set_coordinate(16,"Clique onde digita o caminho pra eu entender onde fica")
    click(input_fild_salvar_pdf_jpeg_coordenadas[0],input_fild_salvar_pdf_jpeg_coordenadas[1],clicks_quant=3)
    selecionar_tudo(tempo=0.3)
    escrever_texto(pasta_salvar,velocidade=0.002)
    esperar(0.2)
    if Text_infos.tipo_mapa == 'Pedologia':
        escrever_texto("Mapa A4- Fitofisionomias.jpg")
    if Text_infos.tipo_mapa == 'Geologia':
        escrever_texto("Mapa A4- Geofomologia.jpg")
    if Text_infos.tipo_mapa == 'Fitofisionomias':
        escrever_texto("Mapa A4- Fitofisionomias.jpg")
    if Text_infos.tipo_mapa == 'Regioes_climaticas':
        escrever_texto("Mapa A4- Regioes Climaticas.jpg")
    if Text_infos.tipo_mapa == 'Declividade':
        escrever_texto("Mapa A4- Declividade.jpg")
    if Text_infos.tipo_mapa == 'Erodibilidade':
        escrever_texto("Mapa A4- Erodibilidade.jpg")
    
    apertar_Tab(tempo_espera=0.1)
    pressionar_tecla("j",tempo=0.3)
    enter()
    janela_pausa("espere o globo no canto esquerdo finalizar e aperte ok")
    salvar_export_mapa()
    janela_pausa("espere abrir e aperte ok")
    click(input_fild_salvar_pdf_jpeg_coordenadas[0],input_fild_salvar_pdf_jpeg_coordenadas[1],clicks_quant=3)
    selecionar_tudo(tempo=0.3)
    escrever_texto(pasta_salvar,velocidade=0.002)
    esperar(0.2)
    if Text_infos.tipo_mapa == 'Pedologia':
        escrever_texto("Mapa A4- Fitofisionomias.pdf")
    if Text_infos.tipo_mapa == 'Geologia':
        escrever_texto("Mapa A4- Geofomologia.pdf")
    if Text_infos.tipo_mapa == 'Fitofisionomias':
        escrever_texto("Mapa A4- Fitofisionomias.pdf")
    if Text_infos.tipo_mapa == 'Regioes_climaticas':
        escrever_texto("Mapa A4- Regioes Climaticas.pdf")
    if Text_infos.tipo_mapa == 'Declividade':
        escrever_texto("Mapa A4- Declividade.pdf")
    if Text_infos.tipo_mapa == 'Erodibilidade':
        escrever_texto("Mapa A4- Erodibilidade.pdf")
    
    apertar_Tab(tempo_espera=0.1)
    pressionar_tecla("j",tempo=0.2)
    pressionar_tecla("p",quantidade=2,tempo=0.2)
    enter()