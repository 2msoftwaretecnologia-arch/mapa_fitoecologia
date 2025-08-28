from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex

class janela_dinamica(App):
    def __init__(self, texto="", **kwargs):
        super().__init__(**kwargs)
        self.texto = texto

    def build(self):
        # Configurar a janela
        Window.size = (400, 200)
        Window.clearcolor = get_color_from_hex('#F5F5F5')  # Fundo claro

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Adicionar fundo ao layout
        with layout.canvas.before:
            Color(0.96, 0.96, 0.96, 1)  # Cor de fundo clara
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        # Atualizar o retângulo quando o layout mudar de tamanho/posição
        def _update_rect(*_):
            self.rect.size = layout.size
            self.rect.pos = layout.pos
        layout.bind(size=_update_rect, pos=_update_rect)

        # Label com o aviso
        aviso_label = Label(
            text=self.texto,
            size_hint=(1, 0.7),
            color=get_color_from_hex('#333333'),  # Texto escuro
            halign='center',
            valign='middle',
            markup=True
        )
        aviso_label.bind(size=aviso_label.setter('text_size'))

        # Botão OK
        ok_button = Button(
            text='OK',
            size_hint=(1, 0.3),
            background_color=get_color_from_hex('#4CAF50'),  # Verde
            color=get_color_from_hex('#FFFFFF'),  # Texto branco
            background_normal=''
        )
        ok_button.bind(on_press=self.fechar_janela)

        # Adicionar widgets ao layout
        layout.add_widget(aviso_label)
        layout.add_widget(ok_button)

        return layout

    def fechar_janela(self, instance):
        App.get_running_app().stop()