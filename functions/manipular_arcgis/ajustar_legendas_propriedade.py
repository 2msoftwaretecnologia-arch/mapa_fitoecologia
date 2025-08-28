import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.kivy.input_Texto_dinamico import *
from functions.kivy.campo_dinamico_opcoes import *
from functions.kivy.alerta_dinamico import *
from functions.kivy.alerta_simples import *

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


def ajustar_info_propriedade():
    
    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco,tempo=0.1)
    insert(tempo=0.2)
    abrir_textos()
    esperar(0.3)
    selecionar_tudo()
    escrever_texto(Text_infos.proprietario)
    enter(tempo=0.5)
    x_texto,y_texto = capturar_clique("clique sobre texto para eu enteder onde fica")
    coordinates.x_incio = x_texto
    coordinates.y_incio = y_texto
    esperar(0.3)
    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco,tempo=0.1)
    esperar(0.3)
    click(coordinates.x_incio,coordinates.y_incio,botao='right')
    esperar(0.6)
    apertar_ctrl_end()
    enter()
    x_primeiro,y_primeiro = capturar_clique("clique em 'Text' pra eu entender como fica")
    click(x_primeiro,y_primeiro,clicks_quant=3)
    direita()
    apertar_Tab(tempo_espera=0.1)
    escrever_texto("23,2921")
    apertar_Tab(tempo_espera=0.1)
    escrever_texto("1,876")
    apertar_Tab(3,tempo_espera=0.1)
    escrever_texto("0,9878")
    apertar_Tab(tempo_espera=0.1)
    esperar(0.3)
    selecionar_tudo()
    escrever_texto("0,3125")
    enter(tempo=0.5)


    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco,tempo=0.1)
    abrir_textos()
    esperar(0.3)
    selecionar_tudo()
    escrever_texto(Text_infos.matricula)
    enter(tempo=0.5)
    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco,tempo=0.1)
    esperar(0.3)
    click(coordinates.x_incio,coordinates.x_incio,botao='right')
    esperar(0.6)
    apertar_ctrl_end()
    enter(tempo=0.5)
    click(x_primeiro,y_primeiro,clicks_quant=3)
    direita()
    apertar_Tab(tempo_espera=0.1)
    escrever_texto("27,8184")
    apertar_Tab(tempo_espera=0.1)
    escrever_texto("1,8989")
    apertar_Tab(3,tempo_espera=0.1)
    escrever_texto("0,8466")
    apertar_Tab(tempo_espera=0.1)
    esperar(0.3)
    selecionar_tudo()
    escrever_texto("0,3125")
    enter(tempo=0.5)


    cidade_estado = Text_infos.cidade_uf
    if len(cidade_estado) > 16:
        p1,p2 = quebrar_texto(cidade_estado,16,False,True)
    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco,tempo=0.1)
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
    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco,tempo=0.1)
    esperar(0.3)
    click(x_texto,y_texto,botao='right')
    esperar(0.6)
    apertar_ctrl_end()
    enter(tempo=0.5)
    click(x_primeiro,y_primeiro,clicks_quant=3)
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
