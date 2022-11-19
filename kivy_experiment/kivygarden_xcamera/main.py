from kivy.app import App
from kivy.lang import Builder


class Main(App):
    def build(self):
        return Builder.load_file("camera.kv")


Main(kv_file="camera.kv").run()