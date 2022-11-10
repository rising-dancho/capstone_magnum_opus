from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from models import Pizza

class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()


class MainWidget(BoxLayout):
    from_main_recycle_view = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 Cheeses","mozerella, emmental, brie, blue cheese", 9.5, True),
            Pizza("Chorizo","tomato, chorizo, cheese", 11.2, False),
            Pizza("Calzone","cheese, ham, mushrooms",10, False)
        ]
    def on_parent(self, widget, parent):    
        self.from_main_recycle_view.data = [tae.get_dictionary() for tae in self.pizzas]
        print(self.from_main_recycle_view.data)
        # [
        #     {"name": "4 Cheeses"},
        #     {"name": "Chorizo"}
        # ]


class PizzaApp(App):
    ...

PizzaApp().run()