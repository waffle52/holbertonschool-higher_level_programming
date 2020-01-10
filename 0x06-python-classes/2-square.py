#!/usr/bin/python
class Square:
    """class Square"""
    def __init__(self, size=0):
        """def init"""
        try:
            self._Square__size = size
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
