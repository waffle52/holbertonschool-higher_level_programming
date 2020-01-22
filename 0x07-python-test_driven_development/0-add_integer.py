#!/usr/bin/python3
"""

Module to add two numbers together

"""


def add_integer(a, b=98):
    """ Returns addition of both integers
    >>> result = add_integer(10, 15)
    """
    if a is None or b is None:
        return None
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
