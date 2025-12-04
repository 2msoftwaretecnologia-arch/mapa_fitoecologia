import pyautogui
from typing import Literal

def desenhar_quadrado(
    x1: int,
    y1: int,
    largura: int = 166,
    altura: int = 120,
    duracao: float = 0.2
) -> None:
    """
    Desenha um quadrado (ou retângulo) na tela a partir do canto superior esquerdo.

    Parameters
    ----------
    x1 : int
        Coordenada X (horizontal) do canto superior esquerdo.
    y1 : int
        Coordenada Y (vertical) do canto superior esquerdo.
    largura : int, optional
        Largura do quadrado em pixels (padrão: 166).
    altura : int, optional
        Altura do quadrado em pixels (padrão: 120).
    duracao : float, optional
        Tempo em segundos para mover o mouse e arrastar (padrão: 0.2).

    Returns
    -------
    None
        A função não retorna valor — apenas executa ações na tela.

    Behavior
    --------
    1. Move o cursor até o ponto (x1, y1).
    2. Calcula o ponto inferior direito (x2, y2) com base na largura e altura.
    3. Realiza um "clique e arrasto" do ponto inicial até o ponto final.

    Examples
    --------
    >>> # Desenha um quadrado de 200x150 pixels começando em (500, 400)
    >>> desenhar_quadrado(500, 400, largura=200, altura=150)

    >>> # Desenha um quadrado padrão (166x120) começando em (100, 100)
    >>> desenhar_quadrado(100, 100)
    """
    # Move o cursor até o canto superior esquerdo
    pyautogui.moveTo(x1, y1, duration=duracao)
    
    # Calcula as coordenadas do canto inferior direito
    x2 = x1 + largura
    y2 = y1 + altura
    
    # Realiza o arrasto simulando o desenho do quadrado
    pyautogui.dragTo(x2, y2, duration=duracao, button='left')

def click(
    x: int | None = None,
    y: int | None = None,
    wait_time: float = 0.2,
    ammount_click: int = 1,
    button_side: Literal["left", "right"] = "left"
) -> None:
    """
    Realiza um clique (ou cliques) na tela.

    Parameters
    ----------
    x : int, optional
        Coordenada X (horizontal) onde clicar. Se None, clica na posição atual.
    y : int, optional
        Coordenada Y (vertical) onde clicar. Se None, clica na posição atual.
    wait_time : float, optional
        Tempo em segundos para mover o mouse até (x, y) antes de clicar (padrão: 0.2).
    ammount_click : int, optional
        Número de cliques a realizar (padrão: 1).
    button_side : Literal["left", "right"], optional
        Botão do mouse a usar (padrão: "left").

    Returns
    -------
    None
    """
    if x is None and y is None:
        pyautogui.click(clicks=ammount_click, button=button_side)
    elif x is not None and y is not None:
        pyautogui.click(x, y, duration=wait_time, clicks=ammount_click, button=button_side)
    else:
        raise ValueError("Ambos x e y devem ser fornecidos ou ambos devem ser None.")


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
