import pyautogui

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
