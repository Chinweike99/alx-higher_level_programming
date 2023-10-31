#!/usr/bin/python3
"""The module Writes a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)"""

class Rectangle:
    def __init__(self, width=0, height=0):
        """
        This constructor Initializes a Rectangle with optional width and height.
        :param width: Width of the rectangle (default is 0)
        :param height: Height of the rectangle (default is 0)
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width of the rectangle.
        :param value: The width to set.
        """
        if not isinstance(value, int):
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
        Set the height of the rectangle.
        Args:
            height (int): value for height of rectangle
        Raises:
            TypeError: if `height` is not an integer
            ValueError: if `height` is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle with # characters.
        If width or height is equal to 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        string = ''
        for r in range(self.__height):
            string += '#' * self.width + "\n"
        return string[:-1]


    def __repr__(self):
        """Return a string representation of the rectangle for debugging."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message Bye rectangle"""
        print("Bye rectangle...")
