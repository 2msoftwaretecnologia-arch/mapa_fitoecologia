# ============================================================
# 🧩 CLASSE: coordinates
# ============================================================
# Representa um conjunto de coordenadas e dimensões da tela do
# usuário, geralmente utilizadas para automações gráficas (ex:
# PyAutoGUI, ArcGIS, QGIS, etc.).
#
# Essa classe mantém as coordenadas do clique no ArcGIS e também
# armazena a resolução atual do monitor, permitindo ajustar ações
# automaticamente conforme o tamanho da tela.
# ============================================================
class coordinates:
    """
    ============================================================
    🧠 CLASSE: coordinates
    ============================================================

    📋 DESCRIÇÃO:
        Armazena e gerencia informações de posição e dimensão da tela
        utilizadas em processos de automação (ex: captura de cliques
        no ArcGIS, posicionamento de elementos, etc.).

    ⚙️ ATRIBUTOS:
        x_arcgis (int):
            Coordenada X do ponto de referência capturado no ArcGIS.

        y_arcgis (int):
            Coordenada Y do ponto de referência capturado no ArcGIS.

        largura_atual (int):
            Largura atual do monitor do usuário.

        altura_atual (int):
            Altura atual do monitor do usuário.

    ============================================================
    """
    def __init__(
        self,
        
       
        x_arcgis: int,
        Y_arcgis: int,
        largura_atual: int,
        altura_atual: int,
        x_espaco_Branco: int,
        y_espaco_Branco: int,
        x_ponto_incial: int,
        y_ponto_incial: int,
        x_size_position: int,
        y_size_position: int,
       
        
    ):
        """
        ============================================================
        🔧 CONSTRUTOR
        ============================================================
        Inicializa a classe com as coordenadas e as dimensões
        atuais do monitor.

        Args:
            x_arcgis (int): Coordenada X do ponto clicado.
            y_arcgis (int): Coordenada Y do ponto clicado.
            largura_atual (int): Largura do monitor em pixels.
            altura_atual (int): Altura do monitor em pixels.
        ============================================================
        """
        self.x_arcgis = x_arcgis
        self.Y_arcgis = Y_arcgis
        self.largura_atual = largura_atual
        self.altura_atual = altura_atual
        self.x_espaco_Branco = x_espaco_Branco
        self.y_espaco_Branco = y_espaco_Branco
        self.x_ponto_incial = x_ponto_incial
        self.y_ponto_incial = y_ponto_incial
        self.x_size_position = x_size_position
        self.y_size_position = y_size_position

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
    def y_espaco_Branco(self, novo_y_espaco_Branco: int) -> None:
        self._y_espaco_Branco = novo_y_espaco_Branco
    
    @property
    def x_ponto_incial(self) -> int:
        return self._x_ponto_incial
    
    @x_ponto_incial.setter
    def x_ponto_incial(self, novo_x_ponto_incial: int) -> None:
        self._x_ponto_incial = novo_x_ponto_incial
    
    @property
    def y_ponto_incial(self) -> int:
        return self._y_ponto_incial
    
    @y_ponto_incial.setter
    def y_ponto_incial(self, novo_y_ponto_incial: int) -> None:
        self._y_ponto_incial = novo_y_ponto_incial

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
    def y_size_position(self, novo_y_size_position: int) -> None:
        self._y_size_position = novo_y_size_position