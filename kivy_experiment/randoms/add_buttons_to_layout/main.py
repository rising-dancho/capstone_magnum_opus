from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.button import Button

from kivy.properties import NumericProperty

Builder.load_string("""
<Start>:
    BoxLayout:
        size_hint_y: 0.2
        pos_hint: {'y': 0.8}
        Button:
            text: 'Add'
            on_press: root.add_buttons()
        Button:
            text: 'Remove'
            on_press: root.remove_buttons()
    
    BoxLayout:
        orientation: 'vertical'
        id: grid_id
        # cols: 5
        size_hint_y: .8
        pos_hint: {'y':0}
""")

class Start(Screen):
    name = NumericProperty(0)

    def add_buttons(self):
        self.name += 1
        new_btn = Button(text=str(self.name))
        self.ids.grid_id.add_widget(new_btn)
    
    def remove_buttons(self):
        try:
            self.ids.grid_id.remove_widget(self.ids.grid_id.children[0])
        except:
            print("no buttons to remove")


class MainApp(App):
    def build(self):
        return Start()
    
MainApp().run()