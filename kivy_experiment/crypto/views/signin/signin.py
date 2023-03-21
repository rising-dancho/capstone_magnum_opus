from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

Builder.load_file('views/signin/signin.kv')
class Signin(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

        

        
