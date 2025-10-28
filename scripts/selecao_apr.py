import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.text_infos import Text_infos
from buildkite.Windows.manipular_windos import esperar
from buildkite.functions_tkinter.interfaces import escolher_shp
from buildkite.functions_pyautogui.funcoes_teclado_mouse import (clicar_centro_tela,click,enter,apertar_ctrl_home,
                                                                 apertar_pra_baixo,apertar_Tab,escrever_texto,pressionar_tecla)
from buildkite.utils.helpers import esperar_aii,janela_pausa
from database.requests import get_or_set_coordinate

def selecionar_apr():
    
    var_apr = escolher_shp("escolha o shp da apr")
    var_aii = esperar_aii(var_apr)
    var_apr = var_apr.replace("/","\\")
    var_aii = var_aii.replace("/","\\")
    Text_infos.caminho_mapa_atual = var_apr
    camada_cordenadas = get_or_set_coordinate(objeto_id=1,mensagem="Clique na lista onde fica a Layer principal do mapa")
    clicar_centro_tela()
    esperar(0.2)
    click(camada_cordenadas[0],camada_cordenadas[1])
    esperar(0.5)
    apertar_ctrl_home()
    esperar(0.5)
    apertar_pra_baixo(1)
    esperar(0.2)
    enter()
    esperar(0.5)
    janela_pausa("Espere a seleção ser concluída e aperte Entendi")
    source_cordenadas = get_or_set_coordinate(objeto_id=12,mensagem="Clique no botão 'Source'")
    click(source_cordenadas[0],source_cordenadas[1],clicks_quant=3)
    esperar(0.3)
    apertar_Tab(6,tempo_espera=0.01)
    enter()
    janela_pausa("Espere a seleção ser concluída e aperte Entendi")
    esperar(0.3)
    input_caminho = get_or_set_coordinate(14,"Clique no campo onde digitamos o caminho do shp")
    esperar(0.3)
    click(input_caminho[0],input_caminho[1])
    escrever_texto(var_apr,velocidade=0.002)
    enter()
    esperar(0.2)
    apertar_Tab(1)
    esperar(0.2)
    enter()
    pressionar_tecla("f2",tempo=0.4)
    escrever_texto(f'{Text_infos.nome_propriedade} - A.P.R',velocidade=0.002)
    enter(tempo=0.5)
    apertar_pra_baixo(2)
    esperar(0.2)
    enter()
    janela_pausa("Espere a seleção ser concluída e aperte Entendi")
    click(source_cordenadas[0],source_cordenadas[1],clicks_quant=3)
    esperar(0.5)
    apertar_Tab(6,tempo_espera=0.01)
    enter()
    esperar(0.5)
    escrever_texto(var_aii,velocidade=0.002)
    enter()
    esperar(0.2)
    apertar_Tab(1)
    esperar(0.2)
    enter()
    esperar(1)
    
    #modificando a camada de baixo
    if Text_infos.tipo_mapa == 'Fitoecologia':
        apertar_pra_baixo(18,tempo_espera=0.002)
    if Text_infos.tipo_mapa == 'Geologia':
        apertar_pra_baixo(10,tempo_espera=0.002)
    if Text_infos.tipo_mapa == 'Pedologia':
        apertar_pra_baixo(10,tempo_espera=0.002)
    if Text_infos.tipo_mapa == 'Regioes_climaticas':
        apertar_pra_baixo(10,tempo_espera=0.002)
    if Text_infos.tipo_mapa == 'Declividade':
        apertar_pra_baixo(10,tempo_espera=0.002)
    if Text_infos.tipo_mapa == 'Erodibilidade':
        apertar_pra_baixo(10,tempo_espera=0.002)
    
    esperar(0.2)
    enter()
    janela_pausa("Espere a seleção ser concluída e aperte Entendi")
    click(source_cordenadas[0],source_cordenadas[1],clicks_quant=3)
    esperar(0.5)
    apertar_Tab(6,tempo_espera=0.01)
    enter()
    esperar(1)
    escrever_texto(var_apr,velocidade=0.002)
    enter()
    esperar(0.2)
    apertar_Tab(1)
    esperar(0.2)
    enter()
    pressionar_tecla("f2",tempo=0.4)
    escrever_texto(f'{Text_infos.nome_propriedade} - A.P.R',velocidade=0.002)
    enter(tempo=0.5)
    apertar_pra_baixo(2)
    esperar(0.2)
    enter()
    janela_pausa("Espere a seleção ser concluída e aperte Entendi")
    click(source_cordenadas[0],source_cordenadas[1],clicks_quant=3)
    esperar(0.2)
    apertar_Tab(6,tempo_espera=0.01)
    enter()
    esperar(0.5)
    escrever_texto(var_aii,velocidade=0.002)
    enter()
    esperar(0.2)
    apertar_Tab(1)
    esperar(0.2)
    enter()
    esperar(1)