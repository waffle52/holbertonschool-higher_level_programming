#!/usr/bin/python3
class Square:
    """class Square"""
    def __init__(self, size=0):
        """def init"""
        self.__size = size
        if type(size) is not int:
            print("size must be an integer")
            raise TypeError
        elif size < 0:
            print("size must be >= 0")
            raise ValueError
