from kivymd.uix.card import MDCard
from kivy.uix.button import ButtonBehavior 
from kivy.properties import StringProperty


class CustomCard(MDCard, ButtonBehavior):
    source = StringProperty()
    text = StringProperty()