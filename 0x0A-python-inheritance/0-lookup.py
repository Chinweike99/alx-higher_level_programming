#!/usr/bin/python3
"""A script that returns a list"""

def lookup(obj):
    """A function that returns the list of available attributes
        and method of an object.
    Args:
        obj - Object of the class

    Return:
        a list object
    """
    list = dir(obj)
    return list
