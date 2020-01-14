#!/usr/bin/python3
"""

Module to print a sqaure by size given

"""


def print_square(size):
    """ Prints a square by number given
    >>> print_square(20)
    """
    if size == None:
        return None
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
