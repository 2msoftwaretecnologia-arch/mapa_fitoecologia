from typing import Tuple, Union, List

def quebrar_texto(
    texto: str,
    limite: int,
    multi: bool = True,
    duas_variaveis: bool = False,
) -> Union[str, Tuple[str, str]]:
    """
    ============================================================
    🧠 FUNÇÃO: quebrar_texto(texto, limite, multi=True, duas_variaveis=False)
    ============================================================

    📋 DESCRIÇÃO:
        Quebra o texto em múltiplas linhas ou apenas uma vez,
        respeitando o limite de caracteres informado.

        Essa função é útil para formatar textos longos em relatórios,
        caixas de texto, ou gerar quebras automáticas de linha sem cortar palavras.

    ⚙️ PARÂMETROS:
        texto (str):
            O texto completo a ser quebrado.

        limite (int):
            Quantidade máxima de caracteres por linha antes da quebra.

        multi (bool, opcional):
            - Se True (padrão): quebra o texto em múltiplas linhas (word wrap).
            - Se False: quebra apenas uma vez, no último espaço antes do limite.

        duas_variaveis (bool, opcional):
            - Se True: retorna duas partes separadas (tupla: parte1, parte2)
            - Se False: retorna o texto completo já formatado com "\n"

    🎯 RETORNO:
        Union[str, Tuple[str, str]]:
            - Se duas_variaveis=False → retorna o texto quebrado como string.
            - Se duas_variaveis=True  → retorna uma tupla (parte1, parte2).

    💡 EXEMPLOS DE USO:
        >>> quebrar_texto("Este é um exemplo de texto longo", 10)
        'Este é um\nexemplo de\ntexto longo'

        >>> quebrar_texto("Este é um exemplo de texto longo", 10, multi=False)
        'Este é um\nexemplo de texto longo'

        >>> quebrar_texto("Texto grande demais", 8, multi=False, duas_variaveis=True)
        ('Texto', 'grande demais')

    ============================================================
    """

    # ============================================================
    # 🧩 CASO 1 — Quebra simples (multi=False)
    # ============================================================
    if not multi:
        # Se o texto já for menor que o limite, retorna direto
        if len(texto) <= limite:
            return (texto, "") if duas_variaveis else texto

        # Procura o último espaço antes do limite para evitar cortar palavras
        pos = texto.rfind(" ", 0, limite + 1)

        # Se não houver espaço (ex: palavra contínua), quebra no limite bruto
        if pos == -1:
            pos = limite

        # Divide o texto em duas partes e remove espaços extras
        parte1 = texto[:pos].rstrip()
        parte2 = texto[pos:].lstrip()

        # Retorna de acordo com o modo de saída
        return (parte1, parte2) if duas_variaveis else (parte1 + "\n" + parte2)

    # ============================================================
    # 🧩 CASO 2 — Quebra múltipla (multi=True)
    # ============================================================

    # Divide o texto em palavras
    palavras = texto.split()

    linhas: List[str] = []  # lista com as linhas já formatadas
    linha_atual = ""        # acumula as palavras até atingir o limite

    # Itera sobre cada palavra do texto
    for palavra in palavras:
        # Monta a linha candidata com a nova palavra
        candidato = palavra if not linha_atual else f"{linha_atual} {palavra}"

        # Se ainda está dentro do limite, mantém a linha atual
        if len(candidato) <= limite:
            linha_atual = candidato
        else:
            # Quando ultrapassa o limite, salva a linha atual e começa nova
            if linha_atual:
                linhas.append(linha_atual)
            linha_atual = palavra  # inicia nova linha com a palavra atual

    # Adiciona a última linha se houver conteúdo
    if linha_atual:
        linhas.append(linha_atual)

    # ============================================================
    # 🧾 Retorno condicional conforme duas_variaveis
    # ============================================================
    if duas_variaveis:
        # Retorna a primeira linha separada do restante
        primeira = linhas[0] if linhas else ""
        resto = "\n".join(linhas[1:]) if len(linhas) > 1 else ""
        return (primeira, resto)

    # Caso padrão: retorna todas as linhas unidas por "\n"
    return "\n".join(linhas)
