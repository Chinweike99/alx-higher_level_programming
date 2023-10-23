#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printedIntegers = 0
    try:
        for item in my_list:
            try:
                print("{:d}".format(item), end="")
                printedIntegers += 1
            except (ValueError, TypeError):
                continue

            if printedIntegers >= x:
                break

        print()
        return printedIntegers

    except IndexError:
        raise Exception("x is greater than the length of my_list")
