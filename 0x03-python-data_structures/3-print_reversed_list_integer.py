#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    return my_list[::-1]

my_list = [1, 2, 3, 4, 5]
reversed_list = print_reversed_list_integer(my_list)
for i in reversed_list:
    print("{:d}".format(i))
