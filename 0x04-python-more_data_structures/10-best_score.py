#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    Maximum = 0
    for key, value in a_dictionary.items():
        if value > Maximum:
            Maximum = value
    for key, value in a_dictionary.items():
        if value == Maximum:
            return key
