import tkinter as tk
from tkinter import ttk, messagebox
import os, sys
import threading
from .build_get_city_state import GetCityStateBuild
from database.text_infos import Text_infos
        
class PropertyInfosWindowBuild:
    def __init__(self):
        self.result = {}
        self.root = tk.Tk()
        self.root.title("Initial Form")

        # Widgets
        self.entry_name = ttk.Entry(self.root, width=40)
        self.entry_owner = ttk.Entry(self.root, width=40)
        self.entry_registration = ttk.Entry(self.root, width=40)
        self.entry_city_state = ttk.Entry(self.root, width=40, state='readonly')

        # Buttons (manter nomes dos botões)
        self.btn_select_city = ttk.Button(self.root, text="Selecionar Cidade/Estado", command=self._select_city_state)
        self.btn_confirm = ttk.Button(self.root, text="Confirmar", command=self._confirm, state='disabled')

        # Layout
        self._build_ui()
        # Estado inicial do botão Confirmar
        self._update_confirm_state()

    def _build_ui(self):
        ttk.Label(self.root, text="Nome da propriedade:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        self.entry_name.bind("<KeyRelease>", self._update_confirm_state)

        ttk.Label(self.root, text="Proprietário:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_owner.grid(row=1, column=1, padx=10, pady=5)
        self.entry_owner.bind("<KeyRelease>", self._update_confirm_state)

        ttk.Label(self.root, text="Matricula:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_registration.grid(row=2, column=1, padx=10, pady=5)
        self.entry_registration.bind("<KeyRelease>", self._update_confirm_state)

        ttk.Label(self.root, text="Cidade - Estado:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_city_state.grid(row=3, column=1, padx=10, pady=5)

        self.btn_select_city.grid(row=3, column=2, padx=5, pady=5)
        self.btn_confirm.grid(row=4, column=0, columnspan=3, pady=15)

    def _valid_text(self, value: str, minimum: int = 2) -> bool:
        """Valida texto não vazio, sem ser só espaços e com tamanho mínimo."""
        if not isinstance(value, str):
            return False
        v = value.strip()
        return len(v) >= minimum

    def _all_fields_valid(self) -> bool:
        return (
            self._valid_text(self.entry_name.get()) and
            self._valid_text(self.entry_owner.get()) and
            self._valid_text(self.entry_registration.get()) and
            self._valid_text(self.entry_city_state.get())
        )

    def _update_confirm_state(self, *_args):
        # Habilita Confirmar somente quando todos campos estiverem válidos
        self.btn_confirm.config(state='normal' if self._all_fields_valid() else 'disabled')

    def _select_city_state(self):
        if self.root.winfo_exists():
            # Usa Toplevel ao invés de criar novo Tk
            top = tk.Toplevel(self.root)
            top.withdraw()  # Oculta a janela até o diálogo ser exibido
            value = GetCityStateBuild(top)
            value.grab_set()  # bloqueia interação com a janela principal até fechar
            value.wait_window()
            top.destroy()
            if value.result:
                self.entry_city_state.config(state='normal')
                self.entry_city_state.delete(0, 'end')
                self.entry_city_state.insert(0, value.result)
                self.entry_city_state.config(state='readonly')
                self.result['cidade_uf'] = value.result
                self._update_confirm_state()

    def _save_data(self):
        """Coleta e salva os dados nos resultados."""
        self.result['property_name'] = self.entry_name.get().strip()
        self.result['proprietario'] = self.entry_owner.get().strip()
        self.result['matricula'] = self.entry_registration.get().strip()
        self.result['cidade_uf'] = self.entry_city_state.get().strip()
        Text_infos.property_name = self.result['property_name']
        Text_infos.owner = self.result['proprietario']
        Text_infos.registration_property = self.result['matricula']
        Text_infos.city_uf = self.result['cidade_uf']
        print("Dados coletados:", self.result)

    def _confirm(self):
        if self.btn_confirm['state'] == 'disabled':
            return
        if not self._all_fields_valid():
            messagebox.showerror(
                title="Invalid data",
                message=(
                    "Fill in all fields correctly.\n"
                    "- Minimum of 2 characters per field\n"
                    "- Select City/State"
                ),
            )
            self._update_confirm_state()
            return

        # Preservar chaves de saída em português para compatibilidade
        self._save_data()
        self.btn_select_city.config(state='disabled')
        self.btn_confirm.config(state='disabled')
        self.root.destroy()

    def open(self) -> dict:
        self.root.mainloop()
        return self.result

    def open_async(self) -> None:
        threading.Thread(target=self.root.mainloop, daemon=True).start()
