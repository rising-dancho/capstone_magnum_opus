
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict


Builder.load_file('views/overview/overview.kv')
class Overview(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
    