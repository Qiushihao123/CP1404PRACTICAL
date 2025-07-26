from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934  # Constant conversion factor


class MilesConverterApp(App):
    output_text = StringProperty()

    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = "0.0"
        return self.root

    def handle_calculate(self):
        """Convert miles to kilometres and update the label."""
        miles = self.get_miles()
        km = miles * MILES_TO_KM
        self.output_text = f"{km:.3f}"

    def handle_increment(self, change):
        """Increment/decrement the input miles and update the result."""
        miles = self.get_miles()
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_miles(self):
        """Attempt to parse miles input, return 0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


if __name__ == '__main__':
    MilesConverterApp().run()
