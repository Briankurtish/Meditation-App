import os
import importlib
from sys import path
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder

from kaki.app import App
from Screens.HomeScreen.trimester_1 import Trimester_1
from Screens.HomeScreen.trimester_2 import Trimester_2

from Screens.RootScreen.root_screen import RootScreen
from Screens.HomeScreen.home_screen import HomeScreen
from Screens.HomeScreen.components.card import CustomCard


# screen_helper = """
# ScreenManager:
#     Trim1Screen:
#     Trim2Screen:

# <Trim1Screen>:
#     name: 'trim1'
#     MDRectangularFlatButton:
#         text: 'profile'
#         pos_hint: {'center_x':0.5, 'center_y':0.5}
#         on_press: root.manager.current = 'trim2'

# <Trim2Screen>:
#     name: 'trim2'
#     MDLabel:
#         text: 'Welcome'
#         halign: 'center'
        

# """


sm = ScreenManager()
sm.add_widget(Trimester_1(name='trim1'))
sm.add_widget(Trimester_2(name='trim2'))



class StarMumApp(App):
    

    def build_app(self):
        Window.size = [400, 600]
        self.load_all_kv_files()
        self.theme_cls.primary_palette = "Orange"
        import Screens.RootScreen.root_screen

        Window.bind(on_keyboard=self._rebuild)
        importlib.reload(Screens.RootScreen.root_screen)

        return Screens.RootScreen.root_screen.RootScreen()
    
    def load_all_kv_files(self):
        Builder.load_file('Screens/RootScreen/root_screen.kv')
        Builder.load_file('Screens/HomeScreen/home_screen.kv')
        Builder.load_file('Screens/HomeScreen/components/card.kv')
        Builder.load_file('Screens/HomeScreen/trimester_1.kv')

    
    def _rebuild(self, *args):
        if args[1] == 32:
            self._rebuild()

StarMumApp().run()
