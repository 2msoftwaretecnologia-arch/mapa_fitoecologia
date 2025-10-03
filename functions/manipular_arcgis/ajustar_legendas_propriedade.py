import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.manipular_arcgis.comandos_basicos import *
from functions.functions_pyautogui.funcoes_teclado_mouse import *
from functions.manipular_textos.manipular_textos import *
from functions.outras_funcoes.outras_infos import *
from database.requests import *

def ajustar_info_propriedade():
    posicoes = [
        ("23,2921","1,876","0,9878","0,3125"),
        ("27,8184","1,8989","0,8466","0,3125")]
    informacoes = [Text_infos.proprietario,Text_infos.matricula]
    for posicao,informacao in zip(posicoes,informacoes):
        espaco_branco_coordenadas = get_or_set_coordinate(2,"aperte no espaçõ em branco pra eu saber onde fica")
        click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1],tempo=0.1)
        insert(tempo=0.2)
        abrir_textos()
        esperar(0.3)
        selecionar_tudo()
        escrever_texto(informacao)
        enter(tempo=0.5)
        ponto_incial_coordenadas = get_or_set_coordinate(9,"clique sobre texto para eu enteder onde fica")
        esperar(0.3)
        click(ponto_incial_coordenadas[0],ponto_incial_coordenadas[1])
        esperar(0.3)
        click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1],tempo=0.1)
        esperar(0.3)
        click(ponto_incial_coordenadas[0],ponto_incial_coordenadas[1],botao='right')
        esperar(0.6)
        apertar_ctrl_end()
        enter()
        janela_dinamica("espere abrir e aperte 'OK'")
        text_coordenadas = get_or_set_coordinate(13,"clique em 'Text' pra eu entender como fica")
        esperar(0.3)
        click(text_coordenadas[0],text_coordenadas[1],clicks_quant=3)
        direita()
        apertar_Tab(tempo_espera=0.1)
        escrever_texto(posicao[0])
        apertar_Tab(tempo_espera=0.1)
        escrever_texto(posicao[1])
        apertar_Tab(3,tempo_espera=0.1)
        escrever_texto(posicao[2])
        apertar_Tab(tempo_espera=0.1)
        esperar(0.3)
        selecionar_tudo()
        escrever_texto(posicao[3])
        enter(tempo=0.7)


    cidade_estado = Text_infos.cidade_uf
    if len(cidade_estado) > 16:
        p1,p2 = quebrar_texto(cidade_estado,16,False,True)
    click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1],tempo=0.1)
    abrir_textos()
    esperar(0.3)
    selecionar_tudo()
    if len(cidade_estado) > 16:
        escrever_texto(p1)
        pyautogui.hotkey("ctrl","enter")
        escrever_texto(p2)
    if len(cidade_estado) <= 16:
        escrever_texto(cidade_estado)
    enter(tempo=0.5)
    click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1],tempo=0.1)
    esperar(0.3)
    click(ponto_incial_coordenadas[0],ponto_incial_coordenadas[1],botao='right')
    esperar(0.6)
    apertar_ctrl_end()
    enter(tempo=0.5)
    click(text_coordenadas[0],text_coordenadas[1],clicks_quant=3)
    direita()
    if len(cidade_estado) > 16: 
        apertar_Tab(tempo_espera=0.1)
        escrever_texto("27,965")
        apertar_Tab(tempo_espera=0.1)
        escrever_texto("0,5747")
        apertar_Tab(3,tempo_espera=0.1)
        escrever_texto("1,4216")
        apertar_Tab(tempo_espera=0.1)
        esperar(0.3)
        selecionar_tudo()
        escrever_texto("0,4778")
    if len(cidade_estado) <= 16:
        apertar_Tab(tempo_espera=0.1)
        escrever_texto("27,931")
        apertar_Tab(tempo_espera=0.1)
        escrever_texto("0,7082")
        apertar_Tab(3,tempo_espera=0.1)
        escrever_texto("0,9406")
        apertar_Tab(tempo_espera=0.1)
        esperar(0.3)
        selecionar_tudo()
        escrever_texto("0,2344")
    enter(tempo=0.5)
