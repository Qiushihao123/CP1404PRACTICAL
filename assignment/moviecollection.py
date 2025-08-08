import json
from operator import attrgetter
from movie import Movie


class MovieCollection:
    """A collection of Movie objects."""

    def __init__(self):
        self.movies = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def get_number_watched(self):
        return sum(1 for m in self.movies if m.is_watched)

    def get_number_unwatched(self):
        return sum(1 for m in self.movies if not m.is_watched)

    def load_movies(self, filename: str):
        with open(filename, 'r') as f:
            data = json.load(f)
            for entry in data:
                movie = Movie(entry['title'], entry['year'], entry['category'], entry['is_watched'])
                self.add_movie(movie)

    def save_movies(self, filename: str):
        with open(filename, 'w') as f:
            json.dump([vars(movie) for movie in self.movies], f, indent=4)

    def sort(self, key: str):
        self.movies.sort(key=attrgetter(key, "title"))
