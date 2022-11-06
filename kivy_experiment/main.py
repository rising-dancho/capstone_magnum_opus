from kivy.app import App
from kivy.properties import ObjectProperty
from navigation_screen_manager import NavigationScreenManager
# #:import CardTransition kivy.uix.screenmanager.CardTransition
# https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html?highlight=screenmanager#module-kivy.uix.screenmanager


class MyScreenManager(NavigationScreenManager):
    ...

class TheLabApp(App):
    manager = ObjectProperty(None)
     
    def build(self):
        self.manager = MyScreenManager()
        return self.manager

TheLabApp().run()