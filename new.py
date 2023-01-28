"""
CP1404 Practical
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):

    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():


    assert repeat_string("Python", 1) == "Python"

    assert repeat_string("hi", 2) == "hi hi"


    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"


    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    test_car = Car()
    assert test_car.fuel == 0




def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a .
    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('This subject rocks')
    'This subject rocks.'
    """

    sentence = phrase.capitalize()

    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()