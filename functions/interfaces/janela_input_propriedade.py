import tkinter as tk
from tkinter import ttk

def abrir_janela_input_propriedade():
    resultado = {}

    def confirmar():
        resultado['nome_propriedade'] = entry_nome.get()
        resultado['proprietario'] = entry_proprietario.get()
        resultado['matricula'] = entry_matricula.get()
        resultado['cidade_uf'] = entry_cidade.get()
        root.quit()

    root = tk.Tk()
    root.title("Formulário Inicial")

    ttk.Label(root, text="Nome da propriedade:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nome = ttk.Entry(root, width=40)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(root, text="Proprietário:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_proprietario = ttk.Entry(root, width=40)
    entry_proprietario.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(root, text="Matrícula:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_matricula = ttk.Entry(root, width=40)
    entry_matricula.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(root, text="Cidade - Estado:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_cidade = ttk.Entry(root, width=40)
    entry_cidade.grid(row=3, column=1, padx=10, pady=5)

    btn_confirmar = ttk.Button(root, text="Confirmar", command=confirmar)
    btn_confirmar.grid(row=4, column=0, columnspan=2, pady=15)

    root.mainloop()
    root.destroy()
    return resultado