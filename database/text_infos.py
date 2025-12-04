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

        nome_propriedade (str):
            Nome oficial da fazenda/propriedade.

        tipo_dominante_fitoecologia (str):
            Tipo de vegetação predominante (para mapa de fitoecologia).

        tipo_dominante_geologia (str):
            Tipo de formação predominante (para mapa de geologia/geomorfologia).

        itens_atuais (list):
            Lista de elementos ativos no mapa atual (ex: polígonos, shapefiles, legendas etc.).

        tipo_mapa (str):
            Tipo do mapa em uso. Exemplos: "Fitoecologia", "Geologia".

        quantidade_necessario_mapa_atual (int):
            Número de elementos obrigatórios para o mapa estar completo.

        descricao_mapa_atual (dict):
            Dicionário com detalhes do mapa (ex: legenda, escala, título).

        caminho_mapa_atual (str):
            Caminho absoluto do arquivo de mapa atual (.mxd, .shp, etc.).

    ============================================================
    """

    def __init__(
        self,
        lista_camadas: list,
        owner: str,
        registration_property: str,
        city_uf: str,
        nome_propriedade: str,
        tipo_dominante_fitoecologia: str,
        tipo_dominante_geologia: str,
        itens_atuais: list,
        tipo_mapa: str,
        quantidade_necessario_mapa_atual: int,
        descricao_mapa_atual: dict,
        caminho_mapa_atual: str,
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
            nome_propriedade (str): Nome da propriedade.
            tipo_dominante_fitoecologia (str): Vegetação dominante.
            tipo_dominante_geologia (str): Formação geológica dominante.
            itens_atuais (list): Lista de itens ativos do mapa.
            tipo_mapa (str): Tipo do mapa atual ("Fitoecologia", "Geologia", etc.).
            quantidade_necessario_mapa_atual (int): Quantidade mínima de camadas obrigatórias.
            descricao_mapa_atual (dict): Informações descritivas (legenda, escala, etc.).
            caminho_mapa_atual (str): Caminho absoluto do arquivo do mapa atual.
        ============================================================
        """

        # ============================================================
        # 📦 ATRIBUTOS BÁSICOS
        # ============================================================
        self._lista_camadas = lista_camadas
        self.owner = owner
        self.registration_property = registration_property
        self.city_uf = city_uf
        self.nome_propriedade = nome_propriedade

        # ============================================================
        # 🌳 INFORMAÇÕES TÉCNICAS DE MAPA
        # ============================================================
        self.tipo_dominante_fitoecologia = tipo_dominante_fitoecologia
        self.tipo_dominante_geologia = tipo_dominante_geologia
        self.itens_atuais = itens_atuais
        self.tipo_mapa = tipo_mapa
        self.quantidade_necessario_mapa_atual = quantidade_necessario_mapa_atual
        self.descricao_mapa_atual = descricao_mapa_atual
        self.caminho_mapa_atual = caminho_mapa_atual
        self.caminho_mapa_atual = caminho_mapa_atual
        

    @property
    def lista_camadas(self) -> list:
        return self._lista_camadas

    @lista_camadas.setter
    def lista_camadas(self, nova_lista_camadas: list) -> None:
        self._lista_camadas = nova_lista_camadas

    @property
    def descricao_mapa_atual(self) -> list:
        return self._descricao_mapa_atual

    @descricao_mapa_atual.setter
    def descricao_mapa_atual(self, nova_descricao_mapa_atual: list) -> None:
        self._descricao_mapa_atual = nova_descricao_mapa_atual

    @property
    def caminho_mapa_atual(self) -> str:
        return self._caminho_mapa_atual

    @caminho_mapa_atual.setter
    def caminho_mapa_atual(self, nova_caminho_mapa_atual: str) -> None:
        self._caminho_mapa_atual = nova_caminho_mapa_atual

    @property
    def owner(self) -> str:
        return self._owner
    
    @owner.setter
    def owner(self, novo_owner: str) -> None:
        self._owner = novo_owner
    
    @property
    def registration_property(self) -> str:
        return self._registration_property
    
    @registration_property.setter
    def registration_property(self, nova_registration_property: str) -> None:
        self._registration_property = nova_registration_property

    @property
    def city_uf(self) -> str:
        return self._city_uf
    
    @city_uf.setter
    def city_uf(self, nova_city_uf: str) -> None:
        self._city_uf = nova_city_uf

    @property
    def nome_propriedade(self) -> str:
        return self._nome_propriedade
    
    @nome_propriedade.setter
    def nome_propriedade(self, novo_nome_propriedade: str) -> None:
        self._nome_propriedade = novo_nome_propriedade

    @property
    def tipo_dominante_fitoecologia(self) -> str:
        return self._tipo_dominante_fitoecologia
    
    @tipo_dominante_fitoecologia.setter
    def tipo_dominante_fitoecologia(self, novo_tipo_dominante_fitoecologia: str) -> None:
        self._tipo_dominante_fitoecologia = novo_tipo_dominante_fitoecologia

    @property
    def tipo_dominante_geologia(self) -> str:
        return self._tipo_dominante_geologia
    
    @tipo_dominante_geologia.setter
    def tipo_dominante_geologia(self, novo_tipo_dominante_geologia: str) -> None:
        self._tipo_dominante_geologia = novo_tipo_dominante_geologia

    @property
    def itens_atuais(self) -> list:
        return self._itens_atuais
    
    @itens_atuais.setter
    def itens_atuais(self, novo_itens_atuais: list) -> None:
        self._itens_atuais = novo_itens_atuais

    @property
    def tipo_mapa(self) -> str:
        return self._tipo_mapa
    
    @tipo_mapa.setter
    def tipo_mapa(self, novo_tipo_mapa: str) -> None:
        self._tipo_mapa = novo_tipo_mapa

    @property
    def quantidade_necessario_mapa_atual(self) -> int:
        return self._quantidade_necessario_mapa_atual
    
    @quantidade_necessario_mapa_atual.setter
    def quantidade_necessario_mapa_atual(self, novo_quantidade_necessario_mapa_atual: int) -> None:
        self._quantidade_necessario_mapa_atual = novo_quantidade_necessario_mapa_atual
