import pyautogui

# Função para desenhar um quadrado com base apenas no canto superior esquerdo
def desenhar_quadrado(x1, y1, largura=166, altura=120, duracao=0.2):
    # Move para o canto superior esquerdo
    pyautogui.moveTo(x1, y1, duration=duracao)
    
    # Calcula o canto inferior direito
    x2 = x1 + largura
    y2 = y1 + altura
    
    # Arrasta até o canto inferior direito
    pyautogui.dragTo(x2, y2, duration=duracao, button='left')