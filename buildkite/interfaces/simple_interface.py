import pyautogui

def simple_choices(text_content:str,choices_buttons:list):
    """
    Exibe uma janela com um texto e botões de escolha.

    Parâmetros:
    text_content (str): O texto a ser exibido na janela.
    choices_buttons (list): Uma lista de strings representando os botões de escolha.

    Retorna:
    str: O texto do botão escolhido pelo usuário.
    """
    return pyautogui.confirm(text=text_content, buttons=choices_buttons)
