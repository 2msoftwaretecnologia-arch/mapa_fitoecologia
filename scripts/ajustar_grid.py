import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.functions_pyautogui.funcoes_teclado_mouse import click_center_screen,cima,enter , click,apertar_Tab,escrever_texto,press_insert
from buildkite.interfaces.janelas_dinamicas import BRAKE_WINDOW,input_texto_dinamico
from buildkite.interfaces.simple_interface import simple_choices
from database.requests import get_or_set_coordinate
from buildkite.Windows.manipular_windos import esperar
from database.coordenadas import coordinates
import pyautogui

def set_grid():
    try:
        espaco_branco_coordenadas = get_or_set_coordinate(2,"clique em um espaço vazio fora do mapa para eu saber onde fica")
        coordinates.x_espaco_Branco = espaco_branco_coordenadas[0]
        coordinates.y_espaco_Branco = espaco_branco_coordenadas[1]
        click_center_screen()
        esperar(0.3)
        click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1])
        esperar(1)
        build_grid = simple_choices(text_content="Deseja substituir o grid?", choices_buttons=["sim", "não"])
        while build_grid == 'sim':
            click_center_screen()
            press_insert()
            click_center_screen()
            esperar(0.5)
            pyautogui.click(button="right")#TODO: ajustar essa função aqui depois
            esperar(0.5)
            cima()
            enter()
            
            BRAKE_WINDOW("espere a janela de propriedades abrir")
            BRAKE_WINDOW(mensagem='ATENÇÃO!!!, aperte no grid ate que ele fique embaixo antes de apertar Entendi')
            grid_coordenadas = get_or_set_coordinate(8,"aperte no grid")
            esperar(0.3)
            click(grid_coordenadas[0] , grid_coordenadas[1],clicks_quant=3)
            apertar_Tab(5,tempo_espera=0.01)
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
            apertar_Tab(2,tempo_espera=0.01)
            enter()
            esperar(0.5)
            click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1])
            build_grid = pyautogui.confirm(text="Deseja substituir o grid?", buttons=["sim", "não"])
    except Exception as e:
        print(f"Erro ao ajustar o grid: {e}")