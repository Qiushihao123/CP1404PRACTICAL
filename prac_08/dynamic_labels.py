from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NamesApp(App):
    def build(self):
        self.title = "Dynamic Name Labels"
        self.root = Builder.load_file('names_app.kv')

        # This is our "model" - the data
        names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

        # Dynamically create Labels for each name
        for name in names:
            temp_label = Label(text=name, font_size=24, size_hint_y=None, height=40)
            self.root.ids.main.add_widget(temp_label)

        return self.root


if __name__ == '__main__':
    NamesApp().run()
