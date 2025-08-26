import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class Text_infos:
    def __init__(
        self,
        lista_camadas: list,
        proprietario: str,
        matricula: str,
        cidade_uf: str,
        nome_propriedade: str,
        tipo_dominante: str,
        fito_ecologias: list,
    ):
        
        self._lista_camadas = lista_camadas
        self.proprietario = proprietario
        self.matricula = matricula
        self.cidade_uf = cidade_uf
        self.nome_propriedade = nome_propriedade
        self.tipo_dominante = tipo_dominante
        self.fito_ecologias = fito_ecologias
        

    @property
    def lista_camadas(self) -> list:
        return self._lista_camadas

    @lista_camadas.setter
    def lista_camadas(self, nova_lista_camadas: list) -> None:
        self._lista_camadas = nova_lista_camadas

    @property
    def proprietario(self) -> str:
        return self._proprietario
    
    @proprietario.setter
    def proprietario(self, novo_proprietario: str) -> None:
        self._proprietario = novo_proprietario
    
    @property
    def matricula(self) -> str:
        return self._matricula
    
    @matricula.setter
    def matricula(self, nova_matricula: str) -> None:
        self._matricula = nova_matricula

    @property
    def cidade_uf(self) -> str:
        return self._cidade_uf
    
    @cidade_uf.setter
    def cidade_uf(self, nova_cidade_uf: str) -> None:
        self._cidade_uf = nova_cidade_uf

    @property
    def nome_propriedade(self) -> str:
        return self._nome_propriedade
    
    @nome_propriedade.setter
    def nome_propriedade(self, novo_nome_propriedade: str) -> None:
        self._nome_propriedade = novo_nome_propriedade

    @property
    def tipo_dominante(self) -> str:
        return self._tipo_dominante
    
    @tipo_dominante.setter
    def tipo_dominante(self, novo_tipo_dominante: str) -> None:
        self._tipo_dominante = novo_tipo_dominante

    @property
    def fito_ecologias(self) -> str:
        return self._fito_ecologias
    
    @fito_ecologias.setter
    def fito_ecologias(self, novo_fito_ecologias: str) -> None:
        self._fito_ecologias = novo_fito_ecologias
