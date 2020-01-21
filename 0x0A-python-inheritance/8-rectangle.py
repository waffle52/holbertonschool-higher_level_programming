#!/usr/bin/python3
class Rectangle:
    def __init__(self, width, height):
        BaseGeometry = __import__('7-base_geometry').BaseGeometry
        bg = BaseGeometry()
        bg.integer_validator("width", width)
        bg.integer_validator("height", height)
        self.__width = width
        self.__height = height
