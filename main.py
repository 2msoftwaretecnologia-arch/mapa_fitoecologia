import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from functions.manipular_textos.manipular_textos import *
from functions.manipular_windos.manipular_windos import *
from functions.pyaytogui.funcoes_teclado_mouse import *
from functions.pyaytogui.localizacao import *
from functions.manipular_arcgis.ajustar_grid import *
from functions.manipular_arcgis.ajustar_escala import *
from functions.manipular_arcgis.scritpts_leves import *
from functions.manipular_arcgis.fazer_legenda_fitoecologias import *
from functions.manipular_arcgis.ajustar_nota_Tecnica import *
from functions.manipular_arcgis.ajustar_quadrados import *
from functions.manipular_arcgis.ajustar_legendas_propriedade import *
from functions.outras_funcoes.helpers import *
from functions.interfaces.input_Texto_dinamico import *
from functions.interfaces.campo_dinamico_opcoes import *
from functions.interfaces.alerta_simples import *
from functions.manipular_arcgis.selecao_apr import *
from functions.outras_funcoes.outras_infos import *

Fechar = pyautogui.confirm(title="Confirmação",text="começar??",buttons=["sim","Não"])
tipo_mapa = pyautogui.confirm(title="Confirmação",text="Qual o tipo do mapa?",buttons=["Fitoecologia","Geologia"])
Text_infos.tipo_mapa = tipo_mapa
if Fechar == "sim":
    if Text_infos.tipo_mapa == 'Fitoecologia':
        abrir_documento(caminho_mapa_fitoecologia)
    if Text_infos.tipo_mapa == 'Geologia':
        abrir_documento(caminho_mapa_geologia)
    abrir_documento(caminho_word_nota_tecnica)
    janela_dinamica(texto='ATENÇÃO!!!,\n se atente a todos as mensagens de texto que ira aparecer na sua tela')
    janela_dinamica(texto='ATENÇÃO!!!,\n espere carregar todos os documentos e depois aperte ok')
    colar_scripts()
    selecionar_apr()
    ajustar_escala()
    fazer_grid()
    ajustar_quadrados_mapa(Text_infos.tipo_mapa)
    ajustar_info_propriedade()
    fazer_nota_tencnica(Text_infos.tipo_mapa)
    fazer_parte_legenda(Text_infos.tipo_mapa)