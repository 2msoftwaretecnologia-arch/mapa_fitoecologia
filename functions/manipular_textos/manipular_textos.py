import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

def quebrar_texto(texto: str, limite: int) -> str:
    """
    Quebra o texto em múltiplas linhas de acordo com o limite de caracteres.

    :param texto: Texto a ser quebrado.
    :param limite: Número máximo de caracteres por linha.
    :return: Texto com quebras de linha.
    """
    palavras = texto.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 <= limite:
            linha_atual += (palavra + " ")
        else:
            linhas.append(linha_atual.strip())
            linha_atual = palavra + " "
    if linha_atual:
        linhas.append(linha_atual.strip())

    return "\\n".join(linhas)

