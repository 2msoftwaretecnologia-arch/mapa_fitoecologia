import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.interfaces.campo_dinamico_opcoes import *
from functions.pyaytogui.funcoes_teclado_mouse import * 
from functions.pyaytogui.mexer_mouse import * 
from functions.outras_funcoes.helpers import *
from functions.manipular_windos.manipular_windos import *
from functions.interfaces.alerta_simples import *

def abrir_console():
    pyautogui.hotkey('ctrl','m')

def apertar_ctrl_home():
    pyautogui.hotkey('ctrl', 'home')
    
def apertar_ctrl_end(tempo=0.1):
    pyautogui.hotkey('ctrl', 'end')
    esperar(tempo)

def renomear_arcgis():
    pyautogui.press('f2')
    esperar(0.2)
    
def abrir_textos():
    pyautogui.hotkey('ctrl','h')