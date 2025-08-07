import tkinter as tk
from tkinter import ttk

def checkbox_incial():
    def verificar_checkboxes():
        if all(var.get() for var in variaveis):
            fade_out()

    def fade_out(i=5):
        if i > 0:
            janela.attributes('-alpha', i / 10)
            janela.after(50, fade_out, i - 1)
        else:
            janela.destroy()

    def fade_in(i=0):
        if i <= 10:
            janela.attributes('-alpha', i / 10)
            janela.after(30, fade_in, i + 1)

    # Configuração da janela
    janela = tk.Tk()
    janela.title("Checkbox Master")
    janela.geometry("500x600")
    janela.resizable(False, False)
    janela.configure(bg='#f0f0f0')

    # Estilo
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TCheckbutton', font=('Helvetica', 12), background='#f0f0f0', foreground='#333333', padding=10)
    style.map('TCheckbutton', background=[('active', '#e6e6e6')], foreground=[('active', '#000000')])
    style.configure('TButton', font=('Helvetica', 12, 'bold'), borderwidth=1, relief='raised', padding=10)
    style.map('TButton', background=[('active', '#45a049')], foreground=[('active', 'white')])

    main_frame = ttk.Frame(janela, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(main_frame, text="Selecione todas as opções:", font=('Helvetica', 16, 'bold'), foreground='#2e7d32').pack(pady=(0, 20))

    titulos = [
        "✓ RODOVIAS", "✓ AII", "✓ APR", 
        "✓ LIMITES MUNICIPAIS", 
        "✓ UNIDADES DA FEDERAÇÃO", 
        "✓ REGIÕES DE FITOECOLOGIA",
    ]

    variaveis = []
    for titulo in titulos:
        var = tk.BooleanVar()
        variaveis.append(var)
        ttk.Checkbutton(main_frame, text=titulo, variable=var, style='TCheckbutton', command=verificar_checkboxes).pack(anchor='w', padx=10, pady=8, fill=tk.X)

    ttk.Frame(main_frame).pack(pady=20)
    ttk.Button(main_frame, text="VERIFICAR", command=verificar_checkboxes, style='TButton').pack()

    ttk.Label(main_frame, text="Checklist dos shps", font=('Helvetica', 10), foreground='#666666').pack(side=tk.BOTTOM, pady=(20, 0))

    janela.attributes('-alpha', 0)
    fade_in()

    janela.mainloop()
