FILENAME = 'movies.csv'
VALID_CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
STATUS_UNWATCHED = 'u'
STATUS_WATCHED = 'w'


def main():
    """Main program loop"""
    print("Must-See Movies 1.0 - by Qiu Shihao")
    movies = load_movies(FILENAME)
    print(f"{len(movies)} movies loaded from {FILENAME}")

    while True:
        print("\nMenu:\nD - Display movies\nA - Add new movie\nW - Watch a movie\nQ - Quit")
        choice = input(">>> ").strip().upper()
        if choice == "D":
            display_movies(movies)
        elif choice == "A":
            add_movie(movies)
        elif choice == "W":
            watch_movie(movies)
        elif choice == "Q":
            save_movies(FILENAME, movies)
            print(f"{len(movies)} movies saved to {FILENAME}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def load_movies(filename):
    """Load movies from file and return as list of lists"""
    movies = []
    with open(filename, 'r') as file:
        for line in file:
            title, year, category, status = line.strip().split(',')
            movies.append([title, int(year), category, status])
    return movies


def save_movies(filename, movies):
    """Save movies to file"""
    with open(filename, 'w') as file:
        for movie in movies:
            print(f"{movie[0]},{movie[1]},{movie[2]},{movie[3]}", file=file)


def display_movies(movies):
    """Display all movies in formatted list"""
    sorted_movies = sorted(movies, key=lambda m: (m[1], m[0]))
    to_watch = watched = 0

    for i, movie in enumerate(sorted_movies, start=1):
        marker = "*" if movie[3] == STATUS_UNWATCHED else " "
        print(f"{i:2}. {marker} {movie[0]:35} - {movie[1]:4} ({movie[2]})")
        if movie[3] == STATUS_UNWATCHED:
            to_watch += 1
        else:
            watched += 1

    print(f"{watched} movies watched. {to_watch} movies still to watch.")


def add_movie(movies):
    """Add a new movie to the list"""
    title = input_non_blank("Title: ")
    year = input_positive_integer("Year: ")
    print("Categories available: Action, Comedy, Documentary, Drama, Thriller, Other")
    category = input_non_blank("Category: ").title()
    if category not in VALID_CATEGORIES:
        print("Invalid category; using Other")
        category = "Other"

    movies.append([title, year, category, STATUS_UNWATCHED])
    print(f"{title} ({category} from {year}) added to movie list")


def watch_movie(movies):
    """Mark a movie as watched by its number"""
    if not any(movie[3] == STATUS_UNWATCHED for movie in movies):
        print("No more movies to watch!")
        return

    print("Enter the movie number to mark watched.")
    sorted_movies = sorted(movies, key=lambda m: (m[1], m[0]))
    display_movies(sorted_movies)

    while True:
        try:
            choice = int(input(">>> "))
            if choice < 1:
                print("Number must be >= 1")
            elif choice > len(sorted_movies):
                print("Invalid movie number.")
            else:
                selected = sorted_movies[choice - 1]
                if selected[3] == STATUS_WATCHED:
                    print(f"You have already watched {selected[0]}.")
                else:
                    selected[3] = STATUS_WATCHED
                    print(f"{selected[0]} ({selected[1]}) watched.")
                break
        except ValueError:
            print("Invalid input; enter a valid number")


def input_non_blank(prompt):
    """Prompt for non-blank input"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input can not be blank")


def input_positive_integer(prompt):
    """Prompt for a positive integer input"""
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