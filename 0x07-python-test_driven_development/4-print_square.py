#!/usr/bin/python3
"""A script that prints a square"""

def print_square(size):
    """Prints a square with the character '#'
    size:
        The size of the length of the square
    Raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print('#' * size)
