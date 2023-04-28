import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # initialize infinite keywords
    def __init__(self, **kwargs):
        # call the grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        
        # set columns
        self.cols = 1

        # add widgets
        self.add_widget(Label(text="Name: "))
        # add input box
        self.name  = TextInput(multiline=False)
        self.add_widget(self.name)

        # add widgets
        self.add_widget(Label(text="Favorite Pizza : "))
        # add input box
        self.pizza  = TextInput(multiline=False)
        self.add_widget(self.pizza)

        # create submit button
        self.submit = Button(text="Submit", font_size=28)
        
        # bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        
        # print(f"Hello {name}, you are a fan of {pizza}")
        self.add_widget(Label(text=f'Hello {name}, you are a fan of {pizza}'))

        # clear the boxes
        self.name.text = ""
        self.pizza.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == "__main__":
    MyApp().run()