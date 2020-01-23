#!/usr/bin/python3
"""

Module that seperates text based on chars

"""


def text_indentation(text):
    """
    >>> text_indentation("This text should go to new line. hello therex")
    """
    if text is None:
        return None
    if type(text) != str:
        raise TypeError("text must be a string")
    it = iter(text)
    for i in it:
        if (i == '.' or i == '?' or i == ':'):
            print("{}".format(i), end="")
            print("\n")
            next(it)
        else:
            print("{}".format(i), end="")
