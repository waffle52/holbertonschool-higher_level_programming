#!/usr/bin/python3
class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """def init"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        for i in range(len(value)):
            if type(value[i]) != int or i == 3:
                raise TypeError("position must be a tuple" +
                                "of 2 positive integers")
        self.__position = value

    def area(self):
        """def area"""
        return self.__size ** 2

    def my_print(self):
        """ prints Square """
        if self.__size == 0:
            print("")
        else:
            if self.position[1] > 0:
                    for h in range(0, self.position[1]):
                        print("")
            for j in range(self.size):
                for h in range(self.position[0]):
                    print(" ", end="")
                for i in range(self.size):
                    print("#", end="")
                print("")
