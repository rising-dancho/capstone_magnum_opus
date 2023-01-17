import datetime
from kivy.lang import Builder
from kivy.app import App
from kivy_garden.xcamera import XCamera 

from kivymd.app import MDApp
from kivymd.toast import toast
import os

kv = """
#:import XCamera kivy_garden.xcamera.XCamera
FloatLayout:
    orientation: 'horizontal'

    XCamera:
        id: xcamera
        on_picture_taken: app.picture_taken(*args)
        #directory: '/MedCareCameraImg_1'

    BoxLayout:
        orientation: 'horizontal'
        #orientation: 'vertical'
        size_hint: 1, None
        height: sp(50)
        padding: 10

        Label:
            text: "\u70b9\u51fb\u76f8\u673a\u56fe\u6807\u62cd\u7167\uff0c\u70b9\u51fb\u8f83\u8272\u5c06\u8f83\u8272\u56fe\u50cf\u4fdd\u5b58"
            font_name: './static/DroidSansFallback.ttf'
            
        MDRoundFlatIconButton:
            text: " \u6807\u51c6\u989c\u8272\u6821\u6b63"
            font_name: './static/DroidSansFallback.ttf'
            icon: "format-color-fill"
            # width: dp(150)
            pos_hint: {"center_x": .5}
            on_release:app.color_cal()


"""


class CameraApp(MDApp):

    def color_cal(self):
        print("这是颜色校正的部分")

    def build(self):
        #if not os.path.exists("/MedCareCameraImg_1"):
        #   os.makedirs("/MedCareCameraImg_1")

        return Builder.load_string(kv)

    def picture_taken(self, obj, filename):
        path = "/MedCareCameraImg_1/{}".format(filename)
        toast(path)
        print('Picture taken and saved to {}'.format(filename))

if __name__ == '__main__':
    CameraApp().run()