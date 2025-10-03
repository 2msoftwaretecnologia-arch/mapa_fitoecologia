import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.pyautogui.protecao import *
from functions.outras_funcoes.helpers import *
from functions.pyautogui.funcoes_teclado_mouse import *
from functions.interfaces.input_Texto_dinamico import *
from database.requests import *

def fazer_grid():
    try:
        fazer = "sim"
        espaco_branco_coordenadas = request("get",objeto_id=2)
        if espaco_branco_coordenadas == (0,0):
            x_espaco_vazio, y_espaco_vazio =  capturar_clique("clique em um espaço vazio fora do mapa para eu saber onde fica")
            request("set",objeto_id=2,x=x_espaco_vazio,y=y_espaco_vazio)
            espaco_branco_coordenadas = request("get",objeto_id=2)
        else:
            esperar(0.2)
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
            
            janela_dinamica("espere a janela de propriedades abrir")
            janela_dinamica(texto='ATENÇÃO!!!, aperte no grid ate que ele fique embaixo antes de apertar Entendi')
            grid_coordenadas = request("get",objeto_id=8)
            if grid_coordenadas == (0,0):
                x_grid , y_grid = capturar_clique("aperte no grid ")
                request("set",objeto_id=8,x=x_grid,y=y_grid)
                grid_coordenadas = request("get",objeto_id=8)
                esperar(1)
                click(grid_coordenadas[0] , grid_coordenadas[1],clicks_quant=3)
            else:
                esperar(0.2)
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