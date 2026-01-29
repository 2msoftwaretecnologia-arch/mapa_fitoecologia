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


    @property
    def x_arcgis(self) -> int:
        return self._x_arcgis
    
    @x_arcgis.setter
    def x_arcgis(self, new_x_arcgis: int) -> None:
        self._x_arcgis = new_x_arcgis

    @property
    def y_arcgis(self) -> int:
        return self._y_arcgis
    
    @y_arcgis.setter
    def y_arcgis(self, new_y_arcgis: int) -> None:
        self._y_arcgis = new_y_arcgis

    @property
    def largura_atual(self) -> int:
        return self._largura_atual
    
    @largura_atual.setter
    def largura_atual(self, new_largura_atual: int) -> None:
        self._largura_atual = new_largura_atual

    @property
    def altura_atual(self) -> int:
        return self._altura_atual
    
    @altura_atual.setter
    def altura_atual(self, new_altura_atual: int) -> None:
        self._altura_atual = new_altura_atual

