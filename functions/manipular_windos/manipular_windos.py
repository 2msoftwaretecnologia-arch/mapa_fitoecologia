import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pyperclip


def copiar_para_area_transferencia(texto):
    """
    Copia o texto fornecido para a área de transferência.
    """
    pyperclip.copy(texto)
    print("Texto copiado para a área de transferência.")

def limpar_area_transferencia():
    """
    Limpa a área de transferência.
    """
    pyperclip.copy("")
    print("Área de transferência limpa.")


