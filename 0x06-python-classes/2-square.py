#!/usr/bin/python3
class Square:
    """class Square"""
    def __init__(self, size=0):
        """def init"""
        try:
            self.__size = size
            if type(size) is not int:
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            pass
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
