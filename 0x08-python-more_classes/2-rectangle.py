#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)"""
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
        """
         This property Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This Set the width of the rectangle.
        :param value: The width to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        :param value: The height to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        :return: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        :return: The perimeter of the rectangle.
        """
        return 0 if self.__width == 0 or self.__height == 0 else 2 * (self.__width + self.__height)
