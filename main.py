import kivy
from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp
# from kivymd.app import MDApp
import os
class MainApp(App,MDApp):
    KV_FILES = {
        os.path.join(os.getcwd(),"view/dash.kv")
    }
    CLASSES = {
        "Myapp":"view.dash"
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True})

    ]

    def build_app(self):
        return Factory.Myapp()

MainApp().run()

