#!/usr/bin/python3
class Square:
    """class Square"""
    def __init__(self, size=0):
        """def init"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """def area"""
        return self.__size ** 2

    def my_print(self):
        """ prints Square """
        if self.__size == 0:
            print("")
        else:
            for j in range(self.size):
                for i in range(self.size):
                    print("#", end="")
                print("")
