from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.metrics import dp, sp 
from kivy.utils import rgba, QueryDict
from kivy.properties import ColorProperty, ObjectProperty, BooleanProperty, \
ListProperty, StringProperty, NumericProperty

Builder.load_file('views/assetview/assetview.kv')
class AssetView (ModalView):
    currency = StringProperty("BTC")
    chart_data = ListProperty([0,1])
    asset_value = NumericProperty(42342.62)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


