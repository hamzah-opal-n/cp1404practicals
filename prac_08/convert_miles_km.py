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
        miles = self.get_valid_miles()
        kilometres = miles * MILES_TO_KILOMETRES_RATE
        self.distance_in_kilometres = str(kilometres)

    def get_valid_miles(self):
        """Ensure that the value in the miles text input is valid."""
        try:
            miles = float(self.root.ids.input_number.text)
            return miles
        except ValueError:
            return 0.0

    def handle_increment(self, increment):
        """Handle increment of specified value"""
        miles = self.get_valid_miles()
        miles += increment
        self.root.ids.input_number.text = str(miles)


MilesToKilometresConverter().run()
