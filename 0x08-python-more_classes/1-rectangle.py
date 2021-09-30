#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """An empty Square Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if self < 0:
            raise ValueError("width must be >= 0")
        self.__size = value

    @height.setter
    def height(self, value):
        if type(self) is not int:
            raise TypeError("height must be an integer")
        if self < 0:
            raise ValueError("height must be >= 0")
        self.__size = value
