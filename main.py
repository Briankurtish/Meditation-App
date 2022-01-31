import os
import importlib
from kivymd.app import MDApp
from kivy.core.window import Window

from kaki.app import App

class MeditationAppLive(App):
    KV_FILES = {
        os.path.join(os.getcwd(), "Screens", "RootScreen", "root_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "TodayScreen", "today_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "AllExercisesScreen", "all_exercises_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "AllExercisesScreen", "components", "card.kv"),
    }
    CLASSES = {
        "RootScreen": "Screen.RootScreen.root_screen",
        "TodayScreen": "Screens.TodayScreen.today_screen",
        "AllExercisesScreen": "Screens.AllExercisesScreen.all_exercises_screen",
        "Card": "Screens.AllExercisesScreen.components.card",
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

MeditationAppLive().run()
