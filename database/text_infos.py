# ============================================================
# 🧩 CLASSE: Text_infos
# ============================================================
# Classe usada como estrutura central para armazenar informações
# textuais e contextuais da propriedade, do mapa e dos elementos
# que compõem a análise atual.
#
# Ela serve como um “repositório temporário” para dados que serão
# usados em várias etapas do sistema — desde geração de mapas até
# criação de notas técnicas e relatórios automáticos.
# ============================================================

class Text_infos:
    """
    ============================================================
    🧠 CLASSE: Text_infos
    ============================================================

    📋 DESCRIÇÃO:
        Armazena informações principais sobre:
        - Identificação da propriedade e do proprietário
        - Contexto geográfico (cidade/UF)
        - Tipo e características do mapa sendo processado
        - Camadas e itens de interesse do mapa atual

        É usada como base para comunicação entre diferentes
        módulos do sistema (interfaces, scripts, banco de dados, etc.)
        evitando repetições e facilitando o transporte de dados.

    ⚙️ ATRIBUTOS:
        lista_camadas (list):
            Lista com os nomes das camadas ativas no mapa atual.

        proprietario (str):
            Nome do proprietário da área.

        matricula (str):
            Número da matrícula do imóvel (registro cartorial).

        city_uf (str):
            Cidade e UF onde a propriedade está localizada.

        property_name (str):
            Nome oficial da fazenda/propriedade.

        tipo_dominante_fitoecologia (str):
            Tipo de vegetação predominante (para mapa de fitoecologia).

        tipo_dominante_geologia (str):
            Tipo de formação predominante (para mapa de geologia/geomorfologia).

        current_items (list):
            Lista de elementos ativos no mapa atual (ex: polígonos, shapefiles, legendas etc.).

        kind_mapa (str):
            Tipo do mapa em uso. Exemplos: "Fitoecologia", "Geologia".

        requied_quantity_current_map (int):
            Número de elementos obrigatórios para o mapa estar completo.

        descricao_mapa_atual (dict):
            Dicionário com detalhes do mapa (ex: legenda, escala, título).

        current_map_path (str):
            Caminho absoluto do arquivo de mapa atual (.mxd, .shp, etc.).

    ============================================================
    """

    def __init__(
        self,
        lista_camadas: list,
        owner: str,
        registration_property: str,
        city_uf: str,
        property_name: str,
        tipo_dominante_fitoecologia: str,
        tipo_dominante_geologia: str,
        current_items: list,
        kind_mapa: str,
        requied_quantity_current_map: int,
        descricao_mapa_atual: dict,
        current_map_path: str,
    ) -> None:
        """
        ============================================================
        🔧 CONSTRUTOR
        ============================================================
        Inicializa o objeto `Text_infos` com todos os campos
        necessários para representar o contexto textual de uma
        propriedade ou de um mapa técnico.

        Args:
            lista_camadas (list): Lista com nomes das camadas carregadas.
            proprietario (str): Nome do proprietário.
            matricula (str): Número da matrícula.
            city_uf (str): Cidade e estado (ex: "Porto Nacional - TO").
            property_name (str): Nome da propriedade.
            tipo_dominante_fitoecologia (str): Vegetação dominante.
            tipo_dominante_geologia (str): Formação geológica dominante.
            current_items (list): Lista de itens ativos do mapa.
            kind_mapa (str): Tipo do mapa atual ("Fitoecologia", "Geologia", etc.).
            requied_quantity_current_map (int): Quantidade mínima de camadas obrigatórias.
            descricao_mapa_atual (dict): Informações descritivas (legenda, escala, etc.).
            current_map_path (str): Caminho absoluto do arquivo do mapa atual.
        ============================================================
        """

        # ============================================================
        # 📦 ATRIBUTOS BÁSICOS
        # ============================================================
        self._lista_camadas = lista_camadas
        self.owner = owner
        self.registration_property = registration_property
        self.city_uf = city_uf
        self.property_name = property_name

        # ============================================================
        # 🌳 INFORMAÇÕES TÉCNICAS DE MAPA
        # ============================================================
        self.tipo_dominante_fitoecologia = tipo_dominante_fitoecologia
        self.tipo_dominante_geologia = tipo_dominante_geologia
        self.current_items = current_items
        self.kind_mapa = kind_mapa
        self.requied_quantity_current_map = requied_quantity_current_map
        self.descricao_mapa_atual = descricao_mapa_atual
        self.current_map_path = current_map_path
        self.current_map_path = current_map_path
        

    @property
    def lista_camadas(self) -> list:
        return self._lista_camadas

    @lista_camadas.setter
    def lista_camadas(self, new_lista_camadas: list) -> None:
        self._lista_camadas = new_lista_camadas

    @property
    def descricao_mapa_atual(self) -> list:
        return self._descricao_mapa_atual

    @descricao_mapa_atual.setter
    def descricao_mapa_atual(self, new_descricao_mapa_atual: list) -> None:
        self._descricao_mapa_atual = new_descricao_mapa_atual

    @property
    def current_map_path(self) -> str:
        return self._current_map_path

    @current_map_path.setter
    def current_map_path(self, new_current_map_path: str) -> None:
        self._current_map_path = new_current_map_path

    @property
    def owner(self) -> str:
        return self._owner
    
    @owner.setter
    def owner(self, new_owner: str) -> None:
        self._owner = new_owner
    
    @property
    def registration_property(self) -> str:
        return self._registration_property
    
    @registration_property.setter
    def registration_property(self, new_registration_property: str) -> None:
        self._registration_property = new_registration_property

    @property
    def city_uf(self) -> str:
        return self._city_uf
    
    @city_uf.setter
    def city_uf(self, new_city_uf: str) -> None:
        self._city_uf = new_city_uf

    @property
    def property_name(self) -> str:
        return self._property_name
    
    @property_name.setter
    def property_name(self, new_property_name: str) -> None:
        self._property_name = new_property_name

    @property
    def tipo_dominante_fitoecologia(self) -> str:
        return self._tipo_dominante_fitoecologia
    
    @tipo_dominante_fitoecologia.setter
    def tipo_dominante_fitoecologia(self, new_tipo_dominante_fitoecologia: str) -> None:
        self._tipo_dominante_fitoecologia = new_tipo_dominante_fitoecologia

    @property
    def tipo_dominante_geologia(self) -> str:
        return self._tipo_dominante_geologia
    
    @tipo_dominante_geologia.setter
    def tipo_dominante_geologia(self, new_tipo_dominante_geologia: str) -> None:
        self._tipo_dominante_geologia = new_tipo_dominante_geologia

    @property
    def current_items(self) -> list:
        return self._current_items
    
    @current_items.setter
    def current_items(self, new_current_items: list) -> None:
        self._current_items = new_current_items

    @property
    def kind_mapa(self) -> str:
        return self._kind_mapa
    
    @kind_mapa.setter
    def kind_mapa(self, new_kind_mapa: str) -> None:
        self._kind_mapa = new_kind_mapa

    @property
    def requied_quantity_current_map(self) -> int:
        return self._requied_quantity_current_map
    
    @requied_quantity_current_map.setter
    def requied_quantity_current_map(self, new_requied_quantity_current_map: int) -> None:
        self._requied_quantity_current_map = new_requied_quantity_current_map
