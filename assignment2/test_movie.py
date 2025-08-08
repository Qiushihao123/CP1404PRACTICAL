from movie import Movie


def test_movie_class():
    # Create movie and check default values
    movie = Movie("Inception", 2010, "Action")
    assert movie.title == "Inception"
    assert movie.year == 2010
    assert movie.category == "Action"
    assert not movie.is_watched

    # Test __str__
    assert str(movie) == "Inception (2010) - Action (unwatched)"

    # Mark as watched
    movie.mark_watched()
    assert movie.is_watched

    # Mark as unwatched again
    movie.mark_unwatched()
    assert not movie.is_watched

    print("test_movie_class passed.")
