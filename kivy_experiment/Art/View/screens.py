# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.signup_screen import SignupScreenModel
from Controller.signup_screen import SignupScreenController
from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.splash_screen import SplashScreenModel
from Controller.splash_screen import SplashScreenController
from Model.profile_screen import ProfileScreenModel
from Controller.profile_screen import ProfileScreenController
from Model.art_screen import ArtScreenModel
from Controller.art_screen import ArtScreenController

screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },

    "signup screen": {
        "model": SignupScreenModel,
        "controller": SignupScreenController,
    },

    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },

    "splash screen": {
        "model": SplashScreenModel,
        "controller": SplashScreenController,
    },

    "profile screen": {
        "model": ProfileScreenModel,
        "controller": ProfileScreenController,
    },

    "art screen": {
        "model": ArtScreenModel,
        "controller": ArtScreenController,
    },
}