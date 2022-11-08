from kivy.graphics.vertex_instructions import Line
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

Builder.load_file("canvas_examples.kv")


class CanvasExample1(Widget):
    ...

class CanvasExample2(Widget):
    ...

class CanvasExample3(Widget):
    ...

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1,0,0)
            Line(points=(100,100,400,500), width=2)
            Color(0,1,0)
            Line(circle=(400, 200, 80), width=2)
            Color(1,1,1) # white
            Line(rectangle=(250, 300, 150, 100))  # x, y, w, h
            self.rect = Rectangle(pos=(450,30), size=(150,100))
    
    def on_button_a_click(self):
        x, y = self.rect.pos
        x += dp(10)
        # y += dp(10)
        # print("test")
        self.rect.pos = (x, y)# x,y