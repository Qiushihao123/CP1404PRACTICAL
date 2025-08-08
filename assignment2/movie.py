class Movie:
    """A class representing a movie."""

    def __init__(self, title: str, year: int, category: str, is_watched: bool = False):
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def mark_watched(self):
        self.is_watched = True

    def mark_unwatched(self):
        self.is_watched = False

    def __str__(self):
        status = "watched" if self.is_watched else "unwatched"
        return f"{self.title} ({self.year}) - {self.category} ({status})"