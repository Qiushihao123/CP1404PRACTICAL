from movie import Movie
from moviecollection import MovieCollection


def test_moviecollection_class():
    collection = MovieCollection()

    # Add movies
    movie1 = Movie("Inception", 2010, "Action")
    movie2 = Movie("Interstellar", 2014, "Drama", is_watched=True)
    collection.add_movie(movie1)
    collection.add_movie(movie2)

    assert len(collection.movies) == 2
    assert collection.get_number_unwatched() == 1
    assert collection.get_number_watched() == 1

    # Test sort by year then title
    collection.sort("year")
    assert collection.movies[0].title == "Inception"

    print("test_moviecollection_class passed.")
