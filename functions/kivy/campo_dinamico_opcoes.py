from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window

class SelectionDialog(BoxLayout):
    def __init__(self, options_list, multi_select=False, title="Seleção", **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, size=(800, 600), **kwargs)
        
        self.options_list = options_list
        self.multi_select = multi_select
        self.result = None
        self.selected_options = set()
        
        title_label = Label(
            text=f"{title}\n{'Selecione uma ou mais opções:' if multi_select else 'Selecione uma opção:'}",
            size_hint_y=None,
            height=60,
            halign='center'
        )
        self.add_widget(title_label)
        
        scroll = ScrollView(size_hint=(1, 0.8))
        
        if multi_select:
            options_layout = GridLayout(cols=1, size_hint_y=None, spacing=5)
            options_layout.bind(minimum_height=options_layout.setter('height'))
            
            for option in options_list:
                row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                
                checkbox = CheckBox(size_hint_x=None, width=40)
                checkbox.option = option
                checkbox.bind(active=self.on_checkbox_active)
                
                label = Label(text=option, size_hint_x=1, halign='left')
                
                row.add_widget(checkbox)
                row.add_widget(label)
                options_layout.add_widget(row)
        else:
            options_layout = GridLayout(cols=1, size_hint_y=None, spacing=5)
            options_layout.bind(minimum_height=options_layout.setter('height'))
            
            for option in options_list:
                btn = ToggleButton(
                    text=option,
                    size_hint_y=None,
                    height=40,
                    group='single_select'
                )
                btn.option = option
                btn.bind(state=self.on_toggle_state)
                options_layout.add_widget(btn)
        
        scroll.add_widget(options_layout)
        self.add_widget(scroll)
        
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        self.confirm_btn = Button(text='Confirmar', background_color=(0, 0.7, 0, 1))
        self.cancel_btn = Button(text='Cancelar', background_color=(0.8, 0, 0, 1))
        
        button_layout.add_widget(self.cancel_btn)
        button_layout.add_widget(self.confirm_btn)
        self.add_widget(button_layout)
    
    def on_checkbox_active(self, checkbox, value):
        if value:
            self.selected_options.add(checkbox.option)
        else:
            self.selected_options.discard(checkbox.option)
    
    def on_toggle_state(self, toggle, state):
        if state == 'down':
            if not self.multi_select:
                self.selected_options.clear()
            self.selected_options.add(toggle.option)
        elif not self.multi_select:
            self.selected_options.discard(toggle.option)

class SelectionApp(App):
    def __init__(self, options_list, multi_select=False, title="Seleção", **kwargs):
        super().__init__(**kwargs)
        self.options_list = options_list
        self.multi_select = multi_select
        self.title = title
        self.result = None
    
    def build(self):
        Window.size = (800, 600)
        self.root = SelectionDialog(self.options_list, self.multi_select, self.title)
        self.root.confirm_btn.bind(on_press=self.confirm)
        self.root.cancel_btn.bind(on_press=self.cancel)
        return self.root
    
    def confirm(self, instance):
        self.result = list(self.root.selected_options)
        self.stop()
    
    def cancel(self, instance):
        self.result = None
        self.stop()

def selecionar_resposta(options_list, multi_select=False, title="Seleção"):
    """
    Função para exibir a interface de seleção e retornar o resultado
    """
    app = SelectionApp(options_list, multi_select, title)
    app.run()
    return app.result

teste = selecionar_resposta(title="Selecione uma ou mais opções", options_list=["Opção 1", "Opção 2", "Opção 3"], multi_select=True)
