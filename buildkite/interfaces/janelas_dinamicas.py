from typing import Optional, Sequence, Literal
import pyautogui
import os
import sys
import tkinter as tk
import threading


# === Corrigir o caminho para o RAIZ do projeto (map_fitoecologia) ===
CURRENT_DIR = os.path.dirname(__file__)                                  # ...\buildkite\interfaces
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..'))        # ...\map_fitoecologia
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)  # prioriza o raiz do projeto


from database.text_infos import Text_infos  # Import específico em vez de wildcard


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



def janela_pausa(mensagem="Pausa no código"):
    """
    Cria uma janela de pausa que bloqueia a execução até o usuário decidir continuar ou parar.
    
    Args:
        mensagem (str): Mensagem a ser exibida na janela
        
    Returns:
        bool: True se continuar, False se parar
    """
    resultado = {"continuar": None}
    
    def continuar():
        resultado["continuar"] = True
        janela.quit()
        janela.destroy()
    
    def parar():
        resultado["continuar"] = False
        janela.quit()
        janela.destroy()
        sys.exit()
    
    # Criar a janela de pausa
    janela = tk.Tk()
    janela.title("Pausa Dinâmica")
    janela.geometry("400x200")
    janela.resizable(False, False)
    
    # Configurar o protocolo de fechamento para parar o código
    janela.protocol("WM_DELETE_WINDOW", parar)
    
    # Frame principal
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Mensagem
    label_mensagem = tk.Label(frame, text=mensagem, font=("Arial", 12), wraplength=350)
    label_mensagem.pack(pady=20)
    
    # Frame dos botões
    frame_botoes = tk.Frame(frame)
    frame_botoes.pack(pady=20)
    
    # Botão continuar
    botao_continuar = tk.Button(frame_botoes, text="Continuar", command=continuar, 
                               bg="green", fg="white", font=("Arial", 10, "bold"))
    botao_continuar.pack()
    
    # Centralizar a janela na tela
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (janela.winfo_width() // 2)
    y = (janela.winfo_screenheight() // 2) - (janela.winfo_height() // 2)
    janela.geometry(f"+{x}+{y}")
    
    # Executar a janela (bloqueia até ser fechada)
    janela.mainloop()
    
    return resultado["continuar"]



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
    opcoes: Sequence[str] = ("Fitoecologia", "Geologia","Pedologia","Regioes_climaticas","Declividade","Erodibilidade"),
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
    TipoMapa = Literal["Fitoecologia", "Geologia","Pedologia","Regioes_climaticas"]

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
