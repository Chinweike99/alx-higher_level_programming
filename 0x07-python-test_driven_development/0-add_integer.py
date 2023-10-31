#!/usr/bin/python3
"""A script taht adds two integers"""

def add_integer(a, b=98):
    """A Function that adds two integers
    Args:
        a: The first integer
        b: The second integer
    Return:
        Sum of a + b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return a + b
