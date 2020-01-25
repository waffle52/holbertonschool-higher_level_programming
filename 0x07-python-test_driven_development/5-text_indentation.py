#!/usr/bin/python3
"""
Module that seperates text based on chars
"""


def text_indentation(text):
    """
    >>> text_indentation("This text should go to new line. hello there")
    """
    if text is None:
        return None
    if type(text) != str:
        raise TypeError("text must be a string")
    new = '\n\n'
    text = text.replace('.', '.' + new)
    text = text.replace('?', '?' + new)
    text = text.replace(':', ':' + new)

    print("\n".join([x.strip() for x in text.split("\n")]), end="")
