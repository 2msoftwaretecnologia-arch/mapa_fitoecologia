import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from typing import Tuple, Union, List

def quebrar_texto(
    texto: str,
    limite: int,
    multi: bool = True,
    duas_variaveis: bool = False,
) -> Union[str, Tuple[str, str]]:
    """
    Quebra o texto em múltiplas linhas ou apenas uma vez, de acordo com o limite.
    Se duas_variaveis=True, retorna (parte1, parte2).
    """

    if not multi:
        if len(texto) <= limite:
            return (texto, "") if duas_variaveis else texto

        # Procura o último espaço antes do limite
        pos = texto.rfind(" ", 0, limite + 1)
        if pos == -1:  # se não tiver espaço, quebra no limite bruto
            pos = limite

        parte1 = texto[:pos].rstrip()
        parte2 = texto[pos:].lstrip()
        return (parte1, parte2) if duas_variaveis else (parte1 + "\n" + parte2)

    # Caso padrão: múltiplas quebras (word wrap)
    palavras = texto.split()
    linhas: List[str] = []
    linha_atual = ""

    for palavra in palavras:
        candidato = (palavra if not linha_atual else f"{linha_atual} {palavra}")
        if len(candidato) <= limite:
            linha_atual = candidato
        else:
            if linha_atual:
                linhas.append(linha_atual)
            linha_atual = palavra

    if linha_atual:
        linhas.append(linha_atual)

    if duas_variaveis:
        primeira = linhas[0] if linhas else ""
        resto = "\n".join(linhas[1:]) if len(linhas) > 1 else ""
        return (primeira, resto)

    return "\n".join(linhas)


