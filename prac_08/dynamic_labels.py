from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

DynamicLabelsApp().run()