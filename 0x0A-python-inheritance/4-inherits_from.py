#!/usr/bin/python3
"""Script for Same class or inherit from"""

def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited (directly or
        indirectly) from a specified class.
    Args:
        obj: The object to check
        a_class: the class to check against

    Return:
        True - If the object is an instance of a class that inherited from
        False - If otherwise
    """
    base_classes = obj.__class__.mro()
    return a_class in base_classes
