from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

Window.size = (400, 200)

class TextInputApp(App):
    def __init__(self, texto="aperte ok para continuar", **kwargs):
        super().__init__(**kwargs)
        self.texto = texto
        self.user_response = ""

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.label = Label(text=self.texto, size_hint=(1, 0.2), font_size=16)

        self.text_input = TextInput(
            multiline=False,
            size_hint=(1, 0.3),
            font_size=16,
            hint_text="Digite aqui...",
            padding=[10, 10]
        )
        self.text_input.bind(on_text_validate=self.on_enter)

        self.button = Button(
            text="Enviar",
            size_hint=(1, 0.2),
            font_size=16,
            background_normal='',
            background_color=(0.2, 0.6, 0.8, 1),
        )
        self.button.bind(on_press=self.get_user_input)

        layout.add_widget(self.label)
        layout.add_widget(self.text_input)
        layout.add_widget(self.button)

        # foca no campo ao abrir
        Clock.schedule_once(lambda *_: setattr(self.text_input, 'focus', True), 0)

        return layout

    def get_user_input(self, instance):
        self.user_response = self.text_input.text
        self.stop()

    def on_enter(self, instance):
        self.get_user_input(instance)

def input_texto_dinamico(texto="aperte ok para continuar"):
    app = TextInputApp(texto)
    app.run()
    return app.user_response