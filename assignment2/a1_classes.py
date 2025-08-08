from moviecollection import MovieCollection
from movie import Movie

FILENAME = 'movies.json'


def main():
    print("Must-See Movies 2.0 - by Qiu Shihao")
    collection = MovieCollection()
    collection.load_movies(FILENAME)
    print(f"{len(collection.movies)} movies loaded from {FILENAME}")

    while True:
        print("\nMenu:\nD - Display movies\nA - Add new movie\nW - Watch a movie\nQ - Quit")
        choice = input(">>> ").strip().upper()
        if choice == "D":
            display_movies(collection)
        elif choice == "A":
            add_movie(collection)
        elif choice == "W":
            watch_movie(collection)
        elif choice == "Q":
            collection.save_movies(FILENAME)
            print(f"{len(collection.movies)} movies saved to {FILENAME}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def display_movies(collection):
    movies = sorted(collection.movies, key=lambda m: (m.year, m.title))
    for i, movie in enumerate(movies, 1):
        marker = "*" if not movie.is_watched else " "
        print(f"{i:2}. {marker} {movie.title:35} - {movie.year:4} ({movie.category})")

    print(f"{collection.get_number_watched()} movies watched. {collection.get_number_unwatched()} movies still to watch.")


def add_movie(collection):
    title = input_non_blank("Title: ")
    year = input_positive_integer("Year: ")
    category = input_non_blank("Category: ").title()
    if category not in ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]:
        print("Invalid category; using Other")
        category = "Other"

    movie = Movie(title, year, category)
    collection.add_movie(movie)
    print(f"{title} ({category} from {year}) added to movie list")


def watch_movie(collection):
    movies = sorted(collection.movies, key=lambda m: (m.year, m.title))
    unwatched_movies = [m for m in movies if not m.is_watched]

    if not unwatched_movies:
        print("No more movies to watch!")
        return

    display_movies(collection)
    choice = input_positive_integer("Enter the movie number to mark watched: ")
    if 1 <= choice <= len(movies):
        movie = movies[choice - 1]
        if movie.is_watched:
            print(f"You have already watched {movie.title}.")
        else:
            movie.mark_watched()
            print(f"{movie.title} ({movie.year}) watched.")
    else:
        print("Invalid movie number.")


def input_non_blank(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be blank")


def input_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            print("Number must be >= 1")
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == "__main__":
    main()
