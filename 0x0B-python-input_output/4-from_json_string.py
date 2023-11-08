#!/usr/bin/python3

"""a function that returns an object from
the JSON representation of the object (string):"""
import json


def from_json_string(my_str):
    """returns the object from its json representation of the string"""
    return json.loads(my_str)
