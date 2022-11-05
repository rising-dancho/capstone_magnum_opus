from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

from kivy.uix.widget import Widget
from kivy.uix.button import Button

Builder.load_file("layout_examples.kv")

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0,100):
            # size = dp(100) +  i*10
            size = dp(100)
            b = Button(text=str(i+1),size_hint=(None,None), size=(dp(size), dp(size)))
            self.add_widget(b)

class GridLayouttExample(GridLayout):
    ...

class AnchorLayoutExample(AnchorLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

class BoxLayoutExample(BoxLayout):
    ...

class MainWidget(Widget):
    ...