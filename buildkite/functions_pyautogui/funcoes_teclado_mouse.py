"""
Módulo utilitário para automação de teclado e mouse.

Este módulo contém funções simples e reutilizáveis para controlar o mouse e o teclado
usando as bibliotecas `pyautogui` e `keyboard`.

Dependências:
-------------
- pyautogui
- keyboard
- time

As funções são projetadas para serem simples, diretas e facilmente combináveis
em rotinas mais complexas de automação.
"""

import pyautogui
import keyboard
import time
from typing import Literal


# ============================================================
# FUNÇÕES DE CLIQUE E POSICIONAMENTO DO MOUSE
# ============================================================

def click(x: int, y: int, tempo: float = 0.2, clicks_quant: int = 1, botao: Literal["left", "right"] = "left") -> None:
    """
    Realiza um ou mais cliques em uma posição específica da tela.

    Parameters
    ----------
    x : int
        Coordenada horizontal do clique.
    y : int
        Coordenada vertical do clique.
    tempo : float, optional
        Duração do movimento do cursor até o ponto (padrão: 0.2 segundos).
    clicks_quant : int, optional
        Número de cliques consecutivos (padrão: 1).
    botao : {"left", "right"}, optional
        Botão do mouse a ser usado (padrão: "left").

    Returns
    -------
    None

    Examples
    --------
    >>> click(500, 300)
    >>> click(800, 600, tempo=0.5, clicks_quant=2, botao="right")
    """
    pyautogui.click(x, y, duration=tempo, clicks=clicks_quant, button=botao)


def clicar_centro_tela(quantidade: int = 1) -> None:
    """
    Clica no centro da tela uma ou mais vezes.

    Parameters
    ----------
    quantidade : int, optional
        Quantidade de cliques no centro da tela (padrão: 1).

    Returns
    -------
    None
    """
    for _ in range(quantidade):
        largura, altura = pyautogui.size()
        pyautogui.click(largura // 2, altura // 2, duration=0.25)
        time.sleep(0.25)


# ============================================================
# FUNÇÕES DE TECLADO BÁSICAS
# ============================================================

def apertar_pra_baixo(quantidade: int = 1, tempo_espera: float = 0.1) -> None:
    """
    Pressiona a tecla 'seta para baixo' repetidamente.

    Parameters
    ----------
    quantidade : int, optional
        Quantas vezes pressionar (padrão: 1).
    tempo_espera : float, optional
        Intervalo entre as pressões (padrão: 0.1 segundos).

    Returns
    -------
    None
    """
    for _ in range(quantidade):
        pyautogui.press('down')
        time.sleep(tempo_espera)


def apertar_home() -> None:
    """Pressiona a tecla 'Home'."""
    pyautogui.press('home')


def apertar_Tab(quantidade: int = 1, tempo_espera: float = 0.3) -> None:
    """
    Pressiona a tecla 'Tab' repetidamente.

    Parameters
    ----------
    quantidade : int, optional
        Quantidade de pressões (padrão: 1).
    tempo_espera : float, optional
        Intervalo entre as pressões (padrão: 0.3 segundos).
    """
    for _ in range(quantidade):
        pyautogui.press('tab')
        time.sleep(tempo_espera)


def escrever_texto(texto: str, velocidade: float = 0.01) -> None:
    """
    Digita texto simulando digitação humana.

    Parameters
    ----------
    texto : str
        Texto a ser digitado.
    velocidade : float, optional
        Intervalo entre cada caractere (padrão: 0.01 segundos).
    """
    keyboard.write(text=texto, delay=velocidade)


def apertar_espaco() -> None:
    """Pressiona a tecla 'Espaço'."""
    pyautogui.press('space')


def copiar() -> None:
    """Executa o atalho Ctrl + C (copiar)."""
    pyautogui.hotkey('ctrl', 'c')


def colar() -> None:
    """Executa o atalho Ctrl + V (colar)."""
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)


def enter(quantidade: int = 1, tempo: float = 0.3) -> None:
    """Pressiona a tecla 'Enter' repetidamente."""
    for _ in range(quantidade):
        pyautogui.press('enter')
        time.sleep(tempo)


def apertar_esc(quantidade: int = 1) -> None:
    """Pressiona a tecla 'Esc' repetidamente."""
    for _ in range(quantidade):
        pyautogui.press('esc')
        time.sleep(0.1)


# ============================================================
# MOVIMENTAÇÃO ENTRE CAMPOS E SELEÇÃO
# ============================================================

def esquerda(quantidade: int = 1, tempo: float = 0.1) -> None:
    """Move o cursor para a esquerda."""
    for _ in range(quantidade):
        pyautogui.press('left')
        time.sleep(tempo)


def direita(quantidade: int = 1, tempo: float = 0.1) -> None:
    """Move o cursor para a direita."""
    for _ in range(quantidade):
        pyautogui.press('right')
        time.sleep(tempo)


def cima(quantidade: int = 1, tempo: float = 0.2) -> None:
    """Move o cursor para cima."""
    for _ in range(quantidade):
        pyautogui.press('up')
        time.sleep(tempo)


def insert(quantidade: int = 1, tempo: float = 0.2) -> None:
    """Pressiona a tecla 'Insert' repetidamente."""
    for _ in range(quantidade):
        pyautogui.press('insert')
        time.sleep(tempo)


def selecionar_tudo(quantidade: int = 1, tempo: float = 0.2) -> None:
    """Seleciona todo o conteúdo (Ctrl + A)."""
    for _ in range(quantidade):
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(tempo)


def pressionar_tecla(tecla: str, quantidade: int = 1, tempo: float = 0.1) -> None:
    """
    Pressiona qualquer tecla especificada repetidamente.

    Parameters
    ----------
    tecla : str
        Nome da tecla (ex.: 'enter', 'tab', 'a', 'f1').
    quantidade : int, optional
        Quantas vezes pressionar (padrão: 1).
    tempo : float, optional
        Intervalo entre as pressões (padrão: 0.1 segundos).
    """
    for _ in range(quantidade):
        pyautogui.press(tecla)
        time.sleep(tempo)


# ============================================================
# ATALHOS ESPECÍFICOS DO MICROSOFT WORD
# ============================================================

def selecionar_tudo_Word() -> None:
    """Seleciona todo o texto no Word (Ctrl + T)."""
    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.5)


def centralizar_texto_Word() -> None:
    """Centraliza o texto no Word (Ctrl + E)."""
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(0.2)


def escolher_fonte_Word() -> None:
    """Abre a janela de seleção de fonte no Word (Ctrl + Shift + F)."""
    pyautogui.hotkey('ctrl', 'shift', 'f')
    time.sleep(0.5)


def abrir_margen_pagina_Word(quantidade: int = 1, tempo: float = 0.2) -> None:
    """
    Abre a janela de configuração de margens no Word (Ctrl + L).

    Parameters
    ----------
    quantidade : int, optional
        Quantidade de vezes que o atalho será repetido (padrão: 1).
    tempo : float, optional
        Intervalo entre repetições (padrão: 0.2 segundos).
    """
    for _ in range(quantidade):
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(tempo)

# ============================================================
# FUNÇÕES DE TECLADO ARCGIS
# ============================================================

def apertar_ctrl_home():
    pyautogui.hotkey('ctrl', 'home')
    
def apertar_ctrl_end(tempo=0.1):
    pyautogui.hotkey('ctrl', 'end')
    time.sleep(tempo)

def renomear_arcgis():
    pyautogui.press('f2')
    time.sleep(0.2)
    
def abrir_textos():
    pyautogui.hotkey('ctrl','h')