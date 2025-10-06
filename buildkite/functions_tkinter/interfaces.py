import tkinter as tk
from tkinter import filedialog

def escolher_shp(title):
    """Abre uma janela para selecionar um arquivo SHP e retorna o caminho."""
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    
    caminho_arquivo = filedialog.askopenfilename(
        title=title,
        filetypes=[("Shapefile", "*.shp")]
    )
    
    root.destroy()  # Fecha a janela do Tkinter
    return caminho_arquivo if caminho_arquivo else None


def abrir_checkbox_saida():
    def sair():
        root.destroy()  # Fecha a janela
                  # Encerra o programa

    # Criar a janela principal
    root = tk.Tk()
    root.title("Atenção!!!")
    root.geometry("300x100")

    # Criar uma variável associada ao estado da checkbox
    var = tk.IntVar()

    # Criar a checkbox
    checkbox = tk.Checkbutton(
        root,
        text="SO APERTE AQUI DEPOIS QUE\nVOCE TERMINAR DE DIGITAR O TEXTO",
        variable=var,
        command=sair
    )
    checkbox.pack(expand=True, pady=20)  # expand centraliza melhor no eixo Y

    # Rodar a interface
    root.mainloop()