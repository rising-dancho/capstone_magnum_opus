from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty('1')
    text_input_str = StringProperty('text')
    # silder_text_value = StringProperty("20")
    switch_enabled = BooleanProperty(False)

    def on_button_click(self):   
        if self.count_enabled:
            self.count+=1
            self.my_text = str(self.count)
        
    def on_toggle_button_state(self, widget):
        print("toggle state: ", widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True
    
    # def on_switch_active(self, widget):
    #     print("active state: ", str(widget.active))
    #     if widget.active == False:
    #         # "OFF"
    #         self.switch_enabled = False
    #     else:
    #         # "ON"
    #         self.switch_enabled = True
    
    # def on_slider_value(self, widget):
    #     self.silder_text_value = str(int(widget.value))
        # print("slider value: ",str(int(widget.value)))
    
    def on_text_validate(self, widget):
        self.text_input_str = widget.text

        
        

# class ScrollViewExample(ScrollView):
#     ...


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0,100):
            # size = dp(100) +  i*10
            size = dp(100)
            b = Button(text=str(i+1),size_hint=(None,None), size=(dp(size), dp(size)))
            self.add_widget(b)

# class GridLayouttExample(GridLayout):
#     ...

class AnchorLayoutExample(AnchorLayout):
    ...
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class BoxLayoutExample(BoxLayout):
    ...

class MainWidget(Widget):
    ...

class TheLabApp(App):
    ...

TheLabApp().run()