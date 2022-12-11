from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
import cv2
import numpy as np

 
class MainApp(MDApp):

    def build(self):
        layout = MDBoxLayout(orientation="vertical")
        self.image = Image(source="tommy_shelby.jpg")
        self.label = MDLabel()
        layout.add_widget(self.image)
        layout.add_widget(self.label)
        self.save_img_button = MDRaisedButton(
            text="Click Here",
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None,None))
        self.save_img_button.bind(on_press=self.take_picture)
        layout.add_widget(self.save_img_button)
        return layout
    
    def take_picture(self, *args):
        image = cv2.imread(self.image.source)
        mask = np.zeros(image.shape[:2], np.uint8)
        backgroundModel = np.zeros((1, 65), np.float64)
        foregroundModel = np.zeros((1, 65), np.float64)

        rectangle = (0,0, int(self.image.texture_size[1]), int(self.image.texture_size[0]))
        
        cv2.grabCut(image, mask, rectangle, backgroundModel, foregroundModel, 4, cv2.GC_INIT_WITH_RECT)
        finalmask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 0 , 1).astype('uint8')
        image = image * finalmask[:,:, np.newaxis]

        # Convert to transparent
        b, g, r = cv2.split(image)
        gray_layer = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(gray_layer, 0, 255, cv2.THRESH_BINARY)

        rgba = [b, g , r, alpha]
        destination = cv2.merge(rgba, 4)
        cv2.imwrite("grabcutout.jpg", destination)
        self.label.text = "Grabcut successfully"

if __name__ == '__main__':
    MainApp().run()