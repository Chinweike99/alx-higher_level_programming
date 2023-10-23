#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length  # Initialize the result list with zeros
    
    for i in range(list_length):
        try:
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]

            # Check if the elements are numbers (int or float)
            if not (isinstance(value_1, (int, float)) and isinstance(value_2, (int, float))):
                print("wrong type")
            else:
                # Check if the division can be done (no division by zero)
                if value_2 == 0:
                    print("division by 0")
                else:
                    result[i] = value_1 / value_2
        except IndexError:
            print("out of range")

        finally:
            pass
    return result
