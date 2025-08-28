from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty, ListProperty
from kivy.effects.scroll import ScrollEffect
import json
import re

class SearchableDropdown(BoxLayout):
    items = ListProperty([])
    selected_item = StringProperty('')
    placeholder = StringProperty('')
    is_open = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = dp(50)
        self.spacing = dp(2)
        self.filtered_items = []
        
        # Campo de pesquisa
        self.search_input = TextInput(
            size_hint_y=None,
            height=dp(50),
            multiline=False,
            hint_text=self.placeholder,
            background_normal='',
            background_color=(0.95, 0.95, 1, 1),
            foreground_color=(0.2, 0.2, 0.2, 1),
            font_size='16sp',
            padding=dp(15)
        )
        self.search_input.bind(text=self.on_search_text, focus=self.on_focus)
        self.add_widget(self.search_input)
        
        # Container para os itens (inicialmente invisível)
        self.dropdown_container = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=0,
            opacity=0
        )
        self.add_widget(self.dropdown_container)
        
        # ScrollView para os itens
        self.scroll_view = ScrollView(
            size_hint_y=None,
            height=0,
            effect=ScrollEffect()
        )
        self.dropdown_container.add_widget(self.scroll_view)
        
        # Grid para os itens
        self.items_layout = GridLayout(
            cols=1,
            size_hint_y=None,
            spacing=dp(2)
        )
        self.items_layout.bind(minimum_height=self.items_layout.setter('height'))
        self.scroll_view.add_widget(self.items_layout)
        
        self.bind(items=self.update_items)
    
    def on_search_text(self, instance, text):
        self.filter_items(text)
    
    def on_focus(self, instance, value):
        if value:  # Quando ganha foco
            self.open_dropdown()
        else:  # Quando perde foco
            Clock.schedule_once(lambda dt: self.close_dropdown(), 0.1)
    
    def filter_items(self, search_text):
        search_text = search_text.lower().strip()
        if not search_text:
            self.filtered_items = self.items
        else:
            self.filtered_items = [
                item for item in self.items 
                if search_text in item.lower()
            ]
        
        self.update_dropdown_items()
    
    def update_items(self, instance, items):
        self.filtered_items = items
        self.update_dropdown_items()
    
    def update_dropdown_items(self):
        self.items_layout.clear_widgets()
        
        for item in self.filtered_items:
            btn = DropdownItem(
                text=item,
                size_hint_y=None,
                height=dp(40)
            )
            btn.bind(on_release=lambda x, item=item: self.select_item(item))
            self.items_layout.add_widget(btn)
        
        # Ajustar altura do dropdown baseado no número de itens
        item_count = len(self.filtered_items)
        max_height = dp(200)  # Altura máxima
        item_height = dp(42)  # Altura por item
        new_height = min(item_count * item_height, max_height)
        
        self.items_layout.height = new_height
        self.scroll_view.height = new_height
        self.dropdown_container.height = new_height
    
    def open_dropdown(self):
        if not self.is_open and self.filtered_items:
            self.is_open = True
            self.dropdown_container.opacity = 1
            self.height = dp(50) + self.dropdown_container.height
    
    def close_dropdown(self):
        if self.is_open:
            self.is_open = False
            self.dropdown_container.opacity = 0
            self.height = dp(50)
    
    def select_item(self, item):
        self.selected_item = item
        self.search_input.text = item
        self.close_dropdown()
        self.search_input.focus = False

class DropdownItem(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.9, 0.9, 0.95, 1)
        self.color = (0.2, 0.2, 0.2, 1)
        self.font_size = '14sp'
        self.size_hint_y = None

class CitySelectorApp(App):
    result_text = StringProperty('')
    
    def build(self):
        # Configurar tamanho da janela
        Window.size = (450, 700)
        Window.minimum_width, Window.minimum_height = 400, 600
        
        # Carregar dados do JSON
        try:
            with open('estados-cidades.json', 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("Arquivo JSON não encontrado!")
            return Label(text="Arquivo JSON não encontrado!")
        except json.JSONDecodeError:
            print("Erro ao decodificar JSON!")
            return Label(text="Erro no formato do JSON!")
        
        # Parse dos dados
        self.estados_dict = self._parse_estados()
        self.all_estados = sorted(self.estados_dict.keys())
        self.all_cidades = []
        
        # Coletar todas as cidades
        for cidades in self.estados_dict.values():
            self.all_cidades.extend(cidades)
        self.all_cidades = sorted(set(self.all_cidades))
        
        # Layout principal
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Título
        title_label = Label(
            text='🔍 Seletor de Cidades do Brasil',
            size_hint_y=None,
            height=60,
            font_size='26sp',
            bold=True,
            color=(0.2, 0.4, 0.6, 1)
        )
        main_layout.add_widget(title_label)
        
        # Dropdown para estados
        estado_label = Label(
            text='Estado:',
            size_hint_y=None,
            height=30,
            font_size='16sp',
            bold=True,
            color=(0.3, 0.3, 0.3, 1)
        )
        main_layout.add_widget(estado_label)
        
        self.estado_dropdown = SearchableDropdown(
            items=self.all_estados,
            placeholder='Pesquisar estado...',
            size_hint_y=None,
            height=dp(50)
        )
        self.estado_dropdown.bind(selected_item=self.on_estado_selected)
        main_layout.add_widget(self.estado_dropdown)
        
        # Dropdown para cidades
        cidade_label = Label(
            text='Cidade:',
            size_hint_y=None,
            height=30,
            font_size='16sp',
            bold=True,
            color=(0.3, 0.3, 0.3, 1)
        )
        main_layout.add_widget(cidade_label)
        
        self.cidade_dropdown = SearchableDropdown(
            items=self.all_cidades,
            placeholder='Pesquisar cidade...',
            size_hint_y=None,
            height=dp(50)
        )
        self.cidade_dropdown.bind(selected_item=self.on_cidade_selected)
        main_layout.add_widget(self.cidade_dropdown)
        
        # Espaçador
        main_layout.add_widget(Widget(size_hint_y=1))
        
        # Botão de confirmar
        self.confirm_button = StyledButton(
            text='✅ Confirmar Seleção',
            size_hint_y=None,
            height=65,
            background_color=(0.2, 0.6, 0.3, 1),
            disabled=True
        )
        self.confirm_button.bind(on_press=self.on_confirm)
        main_layout.add_widget(self.confirm_button)
        
        # Label de resultado
        self.result_label = Label(
            text='',
            size_hint_y=None,
            height=120,
            text_size=(None, None),
            halign='center',
            valign='middle',
            color=(0.3, 0.3, 0.3, 1),
            font_size='18sp',
            markup=True
        )
        main_layout.add_widget(self.result_label)
        
        return main_layout
    
    def _parse_estados(self):
        """Analisa a estrutura do JSON e retorna dicionário de estados e cidades"""
        estados_dict = {}
        
        if isinstance(self.data, list):
            for item in self.data:
                if 'estado' in item and 'cidades' in item:
                    estados_dict[item['estado']] = item['cidades']
                elif 'nome' in item and 'cidades' in item:
                    estados_dict[item['nome']] = item['cidades']
        
        elif isinstance(self.data, dict):
            if 'estados' in self.data:
                for estado in self.data['estados']:
                    if 'nome' in estado and 'cidades' in estado:
                        estados_dict[estado['nome']] = estado['cidades']
                    elif 'estado' in estado and 'cidades' in estado:
                        estados_dict[estado['estado']] = estado['cidades']
            else:
                for estado, cidades in self.data.items():
                    if isinstance(cidades, list):
                        estados_dict[estado] = cidades
        
        return estados_dict
    
    def on_estado_selected(self, instance, estado):
        if estado:
            # Se um estado for selecionado, podemos filtrar as cidades desse estado
            if estado in self.estados_dict:
                cidades_do_estado = self.estados_dict[estado]
                self.cidade_dropdown.items = sorted(cidades_do_estado)
            self.check_selection()
    
    def on_cidade_selected(self, instance, cidade):
        self.check_selection()
    
    def check_selection(self):
        estado = self.estado_dropdown.selected_item
        cidade = self.cidade_dropdown.selected_item
        
        if estado and cidade:
            self.confirm_button.disabled = False
            # Verificar se a cidade pertence ao estado selecionado
            if estado in self.estados_dict and cidade in self.estados_dict[estado]:
                self.confirm_button.background_color = (0.2, 0.6, 0.3, 1)  # Verde
            else:
                self.confirm_button.background_color = (0.8, 0.4, 0.2, 1)  # Laranja (aviso)
        else:
            self.confirm_button.disabled = True
    
    def on_confirm(self, instance):
        estado = self.estado_dropdown.selected_item
        cidade = self.cidade_dropdown.selected_item
        
        if estado and cidade:
            resultado = f"{cidade}/{estado}"
            
            # Verificar consistência
            if estado in self.estados_dict and cidade in self.estados_dict[estado]:
                self.result_label.text = f'[b]✓ Seleção confirmada:[/b]\n[size=20]{resultado}[/size]'
                self.result_label.color = (0.2, 0.5, 0.2, 1)
            else:
                self.result_label.text = f'[b]⚠️ Atenção:[/b]\nCidade "{cidade}" não pertence a "{estado}"\n[size=20]{resultado}[/size]'
                self.result_label.color = (0.8, 0.4, 0.1, 1)
            
            self.result_text = resultado
            print(f"Seleção confirmada: {resultado}")

class StyledButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = kwargs.get('background_color', (0.2, 0.6, 0.3, 1))
        self.color = (1, 1, 1, 1)
        self.font_size = '18sp'
        self.bold = True
        
        with self.canvas.before:
            Color(*self.background_color)
            self.rect = RoundedRectangle(
                size=self.size,
                pos=self.pos,
                radius=[dp(15)]
            )
        
        self.bind(pos=self._update_rect, size=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    CitySelectorApp().run()