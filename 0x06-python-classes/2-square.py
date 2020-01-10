#!/usr/bin/python3
class Square:
    """class Square"""
    def __init__(self, size=0):
        """def init"""
        try:
            if isinstance(size, int):
                self._Square__size = size
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
