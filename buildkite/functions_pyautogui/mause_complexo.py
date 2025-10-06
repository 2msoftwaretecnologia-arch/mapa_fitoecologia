"""
Módulo para desenho automatizado de formas geométricas usando PyAutoGUI.

Atualmente, contém uma função principal:
    - desenhar_quadrado: desenha um retângulo (ou quadrado) na tela,
      a partir do canto superior esquerdo e dimensões definidas.

Dependência:
------------
- pyautogui
"""

import pyautogui


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
