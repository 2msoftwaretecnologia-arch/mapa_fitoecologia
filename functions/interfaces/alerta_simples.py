import pyautogui


def janela_dinamica(texto):
    pyautogui.alert(texto, title='Atenção!!!', button='OK')