#!/usr/bin/python3
def search_replace(my_list, search, replace):
    updatedList = []

    for element in my_list:
        if element == search:
            updatedList.append(replace)
        else:
            updatedList.append(element)

    return updatedList
