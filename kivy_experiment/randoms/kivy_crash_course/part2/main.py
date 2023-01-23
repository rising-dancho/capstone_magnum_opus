from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_string('''
<ScrollableLabel>:
    text: str("some really long string" *100)
    Label:
        text: root.text
        front_size: 50
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
        
''')


class ScrollableLabel(ScrollView):
    text= StringProperty("")

runTouchApp(ScrollableLabel())

