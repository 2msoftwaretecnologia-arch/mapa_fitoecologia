from database.text_infos import *
import pyautogui


def input_texto_dinamico(texto):
    resposta = pyautogui.prompt(texto, title='Entrada de Texto')
    return resposta

def janela_dinamica(texto):
    pyautogui.alert(texto, title='Atenção!!!', button='OK')

def confirmar_inicio():
    """Pergunta ao usuário se deseja iniciar o processo."""
    resposta = pyautogui.confirm(title="Confirmação", text="Começar o processo?", buttons=["Sim", "Não"])
    return resposta == "Sim"


def escolher_tipo_mapa():
    """Permite ao usuário escolher o tipo de mapa."""
    tipo = pyautogui.confirm(title="Tipo de Mapa", text="Qual o tipo do mapa?", buttons=["Fitoecologia", "Geologia"])
    Text_infos.tipo_mapa = tipo
    return tipo
