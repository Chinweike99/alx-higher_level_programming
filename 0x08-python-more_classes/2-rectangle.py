#!/usr/bin/python3
"""A script that defines a Rectangle and gets Area and Perimeter"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializer of rectangle class

        Args:
            width: the width of the rectangle (int)
            height: the height of the rectangle (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width setter

        Raises:
            TypeError: if value not an integer
            ValueError: if value is < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter

        Raises:
            TypeError: if value not an integer
            ValueError: if value is < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter

        Returns:
            the height of the rectangle  (int)
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
        """Returns the area of the rectangle

        Returns:
            the rectangle area (int)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle

        Returns:
            0 if one of width or height is none
            the rectangle perimeter (int)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height)*2
