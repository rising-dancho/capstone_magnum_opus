from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
import json


class KivyApp(App):
    
    firebase_url = "https://kivycrudproject-fbca8-default-rtdb.firebaseio.com/.json"

    def build(self):
        box_layout = BoxLayout()
        box_layout.orientation = "vertical"

        # button_patch = Button(text="create patch")
        # button_patch.bind(on_press=self.create_patch)

        button_get = Button(text="get data")
        button_get.bind(on_press=self.create_get)

        button_post = Button(text="get post")
        button_post.bind(on_press=self.create_post)

        button_put = Button(text="get put")
        button_put.bind(on_press=self.create_put)

        button_delete = Button(text="get delete")
        button_delete.bind(on_press=self.create_delete)
        
        # box_layout.add_widget(button_patch)
        box_layout.add_widget(button_get)
        box_layout.add_widget(button_post)
        box_layout.add_widget(button_put)
        box_layout.add_widget(button_delete)

        return box_layout

    # def create_patch(self, *kwargs):
    #     print("BUTTON GET CLICKED")
    #     json_data = '{"url": "amazon.com", "age": "17 years old"}'
    #     response = requests.patch(url=self.firebase_url, json=json.loads(json_data))
    #     print(response) 

    def create_get(self, *kwargs):
        print("BUTTON GET CLICKED")
        response = requests.get(url=self.firebase_url)
        print(response.json())

    def create_post(self, *kwargs  ):
        print("BUTTON POST CLICKED")
        json_data = '{"Table1":{"url": "amazon.com", "age": "17 years old"}}'
        response = requests.post(url=self.firebase_url, json=json.loads(json_data))
        print(response)

    def create_put(self, *kwargs):
        print("BUTTON PUT CLICKED")
        json_data = '{"Table1":{"url": "google.com", "age": "25 years old"}}'
        response = requests.put(url=self.firebase_url, json=json.loads(json_data))
        print(response)

    def create_delete(self, *kwargs):
        print("BUTTON DELETE CLICKED")
        delete_url ="https://kivycrudproject-fbca8-default-rtdb.firebaseio.com/"
        response = requests.patch(url=delete_url+"Table1/url"+".json")
        print(response)

if __name__ == "__main__":
    KivyApp().run()

# source: https://www.youtube.com/watch?v=x72qfNCKi4s
