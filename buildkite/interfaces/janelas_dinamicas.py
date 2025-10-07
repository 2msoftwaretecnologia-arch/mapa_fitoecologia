from typing import Optional, Sequence, Literal
import pyautogui
import os
import sys

# === Corrigir o caminho para o RAIZ do projeto (map_fitoecologia) ===
CURRENT_DIR = os.path.dirname(__file__)                                  # ...\buildkite\interfaces
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..'))        # ...\map_fitoecologia
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)  # prioriza o raiz do projeto


from database.text_infos import *  #TODO: Evite wildcard import: deixa claro o que usa


def input_texto_dinamico(mensagem: str, titulo: str = "Entrada de Texto") -> Optional[str]:
    """
    Solicita ao usuário um texto livre via caixa de diálogo.

    Parameters
    ----------
    mensagem : str
        Texto exibido na janela (ex.: "Digite o nome do proprietário:").
    titulo : str, optional
        Título da janela (padrão: "Entrada de Texto").

    Returns
    -------
    Optional[str]
        String digitada pelo usuário. Retorna `None` se o usuário cancelar/fechar a janela.

    Examples
    --------
    >>> nome = input_texto_dinamico("Digite o seu nome:")
    >>> if nome:
    ...     print(f"Olá, {nome}!")
    """
    resposta = pyautogui.prompt(text=mensagem, title=titulo)  # None se Cancelar
    return resposta


def janela_dinamica(mensagem: str, titulo: str = "Atenção!!!", botao: str = "OK") -> None:
    """
    Exibe uma janela de alerta simples com um único botão.

    Parameters
    ----------
    mensagem : str
        Conteúdo informativo do alerta.
    titulo : str, optional
        Título da janela (padrão: "Atenção!!!").
    botao : str, optional
        Rótulo do botão único (padrão: "OK").

    Returns
    -------
    None
        Não há valor de retorno. A função bloqueia até o usuário clicar no botão.

    Notes
    -----
    `pyautogui.alert` retorna o rótulo do botão clicado, mas como há um único botão
    o retorno não é necessário para controle de fluxo aqui.
    """
    pyautogui.alert(text=mensagem, title=titulo, button=botao)


def confirmar_inicio(
    titulo: str = "Confirmação",
    texto: str = "Começar o processo?",
    botoes: Sequence[str] = ("Sim", "Não"),
) -> bool:
    """
    Pergunta ao usuário se deseja iniciar um processo e retorna True/False.

    Parameters
    ----------
    titulo : str, optional
        Título da janela de confirmação (padrão: "Confirmação").
    texto : str, optional
        Texto exibido na janela (padrão: "Começar o processo?").
    botoes : Sequence[str], optional
        Botões exibidos na confirmação (padrão: ("Sim", "Não")).

    Returns
    -------
    bool
        `True` se o usuário clicar em "Sim".
        `False` se clicar em "Não" ou se fechar/cancelar a janela.

    Examples
    --------
    >>> if confirmar_inicio():
    ...     print("Iniciando...")
    ... else:
    ...     print("Ação cancelada.")
    """
    resposta = pyautogui.confirm(title=titulo, text=texto, buttons=list(botoes))
    return resposta == "Sim"




def escolher_tipo_mapa(
    opcoes: Sequence[str] = ("Fitoecologia", "Geologia"),
    titulo: str = "Tipo de Mapa",
    texto: str = "Qual o tipo do mapa?",
    definir_em_text_infos: bool = True,
) -> Optional[str]:
    """
    Permite ao usuário escolher o tipo de mapa e (opcionalmente) salva em `Text_infos.tipo_mapa`.

    Parameters
    ----------
    opcoes : Sequence[str], optional
        Opções apresentadas ao usuário (padrão: ("Fitoecologia", "Geologia")).
    titulo : str, optional
        Título da janela (padrão: "Tipo de Mapa").
    texto : str, optional
        Texto exibido na janela (padrão: "Qual o tipo do mapa?").
    definir_em_text_infos : bool, optional
        Se `True`, atribui o valor escolhido em `Text_infos.tipo_mapa` (padrão: True).

    Returns
    -------
    Optional[str]
        A opção escolhida pelo usuário. Retorna `None` se o usuário fechar/cancelar a janela.

    Side Effects
    ------------
    Quando `definir_em_text_infos=True`, define `Text_infos.tipo_mapa = <opção escolhida>`.

    Examples
    --------
    >>> tipo = escolher_tipo_mapa()
    >>> if tipo is None:
    ...     print("Usuário cancelou.")
    ... else:
    ...     print(f"Tipo selecionado: {tipo}")
    """

    # ===========================================
    # Definição local do tipo literal permitido
    # ===========================================
    TipoMapa = Literal["Fitoecologia", "Geologia"]

    # ===========================================
    # Exibe a janela de seleção para o usuário
    # ===========================================
    tipo: TipoMapa | None = pyautogui.confirm( # type: ignore
        title=titulo,
        text=texto,
        buttons=list(opcoes)
    )

    # ===========================================
    # Caso o usuário escolha uma opção,
    # salva em Text_infos.tipo_mapa se permitido
    # ===========================================
    if tipo is not None and definir_em_text_infos:
        Text_infos.tipo_mapa = tipo  # Efeito colateral intencional

    # ===========================================
    # Retorna a escolha do usuário
    # ===========================================
    return tipo  # Pode ser "Fitoecologia", "Geologia" ou None
