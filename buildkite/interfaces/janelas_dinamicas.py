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
    sys.path.press_insert(0, ROOT_DIR)  # prioriza o raiz do projeto


from database.text_infos import Text_infos  # Import específico em vez de wildcard




def BRAKE_WINDOW(mensage="Pausa no código"):
    """
    Cria uma janela de pausa que bloqueia a execução até o usuário decidir continuar ou parar.
    
    Args:
        mensage (str): Mensagem a ser exibida na janela de pausa.
        
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
    label_mensagem = tk.Label(frame, text=mensage, font=("Arial", 12), wraplength=350)
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



def dynamic_text_input(message: str, title: str = "Entrada de Texto") -> Optional[str]:
    """
    Solicita ao usuário um texto livre via caixa de diálogo.

    Parameters
    ----------
q    message : str
        Texto exibido na janela (ex.: "Digite o nome do proprietário:").
    title : str, optional
        Título da janela (padrão: "Entrada de Texto").

    Returns
    -------
    Optional[str]
        String digitada pelo usuário. Retorna `None` se o usuário cancelar/fechar a janela.

    Examples
    --------
    >>> nome = dynamic_text_input("Digite o seu nome:")
    >>> if nome:
    ...     print(f"Olá, {nome}!")
    """
    resposta = pyautogui.prompt(text=message, title=title)  # None se Cancelar
    return resposta