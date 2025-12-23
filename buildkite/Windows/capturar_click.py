import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ============================================================
# 🔧 IMPORTAÇÕES INTERNAS
# ============================================================
# 'manipular_windos' → funções auxiliares para pausas, janelas, etc.
# 'janelas_dinamicas' → exibe caixas de diálogo interativas (alertas Tkinter)
from buildkite.Windows.manipular_windos import WAIT
from buildkite.interfaces.janelas_dinamicas import BrakeWindow

# ============================================================
# 📦 IMPORTAÇÕES EXTERNAS
# ============================================================
# 'pynput.mouse' → usado para capturar cliques do mouse fora da janela Tkinter
# 'threading' → usado para sincronizar o evento de clique
from pynput import mouse
import threading


def capturar_clique(texto: str) -> tuple[int, int]:
    """
    ============================================================
    🧠 FUNÇÃO: capturar_clique(texto)
    ============================================================

    📋 DESCRIÇÃO:
        Exibe uma janela de aviso solicitando que o usuário clique
        em algum ponto da tela (fora da aplicação), e captura as
        coordenadas (x, y) exatas do clique do mouse.

        Essa função é extremamente útil em automações gráficas com
        PyAutoGUI, ArcGIS, QGIS ou outras interfaces onde é preciso
        registrar posições exatas na tela para posterior automação.

        O processo é feito de forma **bloqueante**:
        - Primeiro, mostra uma janela explicando o que o usuário deve fazer.
        - Depois, aguarda até que o usuário clique em qualquer lugar.
        - Ao detectar o clique, registra as coordenadas e retorna.

    ⚙️ PARÂMETROS:
        texto (str):
            Mensagem que será exibida na janela de aviso.
            Exemplo: "Clique sobre o ponto de referência no mapa."

    🎯 RETORNA:
        tuple[int, int]:
            Uma tupla contendo as coordenadas do clique (x, y) na tela.

            Exemplo:
            (1250, 620)

    💡 EXEMPLO DE USO:
        x, y = capturar_clique("Clique no local onde deseja posicionar o texto")
        print(f"Coordenadas capturadas: X={x}, Y={y}")
    ============================================================
    """

    # ============================================================
    # 🪟 MOSTRA UMA JANELA INFORMATIVA
    # ============================================================
    # A função 'BRAKE_WINDOW' exibe uma caixa de diálogo
    # (janela Tkinter) informando o que o usuário deve fazer.
    BrakeWindow(texto).show()

    # ============================================================
    # 🎯 VARIÁVEIS INTERNAS
    # ============================================================
    coordenadas = {}            # Dicionário que armazenará X e Y
    done = threading.Event()    # Evento que sinaliza quando o clique ocorrer

    # ============================================================
    # 🖱️ FUNÇÃO INTERNA DE CALLBACK
    # ============================================================
    # Esta função é chamada automaticamente pelo Listener do mouse
    # toda vez que o usuário pressiona ou solta um botão.
    def on_click(x, y, pressed):
        if pressed:
            coordenadas['x'] = x
            coordenadas['y'] = y
            done.set()  # Sinaliza que já capturou o clique
            return False  # Para o listener (não continua ouvindo)

    # ============================================================
    # 🎧 INICIALIZA O LISTENER DO MOUSE
    # ============================================================
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    # Aguarda o evento de clique sem travar a interface gráfica
    done.wait()

    # Para o listener após capturar as coordenadas
    listener.stop()

    # Pequena pausa para garantir que o listener finalize corretamente
    WAIT(0.5)

    # ============================================================
    # 📤 RETORNA AS COORDENADAS CAPTURADAS
    # ============================================================
    return coordenadas['x'], coordenadas['y']
