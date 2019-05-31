"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""
import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s]*n)


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


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the failing test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car = Car()
    assert test_car.fuel == 0

    assert automatic_sentence('It is an ex parrot.')

def automatic_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a .
    >>> automatic_sentence('hello')
    'Hello.'
    >>> automatic_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> automatic_sentence('This subject rocks')
    'This subject rocks.'
    """
    sentence = phrase.capitalize()
    if sentence[-1] != ".":
        sentence += "."
    return sentence

run_tests()
doctest.testmod()