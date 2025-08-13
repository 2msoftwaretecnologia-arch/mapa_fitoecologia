import pyautogui
import keyboard
import time
#importar pastas dentro de pastas
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def click(x,y,tempo=0.2,clicks_quant=1):
    pyautogui.click(x, y, duration=tempo,clicks=clicks_quant)   

def clicar_botao(botao='left'):
   
    pyautogui.click(button=botao,interval=0.25)

def clicar_centro_tela(quantidade=1):
    for _ in range(quantidade):
        pyautogui.click(pyautogui.size()[0]//2,pyautogui.size()[1]//2,duration=0.25)
        time.sleep(0.25)

def apertar_pra_baixo(quantidae=1,tempo_espera=0.1):
    for _ in range(quantidae):
        pyautogui.press('down')
        time.sleep(tempo_espera)
    
def apertar_home():
    pyautogui.press('home')
      
def apertar_Tab(quantidade=1,tempo_espera=0.3):
    """Pressiona a tecla Tab."""
    for _ in range(quantidade):
        pyautogui.press('tab')
        time.sleep(tempo_espera)


def escrever_texto(texto,velocidade=0.01):
    keyboard.write(texto,delay=velocidade)

def apertar_espaco():
    pyautogui.press('space')

def copiar():
    pyautogui.hotkey('ctrl','c')

def enter(quantidade=1,tempo=0.3):
    for _ in range(quantidade):
        pyautogui.press('enter')
        time.sleep(tempo)
    

def esquerda(quantidade,tempo=0.1):
    for _ in range(quantidade):
        pyautogui.press('left')
        time.sleep(tempo)

def direita(quantidade=1,tempo=0.1):
    for _ in range(quantidade):
        pyautogui.press('right')
        time.sleep(tempo)
    

def cima(quantidade=1,tempo=0.2):
    for _ in range(quantidade):
        pyautogui.press('up')
        time.sleep(tempo)

def insert(quantidade=1):
    for _ in range(quantidade):
        pyautogui.press('insert')
        time.sleep(0.1)

def colar():
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)

def apertar_esc(quantidade=1):
    for _ in range(quantidade):
        pyautogui.press('esc')
        time.sleep(0.1)

def selecionar_tudo(quantidade=1,tempo=0.2):
    for _ in range(quantidade):
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(tempo)

def pressionar_tecla(tecla, quantidade=1, tempo=0.1):
    for _ in range(quantidade):
        pyautogui.press(tecla)
        time.sleep(tempo)


def selecionar_tudo_Word():
    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.2)

def centralizar_texto_Word():
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(0.2)

def escolher_fonte_Word():
    pyautogui.hotkey('ctrl', 'shift', 'f')
    time.sleep(0.5)