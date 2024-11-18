from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesToKilometersApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 250)
        self.title = "Convert Miles To Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

ConvertMilesToKilometersApp().run()