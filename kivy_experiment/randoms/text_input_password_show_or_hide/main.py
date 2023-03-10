from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MainWidget(Widget):

    textinput = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def togglevisibility(self):
        if self.ti_password.password == True:
            self.ti_password.password = False
            self.ids.btn_toggle.text = "Show"
        else:
            self.ti_password.password = True
            self.ids.btn_toggle.text = "Hide"
    

class PasswordToggleApp(App):
    ...

PasswordToggleApp().run()