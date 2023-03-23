
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_string("""
<BlankTextField>:
    background_normal: ""
    background_active: ""
    background_color: [0,0,0,0]
    foreground_color: app.colors.primary
    padding: [dp(6), (self.height - self.line_height)/2]
""")

class BlankTextField(TextInput):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)