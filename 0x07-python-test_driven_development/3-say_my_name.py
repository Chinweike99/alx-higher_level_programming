#!/usr/bin/python
""""A Script that prints name"""
def say_my_name(first_name, last_name=""):
    """Print a message with the first name and last name
    Args:
        first_name: A string representing the first name
        last_name: A string representing the last name
    Raises:
        TypeError: if first_name or last_name is not string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
