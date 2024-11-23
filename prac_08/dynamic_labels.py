"""Dynamic Labels"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that creates Labels dynamically from a list of data."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Sonic", "Ivo Robotnik", "Agent Stone", "Tails", "Knuckles",
                      "Shadow", "Gerald Robotnik", "Amy?", "Metal Sonic?"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            new_label = Label(text=name)
            self.root.ids.main.add_widget(new_label)


DynamicLabelsApp().run()
