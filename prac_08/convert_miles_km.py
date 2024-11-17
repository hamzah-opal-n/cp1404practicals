"""Miles to Kilometres Converter"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KILOMETRES_RATE = 1.60934


class MilesToKilometresConverter(App):
    """MilesToKilometresConverter is a Kivy App for converting distances in miles to kilometres."""
    distance_in_kilometres = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (500, 250)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """Handle conversion from miles to kilometres"""
        self.distance_in_kilometres = str(float(self.root.ids.input_number.text) * MILES_TO_KILOMETRES_RATE)

    def handle_increment(self, increment):
        """Handle increment of specified value"""
        value = float(self.root.ids.input_number.text) + increment
        self.root.ids.input_number.text = str(value)


MilesToKilometresConverter().run()
