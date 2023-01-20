from kivy.app import App

# from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty
from kivy.graphics.vertex_instructions import (Rectangle,
                                             Ellipse,
                                             Line)
from kivy.graphics.context_instructions import Color

import random

class ScatterTextWidget(BoxLayout):
    
    text_colour = ListProperty([.9, .6, .4, 1]) # setting default color

    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__(**kwargs)
        
        # with self.canvas.after:
        #     Color(.2,1,.5,1)
        #     Rectangle(pos=(0,100), size=(300,100))
        #     Ellipse(pos=(0,100), size=(300,100))
        #     Line(points=[0,0,500,600,400,300],
        #     close=True,
        #     width=3)

    def change_label_colour(self, *args):
        # colour = [random.random() for i in range(3)] + [1]
        colour1  = random.random()
        colour2  = random.random()
        colour3  = random.random()
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