import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.functions_pyautogui.funcoes_teclado_mouse import clicar_centro_tela,cima,enter , click,apertar_Tab,escrever_texto,insert
from buildkite.interfaces.janelas_dinamicas import janela_pausa,input_texto_dinamico
from database.requests import get_or_set_coordinate
from buildkite.Windows.manipular_windos import esperar
from database.coordenadas import coordinates
import pyautogui

def fazer_grid():
    try:
        fazer = "sim"
        espaco_branco_coordenadas = get_or_set_coordinate(2,"clique em um espaço vazio fora do mapa para eu saber onde fica")
        coordinates.x_espaco_Branco = espaco_branco_coordenadas[0]
        coordinates.y_espaco_Branco = espaco_branco_coordenadas[1]
        clicar_centro_tela()
        esperar(0.3)
        click(espaco_branco_coordenadas[0],espaco_branco_coordenadas[1])
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
            
            janela_pausa("espere a janela de propriedades abrir")
            janela_pausa(mensagem='ATENÇÃO!!!, aperte no grid ate que ele fique embaixo antes de apertar Entendi')
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
            fazer = pyautogui.confirm(title="Confirmação",text="deseja ajustar grid??",buttons=["sim","Não"])
    except Exception as e:
        print(f"Erro ao ajustar o grid: {e}")