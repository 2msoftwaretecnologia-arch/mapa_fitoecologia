import pyautogui


def mover_mouse(lado, duracao, distancia,click=False,botao='left'):
    """
    Move o mouse em uma direção a partir da posição atual.
    
    Parâmetros:
    - lado: str -> 'esquerda', 'direita', 'cima', 'baixo'
    - duracao: float -> tempo em segundos para o movimento
    - distancia: int -> quantidade de pixels para mover
    """
    
    # Obtém a posição atual do mouse
    x_atual, y_atual = pyautogui.position()
    
    # Calcula a nova posição com base na direção
    if lado == 'esquerda':
        novo_x = x_atual - distancia
        novo_y = y_atual
    elif lado == 'direita':
        novo_x = x_atual + distancia
        novo_y = y_atual
    elif lado == 'cima':
        novo_x = x_atual
        novo_y = y_atual - distancia
    elif lado == 'baixo':
        novo_x = x_atual
        novo_y = y_atual + distancia
    else:
        raise ValueError("Direção inválida. Use: 'esquerda', 'direita', 'cima' ou 'baixo'")
    
    # Move o mouse para a nova posição com a duração especificada
    pyautogui.moveTo(novo_x, novo_y, duration=duracao)

    if click:
        pyautogui.click(button=botao)