#!/usr/bin/python3


from models.base import Base
""" importing Base file to set rules of ojbect """


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init function """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Returns value of object width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets value of object width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Returns value of object height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets value of object height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Returns value of object x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets value of object x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Returns value of object y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets value of object y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """ Displays grid by width * height"""
        for x in range(self.y):
            print("")
        for i in range(self.height):
            for y in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ Function that returns string info of class """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args):
        """ Updates value from args """
        if len(args) >= 1:
            super().__init__(args[0])
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
