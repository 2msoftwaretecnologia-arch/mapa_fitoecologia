import time
import pyperclip


def limpar_area_transferencia():
    """
    Limpa a área de transferência.
    """
    pyperclip.copy("")
    print("Área de transferência limpa.")


def esperar(segundos):
    """
    Função para pausar a execução do programa por um determinado número de segundos.
    
    Args:
        segundos (int): Número de segundos para pausar.
    """
    time.sleep(segundos)