from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION_RATE = 1.609

class ConvertMilesToKilometersApp(App):
    message = StringProperty()
    input_text = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 250)
        self.title = "Convert Miles To Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Enter miles click convert button"
        return self.root

    def handle_increment_update(self, change):
        try:
            modified_number = float(self.root.ids.input_number.text) + 1 * change
        except ValueError:
            modified_number = 0 + 1 * change
        self.input_text = str(modified_number)

    def convert_miles_to_kilometers(self, miles):
        try:
            kilometers = float(miles) * CONVERSION_RATE
            return str(kilometers)
        except ValueError:
            print("Incorrect value has been entered")
            return "0.0"

    def handle_output_label_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.message = self.convert_miles_to_kilometers(self.root.ids.input_number.text)


ConvertMilesToKilometersApp().run()
