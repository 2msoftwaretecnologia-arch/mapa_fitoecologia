import pyautogui


refazer_escala = pyautogui.confirm(text="Deseja substituir a escala?", buttons=["sim", "não"])

print(refazer_escala)