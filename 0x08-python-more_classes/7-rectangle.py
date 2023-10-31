#!/usr/bin/python3
"""A script that creates a class rectangle"""
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ method to create a rectangle
        Args:
            width(int): Integer width
            height(int): Integer height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width
        Args:
            width (int): the value of width of rectangle
        Raises:
            TypeError: if `width` is not an integer
            ValueError: if `width` is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height
        Args:
            height (int): the value of height of rectangle
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
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 0 if self.__width == 0 or self.__height == 0 else 2 * (self.__width + self.__height)

    def __str__(self):
        """Representation of Rectangle with"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width + "\n"
        return rect_str[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
