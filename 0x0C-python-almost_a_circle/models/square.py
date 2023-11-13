#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square Class that inherits fro Rectangle"""

    def __init__(self, size, x = 0, y = 0, id = None):
        """class constructor
        Args:
            size: either the width or height
            x (int): x-coordinate
            y (int): y -coordinate
            id (int): class id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square class
        Args:
            args: No key-worded arguments
            kwargs: kew=y - worded arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle"""
        square = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
        return square

    def __str__(self):
        """overloading method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
