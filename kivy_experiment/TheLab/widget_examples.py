from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

Builder.load_file("widget_examples.kv")


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
    
    def on_text_validate(self, widget):
        self.text_input_str = widget.text
    
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
    
class ScrollViewExample(ScrollView):
    ...