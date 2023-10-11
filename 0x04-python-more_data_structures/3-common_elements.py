#!/usr/bin/python3
def common_elements(set1, set2):
    mySet = set()

    for element in set1:
        if element in set2:
            mySet.add(element)
    return mySet
