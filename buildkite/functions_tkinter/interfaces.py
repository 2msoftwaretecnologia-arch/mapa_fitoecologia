import tkinter as tk
from tkinter import filedialog
from typing import Optional
import os

# ============================================================
# FUNÇÃO: ESCOLHER ARQUIVO SHAPEFILE
# ============================================================

def escolher_shp(title: str = "Selecione um arquivo Shapefile") -> Optional[str]:
    """
    Abre uma janela de diálogo para o usuário selecionar um arquivo `.shp`.

    Parameters
    ----------
    title : str, optional
        Título da janela de seleção (padrão: "Selecione um arquivo Shapefile").

    Returns
    -------
    Optional[str]
        Caminho absoluto do arquivo `.shp` selecionado.
        Retorna `None` se o usuário cancelar ou fechar a janela.

    Behavior
    --------
    1. Oculta a janela principal do Tkinter.
    2. Abre o seletor de arquivos com filtro apenas para `.shp`.
    3. Retorna o caminho do arquivo escolhido.

    Examples
    --------
    >>> caminho = escolher_shp("Escolha o arquivo de polígono")
    >>> if caminho:
    ...     print(f"Arquivo selecionado: {caminho}")
    ... else:
    ...     print("Nenhum arquivo selecionado.")
    """
    # Cria e oculta a janela principal do Tkinter
    root = tk.Tk()
    root.withdraw()

    # Abre o seletor de arquivos
    caminho_arquivo = filedialog.askopenfilename(
        title=title,
        filetypes=[("Shapefile", "*.shp")]
    )

    # Destroi a janela após seleção
    root.destroy()

    # Retorna o caminho se houver seleção
    return caminho_arquivo if caminho_arquivo else None


# ============================================================
# FUNÇÃO: ABRIR JANELA COM CHECKBOX DE CONFIRMAÇÃO
# ============================================================

def abrir_checkbox_saida() -> None:
    """
    Exibe uma janela com uma checkbox que, ao ser marcada, fecha o programa.

    Essa janela serve como uma pausa controlada em fluxos automatizados —
    o script só continua (ou encerra) após o usuário confirmar manualmente
    que terminou uma tarefa, como digitar um texto em outro software.

    Returns
    -------
    None
        A função não retorna valor; apenas bloqueia o programa até o usuário interagir.

    Behavior
    --------
    1. Cria uma janela de 300x100 pixels.
    2. Exibe uma mensagem de alerta com uma checkbox.
    3. Quando o usuário marcar a checkbox, a janela é encerrada.

    Examples
    --------
    >>> abrir_checkbox_saida()
    # Mostra a janela "Atenção!!!" com a mensagem:
    # "SÓ APERTE AQUI DEPOIS QUE VOCÊ TERMINAR A TAREFA"
    """
    def sair() -> None:
        """Fecha a janela principal ao clicar na checkbox."""
        root.destroy()

    # Criação da janela principal
    root = tk.Tk()
    root.title("Atenção!!!")
    root.geometry("300x100")

    # Variável de controle do estado da checkbox (0 = desmarcado, 1 = marcado)
    var = tk.IntVar()

    # Criação da checkbox interativa
    checkbox = tk.Checkbutton(
        root,
        text="SÓ APERTE AQUI DEPOIS QUE\nVOCÊ TERMINAR A TAREFA",
        variable=var,
        command=sair
    )

    # Centraliza a checkbox na janela
    checkbox.pack(expand=True, pady=20)

    # Inicia o loop da interface (bloqueante até fechar)
    root.mainloop()

def selecionar_pasta(pasta_inicial: str = None) -> str:
    """
    Abre uma janela para o usuário selecionar uma pasta.
    Caso o parâmetro seja um arquivo, o caminho será ajustado
    automaticamente para a pasta onde o arquivo está.

    Parâmetros:
        pasta_inicial (str): Caminho inicial (pode ser pasta ou arquivo).

    Retorna:
        str: Caminho completo da pasta selecionada com barra invertida no final.
    """
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter

    # Define pasta inicial padrão
    if not pasta_inicial:
        pasta_inicial = "C:\\"
    else:
        # Se for arquivo, converte para a pasta onde ele está
        if os.path.isfile(pasta_inicial):
            pasta_inicial = os.path.dirname(pasta_inicial)

    # Abre o seletor de pastas
    caminho_pasta = filedialog.askdirectory(
        initialdir=pasta_inicial,
        title="Selecione uma pasta"
    )

    # Se o usuário cancelar
    if not caminho_pasta:
        return ""

    # Normaliza para barras invertidas e garante barra final
    caminho_pasta = os.path.normpath(caminho_pasta) + "\\"

    return caminho_pasta