from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView

from kivy.properties import StringProperty, NumericProperty
from kivy.metrics import sp,dp
from kivy.utils import rgba

class NewTask(ModalView):
    def __init__(self, **kw):
        super().__init__(**kw)


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