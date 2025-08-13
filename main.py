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
from functions.manipular_arcgis.colar_ia_texto import *
from functions.manipular_arcgis.ajustar_nota_Tecnica import *
from functions.outras_funcoes.helpers import *
from functions.tkinter.input_Texto_dinamico import *
from functions.tkinter.campo_dinamico_opcoes import *
from functions.tkinter.alerta_dinamico import *
from functions.tkinter.alerta_simples import *

Fechar = selecionar_resposta("Realmente deseja abrir a automação?\ndo mapa de Fitosionomia?", ["Sim", "não"])
if Fechar == "Sim":
    janela_dinamica("abra o arcgis")
    show_alert_dinamic("ATENÇÃO!!!, não se esqueça de colocar todos os arquivos shps que voce vai utilizar antes de apertar 'entendi'")
    
    colar_scripts()
    
    fazer_grid()
    ajustar_escala()
    
    fazer_legenda_com_ia()
    fazer_nota_tencnica()
    
    
    