# SOURCE: https://www.youtube.com/watch?v=mzBxRueDfq0&list=PL3eV-nce_-TOxMiWMAgaBEX1CD3luYctv

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapView, MapMarker

class MapViewExample(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.map = self.ids.map
        self.map.add_widget(MapMarker(lat= 14.6447036, lon= 121.2665123, source="marker.png"))
    
    def return_home(self):
        self.map.center_on(14.6447036, 121.2665123)

class Main(MDApp):
    def build(self):
        Builder.load_file("layout.kv")
        return MapViewExample()

Main().run()
