import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.tkinter.input_Texto_dinamico import *
from functions.tkinter.campo_dinamico_opcoes import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.pyaytogui.localizacao import *
from functions.outras_funcoes.helpers import *
from functions.manipular_windos.capturar_click import *
from functions.outras_funcoes.coordenadas import *
from functions.tkinter.alerta_simples import *


def fazer_grid():
    fazer = "sim"
    x_espaco_vazio, y_espaco_vazio =  capturar_clique("clique em um espaço vazio fora do mapa para eu saber onde fica")
    coordinates.x_espaco_Branco = x_espaco_vazio
    coordinates.y_espaco_Branco = y_espaco_vazio
    while fazer == 'sim':
        clicar_centro_tela(1)
        insert(2)
        clicar_centro_tela(1)
        esperar(0.5)
        pyautogui.click(button="right")#TODO: ajustar essa função aqui depois
        esperar(0.5)
        cima()
        enter()
        
        janela_dinamica("espere a janela de propriedades abrir")
        if not isinstance(coordinates.x_grid, int):
            x_grid , y_grid = capturar_clique("aperte no grid duas vezes rapido")
            coordinates.x_grid = x_grid
            coordinates.y_grid = y_grid
            esperar(1)
            click(x_grid , y_grid,clicks_quant=3)
        else:
            click(coordinates.x_grid , coordinates.y_grid,clicks_quant=3)
        apertar_Tab(5,tempo_espera=0.1)
        enter()
        
        esperar(0.5)
        
        grid_atual = input_texto_dinamico("Digite o valor do grid lembrando\n que esse valor vai ser multiplicado por 100 ")
        tipo_formato = selecionar_resposta("Qual o formato da escala que deseja?",["000000","00000"])
        
        apertar_Tab(1)
        grid_atual = int(grid_atual)*100
        escrever_texto(str(grid_atual))
        escrever_texto(f",{tipo_formato}")
        esperar(0.2)
        apertar_Tab(2,0)
        escrever_texto(str(grid_atual))
        escrever_texto(f",{tipo_formato}")
        enter()
        esperar(0.5)
        apertar_Tab(2,tempo_espera=0.1)
        enter()
        esperar(0.5)
        click(coordinates.x_espaco_Branco, coordinates.y_espaco_Branco)
        fazer = selecionar_resposta("Deseja ajustar o grid?", ["sim", "não"])
    