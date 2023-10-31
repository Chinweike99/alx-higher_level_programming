#!/usr/bin/python3
"""This module writes a class that defines a rectangle"""

class Rectangle:
    """A class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializer of rectangle

        Args:
            width: the width of the rectangle (int)
            height: the height of the rectangle (int)
        """
        self.w__idth = width
        self.__height = height

    @property
    def width(self):
        """
        Args: width getter (int)
        Raise:
            TypeError - if width not an integer
            ValueError: if width is < 0
        Returns: 
            The width of of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args: width setter (int)

        Raises:
            TypeError: if width not an integer
            ValueError: if width is < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args: height setter (int)
        Raises:
            TypeError: if height not an integer
            ValueError: if height is < 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
