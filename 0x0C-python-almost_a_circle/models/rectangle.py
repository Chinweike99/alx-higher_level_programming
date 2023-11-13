#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor
        Args:
            width(int): Rectangle width
            height(int): Rectangle height
            x(int): x - coordinate
            y (int): y - coordinate
            id (int): id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Rectangle getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle Setter
        Args:
            value: size of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter
        Args:
            value: height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter
        Args:
            value: x coordinate
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        Args:
            value: y coordinate of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method to get area of rectangle"""
        return self.width * self.height

    def display(self):
        """Print in stdout the Rectangle instance"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update public method
        Args:
            Args: Assigns an argument to each attribue
            kwargs: Assigns Key/value argument attribute
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """The overloading method"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def to_dictionary(self):
        Rectangle = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return Rectangle
