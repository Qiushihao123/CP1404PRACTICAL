from kivy.app import App
from kivy.lang import Builder


class SquaringApp(App):
    def build(self):
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_square(self):
        try:
            user_input = self.root.ids.input_number.text
            number = int(user_input)
            result = number ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"
