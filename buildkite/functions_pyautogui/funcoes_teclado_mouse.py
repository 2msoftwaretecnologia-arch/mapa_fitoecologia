import pyautogui
import keyboard
import time


# ============================================================
# FUNÇÕES DE CLIQUE E POSICIONAMENTO DO MOUSE
# ============================================================

def click_center_screen(ammount: int = 1) -> None:
    """
    Clica no centro da tela uma ou mais vezes.

    Parameters
    ----------
    ammount : int, optional
        ammount de cliques no centro da tela (padrão: 1).

    Returns
    -------
    None
    """
    for _ in range(ammount):
        width, height = pyautogui.size()
        pyautogui.click(width // 2, height // 2, duration=0.25)
        time.sleep(0.25)


# ============================================================
# FUNÇÕES DE TECLADO BÁSICAS
# ============================================================

def press_down(ammount: int = 1, wait_time: float = 0.1) -> None:
    """
    Pressiona a tecla 'seta para baixo' repetidamente.

    Parameters
    ----------
    ammount : int, optional
        Quantas vezes pressionar (padrão: 1).
    tempo_espera : float, optional
        Intervalo entre as pressões (padrão: 0.1 segundos).

    Returns
    -------
    None
    """
    for _ in range(ammount):
        pyautogui.press('down')
        time.sleep(wait_time)


def press_home(ammount: int = 1, wait_time: float = 0) -> None:
    """
    Pressiona a tecla 'Home' repetidamente.

    Parameters
    ----------
    ammount : int, optional
        Quantas vezes pressionar (padrão: 1).
    wait_time : float, optional
        Intervalo entre as pressões (padrão: 0 segundos).
    """
    for _ in range(ammount):
        pyautogui.press('home')
        time.sleep(wait_time)


def press_tab(ammount: int = 1, wait_time: float = 0.3) -> None:
    """
    Pressiona a tecla 'Tab' repetidamente.

    Parameters
    ----------
    ammount : int, optional
        Quantidade de pressões (padrão: 1).
    wait_time : float, optional
        Intervalo entre as pressões (padrão: 0.3 segundos).
    """
    for _ in range(ammount):
        pyautogui.press('tab')
        time.sleep(wait_time)


def write_text(text: str, speed: float = 0.01) -> None:
    """
    Digita texto simulando digitação humana.

    Parameters
    ----------
    text : str
        Texto a ser digitado.
    speed : float, optional
        Intervalo entre cada caractere (padrão: 0.01 segundos).
    """
    keyboard.write(text=text, delay=speed)


def press_space(ammount: int = 1, wait_time: float = 0) -> None:
    """Pressiona a tecla 'Espaço' repetidamente."""
    for _ in range(ammount):
        pyautogui.press('space')
        time.sleep(wait_time)


def copy() -> None:
    """Executa o atalho Ctrl + C (copiar)."""
    pyautogui.hotkey('ctrl', 'c')


def paste() -> None:
    """Executa o atalho Ctrl + V (colar)."""
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)


def press_enter(ammount: int = 1, wait_time: float = 0.3) -> None:
    """Pressiona a tecla 'Enter' repetidamente."""
    for _ in range(ammount):
        pyautogui.press('enter')
        time.sleep(wait_time)


def press_esc(ammount: int = 1, wait_time: float = 0.1) -> None:
    """Pressiona a tecla 'Esc' repetidamente."""
    for _ in range(ammount):
        pyautogui.press('esc')
        time.sleep(wait_time)


# ============================================================
# MOVIMENTAÇÃO ENTRE CAMPOS E SELEÇÃO
# ============================================================

def press_left(ammount: int = 1, wait_time: float = 0.1) -> None:
    """Move o cursor para a esquerda."""
    for _ in range(ammount):
        pyautogui.press('left')
        time.sleep(wait_time)


def press_right(ammount: int = 1, wait_time: float = 0.1) -> None:
    """Move o cursor para a direita."""
    for _ in range(ammount):
        pyautogui.press('right')
        time.sleep(wait_time)


def press_up(ammount: int = 1, wait_time: float = 0.2) -> None:
    """Move o cursor para cima."""
    for _ in range(ammount):
        pyautogui.press('up')
        time.sleep(wait_time)


def press_insert(ammount: int = 1, wait_time: float = 0.2) -> None:
    """Pressiona a tecla 'insert' repetidamente."""
    for _ in range(ammount):
        pyautogui.press('insert')
        time.sleep(wait_time)


def select_all(ammount: int = 1, wait_time: float = 0.2) -> None:
    """Seleciona todo o conteúdo (Ctrl + A)."""
    for _ in range(ammount):
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(wait_time)


def press_key(key: str, ammount: int = 1, wait_time: float = 0.1) -> None:
    """
    Pressiona qualquer tecla especificada repetidamente.

    Parameters
    ----------
    key : str
        Nome da tecla (ex.: 'enter', 'tab', 'a', 'f1').
    ammount : int, optional
        Quantas vezes pressionar (padrão: 1).
    wait_time : float, optional
        Intervalo entre as pressões (padrão: 0.1 segundos).
    """
    for _ in range(ammount):
        pyautogui.press(key)
        time.sleep(wait_time)


# ============================================================
# ATALHOS ESPECÍFICOS DO MICROSOFT WORD
# ============================================================

def select_all_in_Word(ammount: int = 1, wait_time: float = 0.5) -> None:
    """Seleciona todo o texto no Word (Ctrl + T)."""
    for _ in range(ammount):
        pyautogui.hotkey('ctrl', 't')
        time.sleep(wait_time)


def center_text_in_Word(ammount: int = 1, wait_time: float = 0.2) -> None:
    """Centraliza o texto no Word (Ctrl + E)."""
    for _ in range(ammount):
        pyautogui.hotkey('ctrl', 'e')
        time.sleep(wait_time)


def choose_font_in_Word(ammount: int = 1, wait_time: float = 0.5) -> None:
    """Abre a janela de seleção de fonte no Word (Ctrl + Shift + F)."""
    for _ in range(ammount):
        pyautogui.hotkey('ctrl', 'shift', 'f')
        time.sleep(wait_time)


def open_page_margin_Word(ammount: int = 1, wait_time: float = 0.2) -> None:
    """
    Abre a janela de configuração de margens no Word (Ctrl + L).

    Parameters
    ----------
    ammount : int, optional
        Quantidade de vezes que o atalho será repetido (padrão: 1).
    wait_time : float, optional
        Intervalo entre repetições (padrão: 0.2 segundos).
    """
    for _ in range(ammount):
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(wait_time)

# ============================================================
# FUNÇÕES DE TECLADO ARCGIS
# ============================================================

def press_ctrl_home(ammount: int = 1, wait_time: float = 0) -> None:
    """
    Pressiona a tecla 'Ctrl + Home' repetidamente.

    Parameters
    ----------
    ammount : int, optional
        Quantidade de vezes que a tecla será pressionada (padrão: 1).
    wait_time : float, optional
        Intervalo entre cada pressionamento (padrão: 0.0 segundos).
    """
    for _ in range(ammount):
        pyautogui.hotkey('ctrl', 'home')
        time.sleep(wait_time)
    
def press_ctrl_end(ammount: int = 1, wait_time: float = 0.1) -> None:
    """
    Pressiona a tecla 'Ctrl + End' repetidamente.

    Parameters
    ----------
    ammount : int, optional
        Quantidade de vezes que a tecla será pressionada (padrão: 1).
    wait_time : float, optional
        Intervalo entre cada pressionamento (padrão: 0.1 segundos).
    """
    for _ in range(ammount):
        pyautogui.hotkey('ctrl', 'end')
        time.sleep(wait_time)

def rename_arcgis(ammount: int = 1, wait_time: float = 0.2) -> None:
    """
    Renomeia o objeto no ArcGIS (F2).

    Parameters
    ----------
    ammount : int, optional
        Quantidade de vezes que a tecla será pressionada (padrão: 1).
    wait_time : float, optional
        Intervalo entre cada pressionamento (padrão: 0.2 segundos).
    """
    for _ in range(ammount):
        pyautogui.press('f2')
        time.sleep(wait_time)
    
def create_text(wait_time = 0):
    pyautogui.hotkey('ctrl','h')
    time.sleep(wait_time)

def save_mxj(wait_time=0.2):
    pyautogui.hotkey('ctrl','j')
    time.sleep(wait_time)

def save_mapa_export(wait_time=0.2):
    pyautogui.hotkey('ctrl','k')
    time.sleep(wait_time)
