"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase to start with a capital and end with a single full stop.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("what a nice day")
    'What a nice day.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]


def run_tests():
    """Run the tests on the functions."""
    # Testing repeat_string
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Testing Car class (from prac_06.car)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"
    assert car.fuel == 0, "Car does not set default fuel correctly"

    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car does not set custom fuel correctly"


run_tests()
doctest.testmod()
