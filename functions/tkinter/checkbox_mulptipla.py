import tkinter as tk
from tkinter import messagebox

class CheckboxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seletor de Opções")
        
        # Opções disponíveis
        self.options = [
            "Floresta Estacional",
            "Floresta Ombrófila Aberta",
            "Floresta Ombrófila Densa",
            "Savana Gramíneo Lenhosa",
            "Savana Arborizada/Arbórea",
            "Savana Florestada",
            "Savana Parque",
            "Rio"
        ]
        
        # Variáveis para os checkboxes
        self.check_vars = []
        # Contador de seleções
        self.selected_count = 0
        
        # Frame principal
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack()
        
        # Label de instrução
        tk.Label(self.main_frame, text="Quais as fitoecologias predominantes? (Máximo 4):", 
                font=('Arial', 12)).pack(anchor='w', pady=(0, 10))
        
        # Criar checkboxes
        for option in self.options:
            var = tk.IntVar()
            self.check_vars.append((option, var))
            cb = tk.Checkbutton(self.main_frame, text=option, variable=var,
                              command=lambda v=var: self.update_selection(v))
            cb.pack(anchor='w', padx=5)
        
        # Botão de submeter
        self.submit_btn = tk.Button(self.main_frame, text="Confirmar", 
                                   command=self.get_selected_options)
        self.submit_btn.pack(pady=(15, 0))
        
        # Variável para armazenar as opções selecionadas
        self.selected_options = []
    
    def update_selection(self, var):
        """Atualiza o contador de seleções e desabilita checkboxes se necessário"""
        if var.get() == 1:  # Se estiver marcando
            self.selected_count += 1
            if self.selected_count >= 4:
                for option, v in self.check_vars:
                    if v.get() == 0:  # Desabilita apenas os não selecionados
                        for widget in self.main_frame.winfo_children():
                            if isinstance(widget, tk.Checkbutton) and widget.cget("text") == option:
                                widget.config(state=tk.DISABLED)
        else:  # Se estiver desmarcando
            self.selected_count -= 1
            # Reabilita todos os checkboxes se tiver menos de 4 selecionados
            if self.selected_count < 4:
                for widget in self.main_frame.winfo_children():
                    if isinstance(widget, tk.Checkbutton):
                        widget.config(state=tk.NORMAL)
    
    def get_selected_options(self):
        """Obtém as opções selecionadas e fecha a janela"""
        selected = [option for option, var in self.check_vars if var.get() == 1]
        
        if not selected:
            messagebox.showwarning("Atenção", "Selecione pelo menos uma opção!")
            return
        
        self.selected_options = selected
        self.root.destroy()

def get_user_selections():
    """Cria e executa a aplicação, retornando as seleções do usuário"""
    root = tk.Tk()
    app = CheckboxApp(root)
    root.mainloop()
    return app.selected_options

