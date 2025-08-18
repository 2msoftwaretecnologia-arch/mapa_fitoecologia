import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.tkinter.input_Texto_dinamico import *
from functions.tkinter.campo_dinamico_opcoes import *
from functions.tkinter.alerta_dinamico import *
from functions.tkinter.alerta_simples import *
from functions.tkinter.checkbox_mulptipla import *
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

def ajustar_quadrados_fitoecologia():
    fito_ecologias = get_user_selections()
    x_tamanho,y_tamanho = tamano_quadrados(len(fito_ecologias))
    lista_posicao = posicao_quadrados(len(fito_ecologias))
    click(coordinates.x_espaco_Branco,coordinates.y_espaco_Branco)
    insert(2)
    esperar(0.5)
    x_retangulo, y_retangulo = capturar_clique("Clique na seta do retangulo pra eu saber onde fica")
    coordinates.x_retangulo = x_retangulo
    coordinates.y_retangulo = y_retangulo
    x_desenhar_quadradro, y_desenhar_quadradro = capturar_clique("Clique em um lugar para desenhar o quadrado")
    coordinates.x_desenhar_quadradro = x_desenhar_quadradro
    coordinates.y_desenhar_quadradro = y_desenhar_quadradro
    for posicoes,fito_ecologia in zip(lista_posicao,fito_ecologias):
        click(coordinates.x_retangulo,coordinates.y_retangulo,tempo=0.2)
        pressionar_tecla('r')
        desenhar_quadrado(coordinates.x_desenhar_quadradro,coordinates.y_desenhar_quadradro,largura=80)
        esperar(0.5)
        click(coordinates.x_desenhar_quadradro+10,coordinates.y_desenhar_quadradro+10,clicks_quant=2)#aqui to colocando alguns pixels a mais pra ele conseguir clicar mais ou menos no centro do quadrado
        if not isinstance(coordinates.x_symbol_quadrado, int):#aqui ele ta verican ja não foi instanciado
            x_symbol, y_symbol = capturar_clique("Clique em 'symbol'")
            coordinates.x_symbol_quadrado = x_symbol
            coordinates.y_symbol_quadrado = y_symbol
            click(x_symbol,y_symbol,tempo=0.1, clicks_quant=3)
            x_fill_color_quadrado , y_fill_color_quadrado =  capturar_clique("Clique em 'fill color'")
            coordinates.x_fill_color_quadrado = x_fill_color_quadrado
            coordinates.y_fill_color_quadrado = y_fill_color_quadrado
            cima(3)
            esperar(0.5)
            enter()
            escrever_texto(str(estilos_fitoecologias[fito_ecologia][0]))
            apertar_Tab(tempo_espera=0.1)
            escrever_texto(str(estilos_fitoecologias[fito_ecologia][1]))
            apertar_Tab(tempo_espera=0.1)
            escrever_texto(str(estilos_fitoecologias[fito_ecologia][2]))
            enter()
            x_out_line_color_quadrado , y_out_line_color_quadrado =  capturar_clique("Clique em 'outline color'")
            coordinates.x_out_line_color_quadrado = x_out_line_color_quadrado
            coordinates.y_out_line_color_quadrado = y_out_line_color_quadrado
            cima(2)
            enter()
            apertar_Tab()
            escrever_texto("0,40")
            click(coordinates.x_symbol_quadrado,coordinates.y_symbol_quadrado,tempo=0.1, clicks_quant=3)
        else:
            esperar(1)
            click(coordinates.x_symbol_quadrado,coordinates.y_symbol_quadrado,tempo=0.1, clicks_quant=3)
            esperar(0.5)
            click(coordinates.x_fill_color_quadrado,coordinates.y_fill_color_quadrado,tempo=0.1)
            esperar(0.5)
            cima(2)
            enter(tempo=0.5)
            escrever_texto(str(estilos_fitoecologias[fito_ecologia][0]))
            apertar_Tab(tempo_espera=0.1)
            escrever_texto(str(estilos_fitoecologias[fito_ecologia][1]))
            apertar_Tab(tempo_espera=0.1)
            escrever_texto(str(estilos_fitoecologias[fito_ecologia][2]))
            enter()
            click(coordinates.x_out_line_color_quadrado,coordinates.y_out_line_color_quadrado,tempo=0.1)
            cima(1)
            enter()
            apertar_Tab()
            escrever_texto("0,40")
            click(coordinates.x_symbol_quadrado,coordinates.y_symbol_quadrado,tempo=0.1, clicks_quant=3)
        direita(2)
        esperar(0.5)
        apertar_Tab(tempo_espera=0.1)
        escrever_texto(posicoes[0])
        apertar_Tab(tempo_espera=0.1)
        escrever_texto(posicoes[1])
        apertar_Tab(3,tempo_espera=0.1)
        escrever_texto(x_tamanho)
        apertar_Tab(tempo_espera=0.1)
        escrever_texto(y_tamanho)
        esperar(0.5)
        enter()


