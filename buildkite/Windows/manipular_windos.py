import time
import pyperclip

# ============================================================
# 🧩 MÓDULO DE UTILIDADES GERAIS — manipular_windos.py
# ============================================================
# Este módulo contém funções auxiliares simples, utilizadas com
# frequência em automações — como limpar a área de transferência
# e aplicar pequenas pausas controladas entre ações.
# ============================================================


def limpar_area_transferencia() -> None:
    """
    ============================================================
    🧠 FUNÇÃO: limpar_area_transferencia()
    ============================================================

    📋 DESCRIÇÃO:
        Limpa o conteúdo atual da área de transferência (clipboard)
        do sistema operacional, substituindo-o por uma string vazia.

        Essa função é útil em rotinas que utilizam copiar/colar
        (via PyAutoGUI, automações de texto, etc.), garantindo que
        o buffer de dados esteja limpo antes de uma nova operação.

    ⚙️ PARÂMETROS:
        Nenhum.

    🎯 RETORNA:
        None — apenas executa a limpeza.

    💡 EXEMPLO DE USO:
        limpar_area_transferencia()
        # → "Área de transferência limpa." será exibido no console.

    ============================================================
    """
    # Substitui o conteúdo do clipboard por uma string vazia
    pyperclip.copy("")
    print("🧹 Área de transferência limpa.")


def WAIT(seconds: int) -> None:
    """
    ============================================================
    🧠 FUNÇÃO: WAIT(seconds)
    ============================================================

    📋 DESCRIÇÃO:
        Pausa a execução do programa por um número específico de
        segundos — útil para dar tempo a outras janelas, scripts
        ou processos do sistema antes da próxima ação.

        Essa função é frequentemente usada em automações com
        cliques e digitação (ex: PyAutoGUI) para evitar falhas por
        excesso de velocidade de execução.

    ⚙️ PARÂMETROS:
        segundos (int ou float):
            Quantidade de segundos que o programa deve aguardar.
            Pode ser inteiro (ex: 1) ou decimal (ex: 0.5).

    🎯 RETORNA:
        None — apenas realiza a pausa.

    💡 EXEMPLO DE USO:
        print("Iniciando em 3 segundos...")
        esperar(3)
        print("Executando agora!")

    ============================================================
    """
    # Usa o módulo 'time' para interromper a execução temporariamente
    time.sleep(seconds)
