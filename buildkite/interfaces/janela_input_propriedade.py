import tkinter as tk
from tkinter import ttk, messagebox
from buildkite.interfaces.input_de_cidade import *

def abrir_janela_input_propriedade():
    resultado = {}

    def texto_valido(valor: str, minimo: int = 2) -> bool:
        """Valida texto não vazio, sem ser só espaços e com tamanho mínimo."""
        if not isinstance(valor, str):
            return False
        v = valor.strip()
        return len(v) >= minimo

    def todos_campos_validos() -> bool:
        return (
            texto_valido(entry_nome.get()) and
            texto_valido(entry_proprietario.get()) and
            texto_valido(entry_matricula.get()) and
            texto_valido(entry_cidade.get())
        )

    def atualizar_estado_confirmar(*_args):
        # Habilita Confirmar somente quando todos campos estiverem válidos
        btn_confirmar.config(state='normal' if todos_campos_validos() else 'disabled')

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
                atualizar_estado_confirmar()

    def confirmar():
        if btn_confirmar['state'] == 'disabled':
            return
        if not todos_campos_validos():
            messagebox.showerror(
                title="Dados inválidos",
                message=(
                    "Preencha todos os campos corretamente.\n"
                    "- Mínimo de 2 caracteres por campo\n"
                    "- Selecione Cidade/Estado"
                ),
            )
            atualizar_estado_confirmar()
            return

        resultado['nome_propriedade'] = entry_nome.get().strip()
        resultado['proprietario'] = entry_proprietario.get().strip()
        resultado['matricula'] = entry_matricula.get().strip()
        resultado['cidade_uf'] = entry_cidade.get().strip()
        print("Dados coletados:", resultado)
        btn_selecionar_cidade.config(state='disabled')
        btn_confirmar.config(state='disabled')
        root.destroy()

    root = tk.Tk()
    root.title("Formulário Inicial")

    ttk.Label(root, text="Nome da propriedade:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nome = ttk.Entry(root, width=40)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)
    entry_nome.bind("<KeyRelease>", atualizar_estado_confirmar)

    ttk.Label(root, text="Proprietário:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_proprietario = ttk.Entry(root, width=40)
    entry_proprietario.grid(row=1, column=1, padx=10, pady=5)
    entry_proprietario.bind("<KeyRelease>", atualizar_estado_confirmar)

    ttk.Label(root, text="Matrícula:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_matricula = ttk.Entry(root, width=40)
    entry_matricula.grid(row=2, column=1, padx=10, pady=5)
    entry_matricula.bind("<KeyRelease>", atualizar_estado_confirmar)

    ttk.Label(root, text="Cidade - Estado:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_cidade = ttk.Entry(root, width=40, state='readonly')
    entry_cidade.grid(row=3, column=1, padx=10, pady=5)

    btn_selecionar_cidade = ttk.Button(root, text="Selecionar Cidade/Estado", command=selecionar_cidade_estado)
    btn_selecionar_cidade.grid(row=3, column=2, padx=5, pady=5)

    btn_confirmar = ttk.Button(root, text="Confirmar", command=confirmar, state='disabled')
    btn_confirmar.grid(row=4, column=0, columnspan=3, pady=15)

    # Estado inicial do botão Confirmar
    atualizar_estado_confirmar()
    
    root.mainloop()
    return resultado


if __name__ == "__main__":
    # Teste rápido da janela de formulário isoladamente
    dados = abrir_janela_input_propriedade()
    print("Resultado do formulário:", dados)