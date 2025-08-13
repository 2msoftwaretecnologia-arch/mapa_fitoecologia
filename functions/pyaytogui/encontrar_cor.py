import pyautogui
import cv2
import numpy as np
import time



def encontrar_cor_e_mover_mouse(rgb_color=[212, 120, 0]):
    time.sleep(0.5)  # Espera meio segundo antes de começar a procurar a cor
    while True:
        # Define a cor alvo (em BGR porque OpenCV usa BGR, não RGB)
        target_color = np.array(rgb_color)  # (B, G, R)
        tolerance = 30  # tolerância para variação de cor

        # Captura da tela
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Calcula a máscara onde a cor corresponde à cor desejada com tolerância
        lower = np.clip(target_color - tolerance, 0, 255)
        upper = np.clip(target_color + tolerance, 0, 255)
        mask = cv2.inRange(frame, lower, upper)

        # Encontra os contornos (regiões onde a cor foi detectada)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Pega o maior contorno e move o mouse para o seu centro
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                pyautogui.moveTo(cX, cY, duration=0.1)  # move suavemente
            print("Cor encontrada. Parando...")
            break  # Sai do loop quando a cor é encontrada
        else:
            print("Cor não encontrada.")

        # Para evitar uso excessivo da CPU
        time.sleep(0.1)

