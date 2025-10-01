import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class coordinates:
    def __init__(
        self,
        x_camada: int,
        y_camada: int,
        x_escala: int,
        y_escala: int,
        x_espaco_Branco: int,
        y_espaco_Branco: int,
        x_retangulo: int,
        y_retangulo: int,
        x_desenhar_quadradro: int,
        y_desenhar_quadradro: int,
        x_symbol_quadrado: int,
        y_symbol_quadrado: int,
        x_fill_color_quadrado: int,
        y_fill_color_quadrado: int,
        x_out_line_color_quadrado: int,
        y_out_line_color_quadrado: int,
        x_grid: int,
        y_grid: int,
        x_incio: int,
        y_incio: int,
        x_arcgis: int,
        Y_arcgis: int,
        x_size_position: int,
        y_size_position: int,
        
    ):
        self._x_camada = x_camada
        self._y_camada = y_camada
        self.x_escala = x_escala
        self.y_escala = y_escala
        self.x_espaco_Branco = x_espaco_Branco
        self.y_espaco_Branco = y_espaco_Branco
        self.x_retangulo = x_retangulo
        self.y_retangulo = y_retangulo
        self.x_desenhar_quadradro = x_desenhar_quadradro
        self.y_desenhar_quadradro = y_desenhar_quadradro
        self.x_symbol_quadrado = x_symbol_quadrado
        self.y_symbol_quadrado = y_symbol_quadrado
        self.x_fill_color_quadrado = x_fill_color_quadrado
        self.y_fill_color_quadrado = y_fill_color_quadrado
        self.x_out_line_color_quadrado = x_out_line_color_quadrado
        self.y_out_line_color_quadrado = y_out_line_color_quadrado
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.x_incio = x_incio
        self.y_incio = y_incio
        self.x_arcgis = x_arcgis
        self.Y_arcgis = Y_arcgis


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

    @property
    def x_retangulo(self) -> int:
        return self._x_retangulo
    
    @x_retangulo.setter
    def x_retangulo(self, novo_x_retangulo: int) -> None:
        self._x_retangulo = novo_x_retangulo

    @property
    def y_retangulo(self) -> int:
        return self._y_retangulo
    
    @y_retangulo.setter
    def y_retangulo(self, nova_y_retangulo: int) -> None:
        self._y_retangulo = nova_y_retangulo

    @property
    def x_desenhar_quadradro(self) -> int:
        return self._x_desenhar_quadradro
    
    @x_desenhar_quadradro.setter
    def x_desenhar_quadradro(self, novo_x_desenhar_quadradro: int) -> None:
        self._x_desenhar_quadradro = novo_x_desenhar_quadradro

    @property
    def y_desenhar_quadradro(self) -> int:
        return self._y_desenhar_quadradro
    
    @y_desenhar_quadradro.setter
    def y_desenhar_quadradro(self, nova_y_desenhar_quadradro: int) -> None:
        self._y_desenhar_quadradro = nova_y_desenhar_quadradro

    @property
    def x_symbol_quadrado(self) -> int:
        return self._x_symbol_quadrado
    
    @x_symbol_quadrado.setter
    def x_symbol_quadrado(self, novo_x_symbol_quadrado: int) -> None:
        self._x_symbol_quadrado = novo_x_symbol_quadrado

    @property
    def y_symbol_quadrado(self) -> int:
        return self._y_symbol_quadrado
    
    @y_symbol_quadrado.setter
    def y_symbol_quadrado(self, nova_y_symbol_quadrado: int) -> None:
        self._y_symbol_quadrado = nova_y_symbol_quadrado

    @property
    def x_fill_color_quadrado(self) -> int:
        return self._x_fill_color_quadrado
    
    @x_fill_color_quadrado.setter
    def x_fill_color_quadrado(self, novo_x_fill_color_quadrado: int) -> None:
        self._x_fill_color_quadrado = novo_x_fill_color_quadrado

    @property
    def y_fill_color_quadrado(self) -> int:
        return self._y_fill_color_quadrado
    
    @y_fill_color_quadrado.setter
    def y_fill_color_quadrado(self, nova_y_fill_color_quadrado: int) -> None:
        self._y_fill_color_quadrado = nova_y_fill_color_quadrado

    @property
    def x_out_line_color_quadrado(self) -> int:
        return self._x_out_line_color_quadrado
    
    @x_out_line_color_quadrado.setter
    def x_out_line_color_quadrado(self, novo_x_out_line_color_quadrado: int) -> None:
        self._x_out_line_color_quadrado = novo_x_out_line_color_quadrado

    @property
    def y_out_line_color_quadrado(self) -> int:
        return self._y_out_line_color_quadrado
    
    @y_out_line_color_quadrado.setter
    def y_out_line_color_quadrado(self, nova_y_out_line_color_quadrado: int) -> None:
        self._y_out_line_color_quadrado = nova_y_out_line_color_quadrado

    @property
    def x_grid(self) -> int:
        return self._x_grid
    
    @x_grid.setter
    def x_grid(self, novo_x_grid: int) -> None:
        self._x_grid = novo_x_grid

    @property
    def y_grid(self) -> int:
        return self._y_grid
    
    @y_grid.setter
    def y_grid(self, nova_y_grid: int) -> None:
        self._y_grid = nova_y_grid

    @property
    def x_incio(self) -> int:
        return self._x_incio
    
    @x_incio.setter
    def x_incio(self, novo_x_incio: int) -> None:
        self._x_incio = novo_x_incio

    @property
    def y_incio(self) -> int:
        return self._y_incio
    
    @y_incio.setter
    def y_incio(self, nova_y_incio: int) -> None:
        self._y_incio = nova_y_incio

    @property
    def x_arcgis(self) -> int:
        return self._x_arcgis
    
    @x_arcgis.setter
    def x_arcgis(self, novo_x_arcgis: int) -> None:
        self._x_arcgis = novo_x_arcgis

    @property
    def y_arcgis(self) -> int:
        return self._y_arcgis
    
    @y_arcgis.setter
    def y_arcgis(self, nova_y_arcgis: int) -> None:
        self._y_arcgis = nova_y_arcgis

    @property
    def x_size_position(self) -> int:
        return self._x_size_position
    
    @x_size_position.setter
    def x_size_position(self, novo_x_size_position: int) -> None:
        self._x_size_position = novo_x_size_position

    @property
    def y_size_position(self) -> int:
        return self._y_size_position
    
    @y_size_position.setter
    def y_size_position(self, nova_y_size_position: int) -> None:
        self._y_size_position = nova_y_size_position

