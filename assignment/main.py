from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from movie import Movie
from moviecollection import MovieCollection

FILENAME = 'movies.json'
BUTTON_WATCHED_COLOR = [0.5, 0.5, 0.5, 1]   # grey
BUTTON_UNWATCHED_COLOR = [1, 0.7, 0.2, 1]   # orange

class MoviesApp(App):
    """Kivy App for Must-See Movies 2.0"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()

    def build(self):
        self.title = "Must-See Movies 2.0"
        self.root = Builder.load_file('app.kv')
        self.movie_collection.load_movies(FILENAME)
        self.create_movie_buttons()
        self.update_status_label()
        return self.root

    def create_movie_buttons(self):
        """Create buttons for each movie and add to the right panel"""
        self.root.ids.movies_box.clear_widgets()
        for movie in self.movie_collection.movies:
            button = Button(
                text=f"{movie.title} ({movie.year})",
                background_color=BUTTON_WATCHED_COLOR if movie.is_watched else BUTTON_UNWATCHED_COLOR
            )
            button.bind(on_release=self.handle_movie_click)
            button.movie = movie  # attach movie object to button
            self.root.ids.movies_box.add_widget(button)

    def handle_movie_click(self, button):
        """Handle clicking a movie button to toggle watched/unwatched"""
        movie = button.movie
        if movie.is_watched:
            movie.mark_unwatched()
            self.root.ids.status_label.text = f"{movie.title} marked as unwatched"
        else:
            movie.mark_watched()
            self.root.ids.status_label.text = f"{movie.title} marked as watched"
        self.create_movie_buttons()
        self.update_status_label()

    def update_status_label(self):
        """Update the top status label showing watched/unwatched counts"""
        watched = self.movie_collection.get_number_watched()
        unwatched = self.movie_collection.get_number_unwatched()
        self.root.ids.movie_count_label.text = f"Watched: {watched} | To Watch: {unwatched}"

    def on_stop(self):
        """Save data on exit"""
        self.movie_collection.save_movies(FILENAME)

    def add_movie(self):
        """Add a new movie from text inputs"""
        title = self.root.ids.input_title.text.strip()
        year_str = self.root.ids.input_year.text.strip()
        category = self.root.ids.input_category.text.strip().title()

        if not title or not year_str or not category:
            self.root.ids.status_label.text = "All fields must be completed"
            return

        try:
            year = int(year_str)
            if year < 1:
                raise ValueError
        except ValueError:
            self.root.ids.status_label.text = "Please enter a valid number"
            return

        if category not in ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"]:
            self.root.ids.status_label.text = "Invalid category; using Other"
            category = "Other"

        new_movie = Movie(title, year, category)
        self.movie_collection.add_movie(new_movie)
        self.create_movie_buttons()
        self.update_status_label()
        self.clear_inputs()
        self.root.ids.status_label.text = f"{title} ({category} from {year}) added"

    def clear_inputs(self):
        """Clear input fields and status label"""
        self.root.ids.input_title.text = ""
        self.root.ids.input_year.text = ""
        self.root.ids.input_category.text = ""
        self.root.ids.status_label.text = ""
