import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.input_Texto_dinamico import *
from functions.interfaces.campo_dinamico_opcoes import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.pyaytogui.localizacao import *
from functions.pyaytogui.protecao import *
from functions.outras_funcoes.helpers import *
from functions.outras_funcoes.helpers import *
from functions.manipular_windos.capturar_click import *
from functions.outras_funcoes.coordenadas import *
from functions.interfaces.alerta_simples import *


def fazer_grid():
    try:
        fazer = "sim"
        x_espaco_vazio, y_espaco_vazio =  capturar_clique("clique em um espaço vazio fora do mapa para eu saber onde fica")
        coordinates.x_espaco_Branco = x_espaco_vazio
        coordinates.y_espaco_Branco = y_espaco_vazio
        esperar(1)
        while fazer == 'sim':
            clicar_centro_tela(1)
            insert(1)
            clicar_centro_tela(1)
            esperar(0.5)
            pyautogui.click(button="right")#TODO: ajustar essa função aqui depois
            esperar(0.5)
            cima()
            enter()
            
            janela_dinamica("espere a janela de propriedades abrir")
            if not isinstance(coordinates.x_grid, int):
                janela_dinamica(texto='ATENÇÃO!!!, aperte no grid ate que ele fique embaixo antes de apertar Entendi')
                x_grid , y_grid = capturar_clique("aperte no grid ")
                coordinates.x_grid = x_grid
                coordinates.y_grid = y_grid
                esperar(1)
                click(x_grid , y_grid,clicks_quant=3)
            else:
                click(coordinates.x_grid , coordinates.y_grid,clicks_quant=3)
            apertar_Tab(5,tempo_espera=0.1)
            enter()
            
            esperar(0.5)
            
            grid_atual = input_texto_dinamico("Digite o valor do grid lembrando\n que esse valor vai ser multiplicado por 100")
            
            apertar_Tab(1)
            grid_atual = int(grid_atual)*100
            escrever_texto(str(grid_atual))
            escrever_texto(str(".000000"))
            esperar(0.2)
            apertar_Tab(2,0)
            escrever_texto(str(grid_atual))
            escrever_texto(str(".000000"))
            enter()
            esperar(0.5)
            apertar_Tab(2,tempo_espera=0.1)
            enter()
            esperar(0.5)
            click(coordinates.x_espaco_Branco, coordinates.y_espaco_Branco)
            fazer = pyautogui.confirm(title="Confirmação",text="deseja ajustar grid??",buttons=["sim","Não"])
    except Exception as e:
        print(f"Erro ao ajustar o grid: {e}")