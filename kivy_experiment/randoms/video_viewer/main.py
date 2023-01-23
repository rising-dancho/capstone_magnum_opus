from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
import pytesseract


class MainApp(MDApp):

    def build(self):
        layout = MDBoxLayout(orientation="vertical")
        self.image = Image()
        self.label = MDLabel()
        layout.add_widget(self.image)
        layout.add_widget(self.label)
        self.save_img_button = MDRaisedButton(
            text="Click Here",
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None,None))
        self.save_img_button.bind(on_press=self.take_picture)
        layout.add_widget(self.save_img_button)
        
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0/30.0)
        return layout
    
    def load_video(self, *args):
        ret, frame = self.capture.read()
        # Frame initialize
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1],frame.shape[0]), colorfmt="bgr")
        texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")
        self.image.texture = texture
    
    def take_picture(self, *args):
        image_name = "picture_at_2_02.png"
        img_gray = cv2.cvtColor(self.image_frame, cv2.COLOR_BGR2GRAY)
        img_guassian_blur = cv2.GaussianBlur(img_gray,(3,3), 0)
        img_thresh = cv2.threshold(img_guassian_blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
        # below code sets the tesseract.exe path to your python script
        pytesseract.pytesseract.tesseract_cmd = 'C:/Users/Server_PC/AppData/Local/Tesseract-OCR/tesseract.exe' 

        text_data = pytesseract.image_to_string(img_thresh, lang="eng", config="--psm 6")
        print(text_data)
        self.label.text = text_data
        cv2.imshow("cv2 final image", img_thresh)
        cv2.imwrite(image_name, self.image_frame)

if __name__ == '__main__':
    MainApp().run()