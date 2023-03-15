from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView
from kivy.garden.circulardatetimepicker import CircularTimePicker
from kivy.uix.button import Button

from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window

from kivy.metrics import sp,dp
from kivy.utils import rgba
from app.storage.db import Database

from datetime import datetime

class NewTask(ModalView):
    def __init__(self, **kw):
        super().__init__(**kw)

    def get_time(self):
        mv = ModalView(size_hint=[.8,.8])
        box = BoxLayout(orientation = 'vertical', size_hint=[.8,.8])
        mv.add_widget(box)

        cl = CircularTimePicker(color=[1,1,1,1])
        cl.bind(time= self.set_time)
        
        submit = Button(text="OK", background_normal='', bold= True, color=rgba('#282C34'), background_color=[1,1,1,1], size_hint_y=.1)
        submit.bind(on_release=lambda x: self.update_time(cl.time, mv))
        box.add_widget(cl)
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
    og_name = StringProperty('')
    time = StringProperty('')
    date = StringProperty('')
    def __init__(self, **kw):
        super().__init__(**kw)

        self.bind(on_release=lambda x: self.view_task())
    
    def view_task(self):
        vt = ViewTask()
        vt.ids.name.text = self.name
        vt.ids.time.text = self.time
        vt.ids.date.text = self.date
        vt.open()


class ViewTask(ModalView):
    ...

class Today(Task):
    ...

class Upcoming(Task):
    ...

class MainWindow(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.db = Database()

        self.init_view()

    def init_view(self):
        """ get all tasks from db and show it
        """ 
        all_tasks = self.db.get_tasks()
        scroll_parent = Window
        tw = self.ids.today_wrapper
        uw = self.ids.upcoming

        for t in all_tasks:
            date, time = t[2].rsplit(' ', 1) # split the outputs separated by space
            
            if self.clean_date(date):
                task = Today() # from main page
                task.og_name = t[1]
                task.name = t[1].upper()
                task.time = time
                task.date = date
                task.size_hint = (None, 1) # 1 means use the available hight for the widget
                task.size = [scroll_parent.width/2.4, 45]  # 45 will not work since Window function overides whetever is in here   
                
                t_task = Today() # from today page
                t_task.name = t[1].upper()
                t_task.og_name = t[1]
                t_task.time = time
                t_task.date = date
                t_task.size_hint = (None, None) # 1 means use the available hight for the widget
                t_task.size = [scroll_parent.width/2.4, round(scroll_parent.height/4)]  # 4 divisions
                
                tw.add_widget(task)
                self.ids.all_today.add_widget(t_task)

                
            else:
                task = Upcoming() # from main page
                task.og_name = t[1]
                task.name = t[1].upper()
                task.time = ' '.join([date,time])
                task.date = date
                task.size_hint = [1, None]
                task.height = dp(100)

                u_task = Upcoming() # from upcoming page
                u_task.name = t[1]
                u_task.time = ' '.join([date,time])
                u_task.date = date
                u_task.size_hint = (None, None) 
                u_task.size = [scroll_parent.width, round(scroll_parent.height/4)]  # 4 divisions

                uw.add_widget(task)
                self.ids.all_upcoming.add_widget(u_task)

        # check if we have enough task to show 
        # if len(tw.children) > 1:
        #     for child in tw.children:
        #         if type(child) == NewButton:
        #             tw.remove_widget(child)
        #             break
            
            

    
    def clean_date(self, date: str):
        today = datetime.today()
        print('today',today)
        _date = date.split('/')
        if len(_date) < 3:
            _date = date.split('-')
        date_ = [int(x) for x in reversed(_date)]

        task_date = datetime(date_[0], date_[1], date_[2])
        print('task_date',task_date)

        x = abs((today - task_date).days)
        if x == 0:
            return True
        else:
            return False

    def get_update(self, inst):
        nt = NewTask()  
        nt.ids.task_name.text = inst.name
        nt.ids.task_time.text = inst.time
        nt.ids.task_date.text = inst.date
        nt.ids.submit_wrapper.clear_widgets()
        submit = Button(text="Update Task", background_normal='', bold= True, color=rgba('#282C34'), background_color=rgba('#F8F9FD'))
        submit.bind(on_release=lambda x: self.update_task(nt, inst))
        nt.ids.submit_wrapper.add_widget(submit)
        nt.open()

    def update_task(self, task_data, task):
        xtask = [
            task_data.ids.task_name.text,
            task_data.ids.task_date.text,
            task_data.ids.task_time.text
        ]
        error = None
        for t in xtask:
            if len(t) < 3:
                t.hint_text ='Field required'
                t.hint_text_color = [1,0,0,1]
                error = True
        if error:
            pass
        else:
            xtask = [xtask[0], ' '.join(xtask[1:]), task.og_name]
            if self.db.update_task(xtask):
                task.name = task_data.ids.task_name.text
                task.time = task_data.ids.task_time.text
                task.date = task_data.ids.task_date.text
        
        task_data.dismiss()
                
    def delete_task(self, task: Today):
        """ delete a task from the today module and also delete it from the database

        Args:
            task (Today): _description_
        """        
        name = task.name
        if self.db.delete_task(name):
            task.parent.remove_widget(task)
    
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
        uw = self.ids.upcoming
        for t in xtask:
            if len(t.text) < 3:
                t.hint_text ='Field required'
                t.hint_text_color = [1,0,0,1]
                error = True
        if error:
            pass
        else:
            date = ' '.join([xtask[1].text, xtask[2].text])
            task_ = (xtask[0].text, date)

            if self.clean_date(xtask[1].text):
                task = Today()
                task.og_name = xtask[0].text
                task.name = xtask[0].text.upper()
                task.time = xtask[2].text
                task.date = xtask[1].text
                task.size_hint = (None, None)
                task.size =  [scroll_parent.width/2.4,scroll_parent.height-(.1*scroll_parent.height)]
                if self.db.add_task(task_):
                    tw.add_widget(task)
            else:
                task = Upcoming()
                task.og_name = xtask[0].text
                task.name = xtask[0].text.upper()
                task.time = xtask[2].text
                task.date = xtask[1].text
                task.size_hint = [1, None]
                task.height = dp(100)
                if self.db.add_task(task_):
                    uw.add_widget(task)

            #add task to db
            mv.dismiss()


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