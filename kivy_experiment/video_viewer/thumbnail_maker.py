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
            text="Remove Background",
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
        cv2.imwrite("grabcutout.png", destination)
        self.label.text = "Grabcut successfully!!"
        self.create_final_image()

    def create_final_image(self):
        bg_image = cv2.imread("bg.jpg")
        overlay_img = cv2.imread("grabcutout.png")
        overlay_img = cv2.resize(overlay_img,(800,533))

        gray_overlay = cv2.cvtColor(overlay_img, cv2.COLOR_BGR2GRAY)
        overlay_mask = cv2.threshold(gray_overlay, 1, 255, cv2.THRESH_BINARY)[1]

        background_mask = 255 - overlay_mask
        overlay_mask =cv2.cvtColor(overlay_mask, cv2.COLOR_GRAY2BGR)
        background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)

        bg_image_part = (bg_image * (1/255.0)) * (background_mask * (1/255.0))
        bg_overlay_part = (overlay_img * (1/255.0)) * (overlay_mask * (1/255.0))

        final_image = cv2.addWeighted(bg_image_part, 255.0, bg_overlay_part, 255.0, 0.0)
        cv2.putText(final_image,"Tommy Shelby", (50,50), cv2.FONT_HERSHEY_DUPLEX,2,(0,0,0), 2, cv2.LINE_AA)
        cv2.imwrite("finalout.png", final_image)
        self.label.text= "final thumbnail is successful!"



if __name__ == '__main__':
    MainApp().run()