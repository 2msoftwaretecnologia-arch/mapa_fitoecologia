import tkinter as tk
from tkinter import ttk
from buildkite.interfaces.input_de_cidade import *

def abrir_janela_input_propriedade():
    resultado = {}

    def selecionar_cidade_estado():
        if root.winfo_exists():
            valor = selecionar_estado_cidade()
            print("Valor selecionado:", valor)
            if valor:
                # Alterna para 'normal' para permitir atualização visual e volta para 'readonly'
                entry_cidade.config(state='normal')
                entry_cidade.delete(0, 'end')
                entry_cidade.insert(0, valor)
                entry_cidade.config(state='readonly')
                resultado['cidade_uf'] = valor  # <-- Atualiza o dicionário imediatamente
                btn_confirmar.config(state='normal')

    def confirmar():
        resultado['nome_propriedade'] = entry_nome.get()
        resultado['proprietario'] = entry_proprietario.get()
        resultado['matricula'] = entry_matricula.get()
        resultado['cidade_uf'] = entry_cidade.get()
        print("Dados coletados:", resultado)
        btn_selecionar_cidade.config(state='disabled')
        btn_confirmar.config(state='disabled')
        root.destroy()

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
    entry_cidade = ttk.Entry(root, width=40, state='readonly')
    entry_cidade.grid(row=3, column=1, padx=10, pady=5)

    btn_selecionar_cidade = ttk.Button(root, text="Selecionar Cidade/Estado", command=selecionar_cidade_estado)
    btn_selecionar_cidade.grid(row=3, column=2, padx=5, pady=5)

    btn_confirmar = ttk.Button(root, text="Confirmar", command=confirmar, state='disabled')
    btn_confirmar.grid(row=4, column=0, columnspan=3, pady=15)
    
    root.mainloop()
    return resultado


if __name__ == "__main__":
    # Teste rápido da janela de formulário isoladamente
    dados = abrir_janela_input_propriedade()
    print("Resultado do formulário:", dados)