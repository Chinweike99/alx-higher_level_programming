#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []  # This list will store the division results

    for i in range(list_length):
        try:
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]
            if not (isinstance(value_1, (int, float)) and isinstance(value_2, (int, float))):
                print("wrong type")
                result.append(0)
                continue
            if value_2 == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(value_1 / value_2)
        except IndexError:
            print("out of range")
            result.append(0)

    return result
