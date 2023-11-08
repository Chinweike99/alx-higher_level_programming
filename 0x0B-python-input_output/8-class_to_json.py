#!/usr/bin/python3
""" A function that returns the dictionary description with a simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an object """

    return_dict = {}
    if hasattr(obj, "__dict__"):
        return_dict = obj.__dict__.copy()
    return return_dict
