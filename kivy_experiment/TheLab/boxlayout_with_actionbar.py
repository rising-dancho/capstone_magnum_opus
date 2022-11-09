from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

Builder.load_file("boxlayout_with_actionbar.kv")

class BoxLayoutWithActionBar(BoxLayout):
    title = StringProperty()