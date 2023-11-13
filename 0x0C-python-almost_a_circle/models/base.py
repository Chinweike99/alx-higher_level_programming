#!/usr/bin/python3
"""Base Module"""
import json

class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A function that returns the JSON string representattation of list_dictionaries
        Args:
            list_dictionaries: A list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class Method that writes the JSON string representation of list_objs"""
        json_list = []
        json_string = '[]'
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
            if len(json_list) > 0:
                json_string = cls.to_json_string(json_list)

        with open(cls.__name__+ '.json', 'w') as f:
            f.write(json_string)
