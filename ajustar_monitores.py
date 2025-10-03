import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.outras_funcoes.coordenadas import *
import json
import os
import tkinter as tk
from tkinter import simpledialog, messagebox, Listbox, END
import pyautogui  # <--- IMPORTADO AQUI

ARQUIVO = "config/coordinates.json"

# ============================
# Modelo fixo de objetos (zerados)
# ============================
OBJETOS_PADRAO = [
    {"id": 1, "nome": "camada", "coordenadas": {"x": 0, "y": 0}},
    {"id": 2, "nome": "espaco_Branco", "coordenadas": {"x": 0, "y": 0}},
    {"id": 3, "nome": "retangulo", "coordenadas": {"x": 0, "y": 0}},
    {"id": 4, "nome": "desenhar_quadradro", "coordenadas": {"x": 0, "y": 0}},
    {"id": 5, "nome": "symbol_quadrado", "coordenadas": {"x": 0, "y": 0}},
    {"id": 6, "nome": "fill_color_quadrado", "coordenadas": {"x": 0, "y": 0}},
    {"id": 7, "nome": "out_line_color_quadrado", "coordenadas": {"x": 0, "y": 0}},
    {"id": 8, "nome": "grid", "coordenadas": {"x": 0, "y": 0}},
    {"id": 9, "nome": "incio", "coordenadas": {"x": 0, "y": 0}},
    {"id": 10, "nome": "escala", "coordenadas": {"x": 0, "y": 0}},
    {"id": 11, "nome": "size_position", "coordenadas": {"x": 0, "y": 0}},
    {"id": 12, "nome": "source", "coordenadas": {"x": 0, "y": 0}},
    {"id": 13, "nome": "text", "coordenadas": {"x": 0, "y": 0}},
]

# ============================
# Utilidades JSON
# ============================
def _arquivo_inicial():
    return {"resolucoes": []}

def _deepcopy_objetos_padrao():
    return json.loads(json.dumps(OBJETOS_PADRAO, ensure_ascii=False))

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(_arquivo_inicial(), f, indent=4, ensure_ascii=False)
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)
    mudou = normalizar_dados(dados)
    if mudou:
        salvar_dados(dados)
    return dados

def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def gerar_nome_unico(base, existentes):
    if base not in existentes:
        return base
    i = 2
    while f"{base}_{i}" in existentes:
        i += 1
    return f"{base}_{i}"

def normalizar_dados(dados):
    mudou = False
    if "resolucoes" not in dados or not isinstance(dados["resolucoes"], list):
        dados["resolucoes"] = []
        return True

    nomes_usados = set()
    for r in dados["resolucoes"]:
        largura = r.get("largura")
        altura = r.get("altura")

        if "nome" not in r or not r["nome"]:
            base = f"Res_{largura}x{altura}" if largura and altura else "Resolucao"
            nome_gerado = gerar_nome_unico(base, nomes_usados)
            r["nome"] = nome_gerado
            mudou = True

        if r["nome"] in nomes_usados:
            nome_corrigido = gerar_nome_unico(r["nome"], nomes_usados)
            r["nome"] = nome_corrigido
            mudou = True

        nomes_usados.add(r["nome"])

        if "objetos" not in r or not isinstance(r["objetos"], list) or len(r["objetos"]) == 0:
            r["objetos"] = _deepcopy_objetos_padrao()
            mudou = True

        for obj in r["objetos"]:
            coords = obj.get("coordenadas", {})
            x = coords.get("x", 0)
            y = coords.get("y", 0)
            try:
                x = int(x)
                y = int(y)
            except Exception:
                x, y = 0, 0
            obj["coordenadas"] = {"x": x, "y": y}

    return mudou

def adicionar_resolucao(nome, largura, altura):
    dados = carregar_dados()
    existentes = {r["nome"] for r in dados["resolucoes"]}
    nome = gerar_nome_unico(nome.strip(), existentes)
    nova = {
        "nome": nome,
        "largura": int(largura),
        "altura": int(altura),
        "objetos": _deepcopy_objetos_padrao()
    }
    dados["resolucoes"].append(nova)
    salvar_dados(dados)
    return nome

def deletar_resolucao(nome):
    dados = carregar_dados()
    antes = len(dados["resolucoes"])
    dados["resolucoes"] = [r for r in dados["resolucoes"] if r.get("nome") != nome]
    depois = len(dados["resolucoes"])
    if antes == depois:
        return False
    salvar_dados(dados)
    return True

# ============================
# Interface Tkinter
# ============================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Resoluções")

        self.lista = Listbox(root, width=50, height=12)
        self.lista.pack(pady=10)

        frame_botoes = tk.Frame(root)
        frame_botoes.pack()

        self.btn_add = tk.Button(frame_botoes, text="➕ Adicionar Resolução", command=self.add_resolucao)
        self.btn_add.grid(row=0, column=0, padx=5, pady=5)

        self.btn_del = tk.Button(frame_botoes, text="🗑️ Deletar Resolução", command=self.del_resolucao)
        self.btn_del.grid(row=0, column=1, padx=5, pady=5)

        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.delete(0, END)
        dados = carregar_dados()
        for r in dados["resolucoes"]:
            nome = r.get("nome") or f"Res_{r.get('largura','?')}x{r.get('altura','?')}"
            largura = r.get("largura", "?")
            altura = r.get("altura", "?")
            self.lista.insert(END, f"{nome} ({largura}x{altura})")

    def add_resolucao(self):
        nome = simpledialog.askstring("Nova Resolução", "Nome da resolução (ex.: FullHD, 1920x1080, etc.):")
        if not nome:
            return

        largura, altura = pyautogui.size()  # sempre automático

        nome_final = adicionar_resolucao(nome, largura, altura)
        if nome_final != nome:
            messagebox.showinfo("Atenção", f"O nome '{nome}' já existia. Criada como '{nome_final}'.")
        self.atualizar_lista()

    def del_resolucao(self):
        selecionado = self.lista.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma resolução para deletar.")
            return
        item = self.lista.get(selecionado[0])
        nome = item.split(" (")[0]
        if messagebox.askyesno("Confirmar", f"Deletar a resolução '{nome}'?"):
            ok = deletar_resolucao(nome)
            if not ok:
                messagebox.showwarning("Aviso", f"Resolução '{nome}' não encontrada (já removida?).")
            self.atualizar_lista()

