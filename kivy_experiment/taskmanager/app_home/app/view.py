from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView
from kivy.garden.circulardatetimepicker import CircularTimePicker
from kivy.uix.button import Button

from kivy.properties import StringProperty, NumericProperty
from kivy.metrics import sp,dp
from kivy.utils import rgba

class NewTask(ModalView):
    def __init__(self, **kw):
        super().__init__(**kw)

    def get_time(self):
        mv = ModalView(size_hint=[.8,.8])
        box = BoxLayout(orientation = 'vertical', size_hint=[.8,.8])
        mv.add_widget(box)

        cl = CircularTimePicker()
        cl.bind(time= self.set_time)
        
        submit = Button(text="Okay", background_normal='', background_color=rgba('#282C34'), size_hint_y=.1)
        submit.bind(on_release=lambda x: self.update_time(cl.time, mv))
        box.add_widget(cl)
        # box.add_widget(Button(background_disabled='', background_color=[1,1,1,0], disabled=True))
        box.add_widget(submit)
        mv.open()

    def set_time(self, inst, value):
        print(value)
    
    def update_time(self, time, mv):
        mv.dismiss()
        self.ids.task_time.text=str(time)


class Task(ButtonBehavior, BoxLayout):
    """
        Description of Task():
        class representing a single task added by the user.

        Args:
            self (python special parameter):
            **kwargs (undefined):

        Attributes
        ----------
        name : str
            task name
        time : str
            time when the task is expected to commence.

    """
    
    name = StringProperty('')
    time = StringProperty('')
    def __init__(self, **kw):
        super().__init__(**kw)
        

class MainWindow(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def add_new(self):
        nt = NewTask()
        nt.open()
    
    def auth_user(self, username,  password):
        """
        Authenticates a user given credentials
        from inputs

        Args:
            self (python special parameter):
            username (kivy.uix.textinput.TextInput): 
                - textinput containing the username
            password kivy.uix.textinput.TextInput): 
                - textinput containing the password
        """


        uname = username.text
        upass = password.text

        self.ids.scrn_mngr.current = 'scrn_main'