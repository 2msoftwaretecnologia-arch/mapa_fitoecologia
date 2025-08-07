import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class coordinates:
    def __init__(
        self,
        fechar_console_x: int,
        fechar_console_y: int,
        x_console_quadro: int,
        y_console_quadro: int,
        x_camada: int,
        y_camada: int,
        x_escala: int,
        y_escala: int,
        x_espaco_Branco: int,
        y_espaco_Branco: int,
        
    ):
        self._fechar_console_x = fechar_console_x
        self._fechar_console_y = fechar_console_y
        self._x_console_quadro = x_console_quadro
        self._y_console_quadro = y_console_quadro
        self._x_camada = x_camada
        self._y_camada = y_camada

    @property
    def fechar_console_x(self) -> int:
        return self._fechar_console_x

    @fechar_console_x.setter
    def fechar_console_x(self, novo_fechar_console_x: int) -> None:
        self._fechar_console_x = novo_fechar_console_x

    @property
    def fechar_console_y(self) -> int:
        return self._fechar_console_y

    @fechar_console_y.setter
    def fechar_console_y(self, nova_fechar_console_y: int) -> None:
        self._fechar_console_y = nova_fechar_console_y

    @property
    def x_console_quadro(self) -> int:
        return self._x_console_quadro

    @x_console_quadro.setter
    def x_console_quadro(self, novo_x_console_quadro: int) -> None:
        self._x_console_quadro = novo_x_console_quadro

    @property
    def y_console_quadro(self) -> int:
        return self._y_console_quadro

    @y_console_quadro.setter
    def y_console_quadro(self, nova_y_console_quadro: int) -> None:
        self._y_console_quadro = nova_y_console_quadro


    @property
    def x_camada(self) -> int:
        return self._x_camada
    
    @x_camada.setter
    def x_camada(self, novo_x_camada: int) -> None:
        self._x_camada = novo_x_camada

    @property
    def y_camada(self) -> int:
        return self._y_camada
    
    @y_camada.setter
    def y_camada(self, nova_y_camada: int) -> None:
        self._y_camada = nova_y_camada

    @property
    def x_escala(self) -> int:
        return self._x_escala
    
    @x_escala.setter
    def x_escala(self, novo_x_escala: int) -> None:
        self._x_escala = novo_x_escala

    @property
    def y_escala(self) -> int:
        return self._y_escala
    
    @y_escala.setter
    def y_escala(self, nova_y_escala: int) -> None:
        self._y_escala = nova_y_escala

    @property
    def x_espaco_Branco(self) -> int:
        return self._x_espaco_Branco
    
    @x_espaco_Branco.setter
    def x_espaco_Branco(self, novo_x_espaco_Branco: int) -> None:
        self._x_espaco_Branco = novo_x_espaco_Branco

    @property
    def y_espaco_Branco(self) -> int:
        return self._y_espaco_Branco
    
    @y_espaco_Branco.setter
    def y_espaco_Branco(self, nova_y_espaco_Branco: int) -> None:
        self._y_espaco_Branco = nova_y_espaco_Branco