import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buildkite.Windows.manipular_windos import *
import pyautogui

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