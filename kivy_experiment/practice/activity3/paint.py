from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button

# touch.ud = is a python dictionary
# touch.ud['line'] = gave the dictionary an arbitrary "key" name 'line'

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        color = (random(), 1., 1.)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30. # size of the cirlce
            print("x",touch.x - d/2)
            print("y",touch.y - d/2)
            Ellipse(pos=(touch.x - d / 2, touch.y - d/2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text="Clear")
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    MyPaintApp().run()