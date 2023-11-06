#!/usr/bin/python3
"""Integer validator Module"""

class BaseGeometry:
    """A class Geometry from 5-base_geometry"""

    def area(self):
        raise Exception ("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer and check if it is greater than 0.
        Args:
            name - String representing the name of the value
            value - The value to be Validated
        Raises:
            TypeError: If the value is not an integer.
            ValueError: if the value is less than or equal to 0.
        """
        self.value = value

        if not isinstance(value, int):
            raise TypeError ("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError ("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
