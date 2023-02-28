from kivy.uix.boxlayout import BoxLayout

class MainWindow(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    def auth_user(self, username,  password):
        """Authenticates a user given credentials
        from inputs
        
        Args:
            username (kivy.uix.textinput.TextInput): 
                - textinput containing the username
            
            password (kivy.uix.textinput.TextInput): 
                - textinput containing the password
        
        Returns:
            None
        """

        uname = username.text
        upass = password.text

        self.ids.scrn_mngr.current = 'scrn_main'