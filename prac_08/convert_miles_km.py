"""Miles to Kilometres Converter"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometresConverter(App):
    """MilesToKilometresConverter is a Kivy App for converting distances in miles to kilometres."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (500, 250)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesToKilometresConverter().run()
