class coordinates:
    def __init__(
        self,
        
       
        x_arcgis: int,
        Y_arcgis: int,
        largura_atual: int,
        altura_atual: int,
       
        
    ):
        self.x_arcgis = x_arcgis
        self.Y_arcgis = Y_arcgis
        self.largura_atual = largura_atual
        self.altura_atual = altura_atual

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
    def largura_atual(self) -> int:
        return self._largura_atual
    
    @largura_atual.setter
    def largura_atual(self, novo_largura_atual: int) -> None:
        self._largura_atual = novo_largura_atual

    @property
    def altura_atual(self) -> int:
        return self._altura_atual
    
    @altura_atual.setter
    def altura_atual(self, nova_altura_atual: int) -> None:
        self._altura_atual = nova_altura_atual

