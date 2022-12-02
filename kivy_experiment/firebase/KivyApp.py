from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
import json


class KivyApp(App):
    
    firebase_url = "https://kivycrudproject-fbca8-default-rtdb.firebaseio.com/.json"

    def build(self):
        box_layout = BoxLayout()
        button = Button(text="Create patch")
        button.bind(on_press=self.create_patch)
        box_layout.add_widget(button)
        return box_layout

    def create_patch(self, *kwargs):
        print("BUTTON CLICKED")
        json_data = '{"url": "google.com", "age": "15 years old"}'
        response = requests.patch(url=self.firebase_url, json=json.loads(json_data))
        print(response)
if __name__ == "__main__":
    KivyApp().run()

# source: https://www.youtube.com/watch?v=x72qfNCKi4s
