from kivy.uix.screenmanager import ScreenManager

class NavigationScreenManager(ScreenManager):
    screen_stack = []
    
    def push(self, screen_name):
        if screen_name is not self.screen_stack:
            self.screen_stack.append(self.current) # save the current screen (previous screen) to the list
            self.transition.direction = "left"
            self.current = screen_name # move to the next screen

    def pop(self):
        if len(self.screen_stack) > 0:
            screen_name =  self.screen_stack[-1] # go back to the previous screen saved in the stack
            del self.screen_stack[-1] # delete previous screen from stack
            self.transition.direction = "right"
            self.current = screen_name 
        
