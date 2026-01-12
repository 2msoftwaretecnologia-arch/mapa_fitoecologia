from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

class show_alert_dinamic(App):
    def __init__(self, texto='ALERTA!\n\nMensagem importante!', **kwargs):
        super().__init__(**kwargs)
        self.texto = texto
    
    def build(self):
        # Configuração inicial da janela
        Window.clearcolor = (1, 0, 0, 1)  # Vermelho inicial
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30, size=(800, 600))
        
        # Label com mensagem de alerta
        self.label = Label(
            text=self.texto,
            font_size='24sp',
            bold=True,
            color=(1, 1, 1, 1),
            halign='center'
        )
        
        # Botão para encerrar
        self.botao = Button(
            text="ENTENDI",
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5},
            font_size='20sp',
            bold=True,
            background_color=(0.2, 0.6, 0.2, 1)
        )
        self.botao.bind(on_press=self.encerrar)
        
        # Adicionando widgets ao layout
        layout.add_widget(self.label)
        layout.add_widget(self.botao)
        
        # Iniciar o piscar da tela
        self.piscando = True
        self.cor_atual = 0  # 0 = vermelho, 1 = azul
        self.evento_piscar = Clock.schedule_interval(self.piscar_tela, 0.5)
        
        return layout
    
    def piscar_tela(self, dt):
        """Alterna entre duas cores de fundo"""
        if self.piscando:
            if self.cor_atual == 0:
                # Muda para azul
                Window.clearcolor = (0, 0, 1, 1)  # Azul
                self.cor_atual = 1
            else:
                # Muda para vermelho
                Window.clearcolor = (1, 0, 0, 1)  # Vermelho
                self.cor_atual = 0
    
    def encerrar(self, instance):
        """Para o piscar e encerra o aplicativo"""
        self.piscando = False
        Clock.unschedule(self.evento_piscar)
        App.get_running_app().stop()