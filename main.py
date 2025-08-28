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
from functions.kivy.input_Texto_dinamico import *
from functions.kivy.campo_dinamico_opcoes import *

from functions.kivy.alerta_simples import *

Fechar = pyautogui.confirm(title="Confirmação",text="começar??",buttons=["sim","Não"])
if Fechar == "sim":

    janela_dinamica(texto='ATENÇÃO!!!,\n se atente a todos as mensagens de texto que ira aparecer na sua tela')
    colar_scripts()
    fazer_grid()
    ajustar_escala()
    ajustar_quadrados_fitoecologia()
    ajustar_info_propriedade()
    fazer_nota_tencnica()
    fazer_parte_legenda()