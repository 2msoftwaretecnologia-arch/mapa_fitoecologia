import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from buildkite.functions_pyautogui.mexer_mouse import * 
from scripts.info_arcgis import *
from buildkite.functions_pyautogui.funcoes_teclado_mouse import *
from database.requests import *
from database.text_infos import *


def ajustar_quadrados_mapa():
    janela_dinamica("espere o arcgis se normalizar e parte ok")
    estilo_atual = estilos_atuais()
    x_tamanho,y_tamanho = tamano_quadrados(Text_infos.quantidade_necessario_mapa_atual)
    lista_posicao = posicao_quadrados(Text_infos.quantidade_necessario_mapa_atual)
    espaco_branco_coordenadas = get_or_set_coordinate(2,"aperte no espaço em branco pra eu saber onde fica")
    click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1],tempo=0.1)
    esperar(0.5)
    retangulo_coordenadas = get_or_set_coordinate(3,"Clique na seta do retangulo pra eu saber onde fica") #local que pega a forma geometrica  do retangulo
    quadrado_coordenadas = get_or_set_coordinate(4,"Clique em um lugar para desenhar o quadrado") #local que vai ser desenhado o quadrado
    for posicoes,tipo in zip(lista_posicao,Text_infos.itens_atuais):
        click(retangulo_coordenadas[0],retangulo_coordenadas[1])
        pressionar_tecla('r')
        desenhar_quadrado(quadrado_coordenadas[0],quadrado_coordenadas[1],largura=80)
        esperar(0.5)
        click(quadrado_coordenadas[0]+10,quadrado_coordenadas[1]+10,clicks_quant=2)#aqui to colocando alguns pixels a mais pra ele conseguir clicar mais ou menos no centro do quadrado
        symbol_cordenadas = get_or_set_coordinate(5,"Clique em 'symbol'")
        esperar(0.2)
        click(symbol_cordenadas[0],symbol_cordenadas[1],tempo=0.1, clicks_quant=3)
        fill_color_cordenadas =  get_or_set_coordinate(6,"Clique em 'fill color'")
        click(symbol_cordenadas[0],symbol_cordenadas[1],tempo=0.1)
        click(fill_color_cordenadas[0],fill_color_cordenadas[1],tempo=0.1)
        cima(2)
        esperar(0.5)
        enter()
        escrever_texto(str(estilo_atual[tipo][0]))
        apertar_Tab(tempo_espera=0.1)
        escrever_texto(str(estilo_atual[tipo][1]))
        apertar_Tab(tempo_espera=0.1)
        escrever_texto(str(estilo_atual[tipo][2]))
        enter()
        outline_cordenadas =  get_or_set_coordinate(7,"Clique em 'fill color'")
        click(symbol_cordenadas[0],symbol_cordenadas[1],tempo=0.1)
        click(outline_cordenadas[0],outline_cordenadas[1],tempo=0.1)
        cima(1)
        enter()
        apertar_Tab()
        escrever_texto("0,40")
        click(symbol_cordenadas[0],symbol_cordenadas[1],tempo=0.1, clicks_quant=3)
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