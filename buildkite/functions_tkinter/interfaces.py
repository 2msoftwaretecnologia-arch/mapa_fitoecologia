import tkinter as tk
from tkinter import filedialog
from typing import Optional
import os

# ============================================================
# FUNÇÃO: ESCOLHER ARQUIVO SHAPEFILE
# ============================================================

def find_shp_file(title: str = "Selecione um arquivo Shapefile") -> Optional[str]:
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
    >>> caminho = find_shp_file("Escolha o arquivo de polígono")
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

class ExitCheckboxWindow:
    """
    Janela modal com checkbox de confirmação.
    O programa só prossegue (ou encerra) após o usuário marcar a checkbox.
    """

    def __init__(self) -> None:
        """Construtor: configura a janela e os widgets."""
        self._build_window()
        self._create_widgets()

    def _build_window(self) -> None:
        """Cria e configura a janela principal."""
        self.root = tk.Tk()
        self.root.title("Atenção!!!")
        self.root.geometry("300x100")
        # Garante que a janela será destruída ao fechar
        self.root.protocol("WM_DELETE_WINDOW", self._close_window)

    def _create_widgets(self) -> None:
        """Cria a checkbox e a posiciona na janela."""
        self.var = tk.IntVar()
        self.checkbox = tk.Checkbutton(
            self.root,
            text="SÓ APERTE AQUI SOMENTE\nDEPOIS QUE VOCÊ TERMINAR A TAREFA",
            variable=self.var,
            command=self._on_checked
        )
        self.checkbox.pack(expand=True, pady=20)

    def _close_window(self) -> None:
        """Encerra o loop e destrói a janela."""
        print("DEBUG: Fechando ExitCheckboxWindow...")
        self.root.quit()
        self.root.destroy()

    def _on_checked(self) -> None:
        """Fecha a janela quando a checkbox é marcada."""
        print("DEBUG: Checkbox marcado.")
        self._close_window()
        

    def show(self) -> None:
        """Exibe a janela modal (bloqueante)."""
        self.root.mainloop()


def select_folder(start_folder: str = None) -> str:
    """
    Abre uma janela para o usuário selecionar uma pasta.
    Caso o parâmetro seja um arquivo, o caminho será ajustado
    automaticamente para a pasta onde o arquivo está.

    Parâmetros:
        start_folder (str): Caminho inicial (pode ser pasta ou arquivo).    

    Retorna:
        str: Caminho completo da pasta selecionada com barra invertida no final.
    """
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter

    # Define pasta inicial padrão
    if not start_folder:
        start_folder = "C:\\"
    else:
        # Se for arquivo, converte para a pasta onde ele está
        if os.path.isfile(start_folder):
            start_folder = os.path.dirname(start_folder)

    # Abre o seletor de pastas
    caminho_pasta = filedialog.askdirectory(
        initialdir=start_folder,
        title="Selecione uma pasta"
    )

    # Se o usuário cancelar
    if not caminho_pasta:
        return ""

    # Normaliza para barras invertidas e garante barra final
    caminho_pasta = os.path.normpath(caminho_pasta) + "\\"

    return caminho_pasta