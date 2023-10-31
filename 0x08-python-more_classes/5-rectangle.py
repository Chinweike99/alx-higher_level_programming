#!/usr/bin/python3
"""The module Writes a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)"""

class Rectangle:
    """Rectangle class
    Args:
        width: the private instance attribute(int)
        height: the private instance attribute for height (int)
    """
    def __init__(self, width=0, height=0):
        """Constructor of the Rectangle class

        Args:
            width: The width of the rectangle (int)
            height: The height of the rectangle (int)
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle.

        Raises:
            TypeError: if the value is not an integer
            Valueerror: if value is < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle.

        Returns:
            the height of the rectangle (int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
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
        """Prints out the rectangle
        Returns:
            The geometric format with print_symbol (str)
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
        """Deletes the istances of the Rectangle"""
        print("Bye rectangle...")
