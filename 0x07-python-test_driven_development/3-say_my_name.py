#!/usr/bin/python3
"""

Module to print name based on parameters given

"""


def say_my_name(first_name, last_name=""):
    """ Prints name if both variables are string
    >>> say_my_name("Sage", "Meadows")
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
