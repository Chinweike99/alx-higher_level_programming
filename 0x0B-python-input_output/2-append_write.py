#!/usr/bin/python3

"""a function appends a string at the end of a text
file (UTF8) and returns the number of characters added:"""


def append_write(filename="", text=""):
    """appends the specified text to file"""
    with open(filename, 'a', encoding="utf-8") as myfile:
        data_written = myfile.write(text)
    return data_written
