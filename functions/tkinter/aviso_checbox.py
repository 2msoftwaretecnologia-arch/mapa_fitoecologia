import tkinter as tk


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