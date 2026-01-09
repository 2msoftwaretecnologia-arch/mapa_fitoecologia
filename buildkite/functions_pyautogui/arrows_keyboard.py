import pyautogui
import time

class ArrowsKeyboard:
    def __init__(self):
        pass

    def _press_down(ammount: int = 1, wait_time: float = 0.1) -> None:
        """
        Pressiona a tecla 'seta para baixo' repetidamente.

        Parameters
        ----------
        ammount : int, optional
            Quantas vezes pressionar (padrão: 1).
        wait_time : float, optional
            Intervalo entre as pressões (padrão: 0.1 segundos).

        Returns
        -------
        None
        """
        for _ in range(ammount):
            pyautogui.press('down')
            time.sleep(wait_time)

    def _press_left(ammount: int = 1, wait_time: float = 0.1) -> None:
        """Move o cursor para a esquerda."""
        for _ in range(ammount):
            pyautogui.press('left')
            time.sleep(wait_time)


    def _press_right(ammount: int = 1, wait_time: float = 0.1) -> None:
        """Move o cursor para a direita."""
        for _ in range(ammount):
            pyautogui.press('right')
            time.sleep(wait_time)


    def _press_up(ammount: int = 1, wait_time: float = 0.2) -> None:
        """Move o cursor para cima."""
        for _ in range(ammount):
            pyautogui.press('up')
            time.sleep(wait_time)
