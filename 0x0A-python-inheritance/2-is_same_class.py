#!/usr/bin/python3
"""Script that checks for Exact Same Object"""
def is_same_class(obj, a_class):
    """A Function that returns True if object is exactly an instance
    of the specified class; otherwise False
    """
    return type(obj) is a_class
