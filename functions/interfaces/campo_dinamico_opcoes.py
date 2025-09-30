import pyautogui


def input_texto_dinamico(texto):
    resposta = pyautogui.prompt(texto, title='Entrada de Texto')
    return resposta