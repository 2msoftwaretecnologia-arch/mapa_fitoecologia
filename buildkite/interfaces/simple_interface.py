import pyautogui
import time
from database.text_infos import Text_infos
def simple_choices(title = "", text: str = "Escolha uma opção", choices_buttons: list = None):

    """
    Exibe uma janela com um texto e botões de escolha.

    Parâmetros:
    text (str): O texto a ser exibido na janela.
    title (str): O título da janela (padrão: "Escolha uma opção").
    choices_buttons (list): Uma lista de strings representando os botões de escolha.

    Retorna:
    str: O texto do botão escolhido pelo usuário.
    """
    return pyautogui.confirm(text=text, title=title, buttons=choices_buttons)


def operation_mode(secod_option,tempo: float = 0.2,):
    """
    Exibe uma janela com um texto e botões de escolha.

    Parâmetros:
    text (str): O texto a ser exibido na janela.
    title (str): O título da janela (padrão: "Escolha o modo de operação").
    choices_buttons (list): Uma lista de strings representando os botões de escolha.

    Retorna:
    str: O texto do botão escolhido pelo usuário.
    """
    choose = Text_infos.operation_mode
    if choose == "rapido":
        time.sleep(tempo)
    elif choose == "normal":
        if callable(secod_option):
            return secod_option()
        return secod_option


#operation_mode(secod_option=lambda: simple_choices(title="Teste",choices_buttons=["Sim", "Não"]))