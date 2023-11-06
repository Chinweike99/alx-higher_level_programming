#!/usr/bin/python3
"""Script for Same class or inherit from"""

def is_kind_of_class(obj, a_class):
    """Function to check if the object is instance of a class
    Return:
        True - If the object is an instance of a class that inherited from
        False - If otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
