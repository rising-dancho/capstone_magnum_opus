from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView
from kivy.garden.circulardatetimepicker import CircularTimePicker
from kivy.uix.button import Button

from kivy.properties import StringProperty, NumericProperty
from kivy.metrics import sp,dp
from kivy.utils import rgba
from app.storage.db import Database

class NewTask(ModalView):
    def __init__(self, **kw):
        super().__init__(**kw)

    def get_time(self):
        mv = ModalView(size_hint=[.8,.8])
        box = BoxLayout(orientation = 'vertical', size_hint=[.8,.8])
        mv.add_widget(box)

        cl = CircularTimePicker()
        cl.bind(time= self.set_time)
        
        submit = Button(text="OK", background_normal='', background_color=rgba('#282C34'), size_hint_y=.1)
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

class NewButton(ButtonBehavior, BoxLayout):
    ...

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
    date = StringProperty('')
    def __init__(self, **kw):
        super().__init__(**kw)

class Today(Task):
    ...

class Upcoming(Task):
    ...

class MainWindow(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.db = Database()
    
    def add_new(self):
        """
        Description of add_new

        Args:
            self (undefined):

        """
        nt = NewTask()
        nt.open()
    
    def add_task(self, mv, xtask: tuple):
        
        error = False
        scroll_parent = self.ids.scroll_parent
        tw = self.ids.today_wrapper
        for t in xtask:
            if len(t.text) < 1:
                t.hint_text ='Field required'
                t.hint_text_color = [1,0,0,1]
                error = True
        if error:
            pass
        else:
            task= Today()
            task.name = xtask[0].text
            task.time = xtask[1].text
            task.date = xtask[2].text
            task.size_hint = (None, None)
            task.size = [scroll_parent.width/2.4, scroll_parent.height-(.1*scroll_parent.height)]
            tw.add_widget(task)
            mv.dismiss()

            # check if we have enough task to show 
            # if len(tw.children) > 1:
            #     for child in tw.children:
            #         if type(child) == NewButton:
            #             tw.remove_widget(child)
            #             break

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