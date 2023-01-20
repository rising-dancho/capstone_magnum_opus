from kivy.app import App

# from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

import random

class ScatterTextWidget(BoxLayout):
    def change_label_colour(self, *args):
        # colour = [random.random() for i in range(3)] + [1]
        colour1  = random.random()
        colour2  = random.random()
        colour3  = random.random()
        # colour4  = random.random()
        colour4  = 1
        colour = [colour1, colour2, colour3, colour4]

        print(colour)
        label = self.ids.my_label
        label.color = colour


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()