#!/usr/bin/python3

"""a function that returns the JSON
representation of an object (string):"""
import json


def to_json_string(my_obj):
    """returns the json representation of the string object"""
    return json.dumps(my_obj)
