from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Clock
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
            self.rect = Rectangle(pos=(0,0), size=(15,10), width=100)
    
    def on_button_a_click(self):
        # print("test")
        x, y = self.rect.pos
        w, h = self.rect.size
        inc  =  dp(10)
     
        
        pos_of_object_in_x_axis = (x + w) # object's width with respect to the x axis
        total_distance_x = self.width # distance from position 0 to the current edge of the screen
        
        diff = total_distance_x - pos_of_object_in_x_axis  # calculating the remaining distance remaining for incrementation
        
        if diff < inc: # if the remaining distance is less the increment : stop moving
            inc = diff # assign zero

        x += inc
        self.rect.pos = (x, y)# x,y


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.velocity_x = dp(3)
        self.velocity_y = dp(3)
        with self.canvas:
            self.ball = Ellipse(pos=(self.center), size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)
    
    def on_size(self, *args):
        # print("print on size: "+ str(self.width) + ", "+ str(self.height))
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    def update(self, delta_time):
        # print("update")
        x, y = self.ball.pos
        x += self.velocity_x
        y += self.velocity_y

        if y + self.ball_size > self.height: # bounce back if ball reached top side of the screen
            y = self.height - self.ball_size
            self.velocity_y = -self.velocity_y

        if x + self.ball_size > self.width:  # bounce back if ball reached right side of the screen
            x = self.width - self.ball_size
            self.velocity_x = -self.velocity_x
        
        if x + self.ball_size > self.width:  # bounce back if ball reached right side of the screen
            self.velocity_x = -self.velocity_x
        
        if y < 0:  # bounce back if ball reached left side origin of the screen
            y = 0
            self.velocity_y = -self.velocity_y
        
        if x < 0: # bounce back if ball reached bottom side origin of the screen
            x = 0
            self.velocity_x = -self.velocity_x

        self.ball.pos = (x, y) # step +4 amount per 60 fps

    
class CanvasExample6(Widget):
    ...

class CanvasExample7(BoxLayout):
    ...