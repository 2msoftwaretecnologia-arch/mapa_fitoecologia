def format_path(path: str) -> str:
    """
    Formata um caminho de arquivo ou diretório para usar barras normais (/) em vez de barras invertidas (\).

    Parameters
    ----------
    path : str
        O caminho de arquivo ou diretório a ser formatado.

    Returns
    -------
    str
        O caminho formatado com barras normais.

    Examples
    --------
    >>> format_path("C:\\Users\\2mbet\\Desktop\\automacoes_envimap\\map_fitoecologia\\scripts\\selecao_apr.py")
    'C:/Users/2mbet/Desktop/automacoes_envimap/map_fitoecologia/scripts/selecao_apr.py'
    """
    return path.replace("/","\\")