import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pyautogui
import time

def localizar_e_clicar(imagem, mensagem_erro, movimento_relativo=None, double_click=False,rightClick=False):
    try:
        # Localiza a imagem na tela com uma confiança de 70%
        image_location = pyautogui.locateOnScreen(imagem, confidence=0.8)
        if image_location:
            # Obtém o centro da imagem localizada
            image_center = pyautogui.center(image_location)
            pyautogui.moveTo(image_center,duration=0.1)  # Move o mouse para o centro da imagem localizada
            # Se houver movimento relativo especificado, realiza o movimento
            if movimento_relativo:
                pyautogui.moveRel(*movimento_relativo, duration=0.3)
            # Executa um clique ou duplo clique dependendo do parâmetro
            if double_click:
                pyautogui.doubleClick()
            elif rightClick:
                pyautogui.rightClick()
        
            else:
                pyautogui.click(duration=0.2)
            time.sleep(0.5)  # Espera meio segundo após o clique
        else:
            # Imprime uma mensagem de erro se a imagem não for encontrada
            pyautogui.alert(mensagem_erro)
          
    except pyautogui.ImageNotFoundException:
        # Captura a exceção caso a imagem não seja encontrada
        pyautogui.alert(mensagem_erro)