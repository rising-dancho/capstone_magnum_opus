from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 3
        self.row_default_height = dp(54)
        self.add_widget(Button(text='Button 1'))
        self.add_widget(Button(text='Button 2'))
        self.add_widget(Button(text='Button 3'))

class MyFloatLayout(FloatLayout):
    pass

class MyApp(App):
    def build(self):
        return MyFloatLayout(
            size_hint=(1, 1),
            MyGridLayout(
                size_hint=(1, 0.2),
                pos_hint={'x': 0, 'y': 0}
            )
        )

if __name__ == '__main__':
    MyApp().run()