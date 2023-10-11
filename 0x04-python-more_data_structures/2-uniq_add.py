#!/usr/bin/python3
def uniq_add(my_list=[]):
    mySet = set()
    total = 0
    for element in my_list:
        if element not in mySet:
            total += element
            mySet.add(element)
    return total
