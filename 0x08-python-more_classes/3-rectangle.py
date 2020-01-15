#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """ init function """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Returns value of object width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets value of object width """
        if type(value) != int:
            raise ValueError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns value of object height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets value of object height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns area of rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Returns perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """ returns string """
        str = ""
        if self.width == 0 or self.height == 0:
            return str
        else:
            for j in range(self.height):
                for i in range(self.width):
                    str += "#"
                if j + 1 != self.height:
                    str += "\n"
            return str
