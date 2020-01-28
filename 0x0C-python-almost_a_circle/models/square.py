#!/usr/bin/python3
""" class Square """

from models.rectangle import Rectangle
""" importing Rectangle file to inherit"""


class Square(Rectangle):
    """  Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize variables"""
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """ Return string """
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size))

    @property
    def size(self):
        """ Return value of size """
        return self.width

    @size.setter
    def size(self, value):
        """ Set size to value """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
