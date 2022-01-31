import os
import importlib
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from kaki.app import App




class StarMumApp(App):
    KV_FILES = {
        os.path.join(os.getcwd(), "Screens", "RootScreen", "root_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "TodayScreen", "today_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "HomeScreen", "home_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "HomeScreen", "components", "card.kv"),
    }
    CLASSES = {
        "RootScreen": "Screen.RootScreen.root_screen",
        "TodayScreen": "Screens.TodayScreen.today_screen",
        "HomeScreen": "Screens.HomeScreen.home_screen",
        "CustomCard": "Screens.HomeScreen.components.card",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        self.theme_cls.primary_palette = "Orange"
        import Screens.RootScreen.root_screen

        Window.bind(on_keyboard=self._rebuild)
        importlib.reload(Screens.RootScreen.root_screen)

        return Screens.RootScreen.root_screen.RootScreen()
    
    def _rebuild(self, *args):
        if args[1] == 32:
            self._rebuild()

StarMumApp().run()
