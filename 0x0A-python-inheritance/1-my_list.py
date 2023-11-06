#!/usr/bin/python3
"""A script that inherits a list Class"""

class MyList(list):
    """A class MYList that inherits from a list"""

    def print_sorted(self):
        #original_list = self.copy()
        """Function that prints the list, but sorted (ascending sort)
            Assuming all the elements of the list is type int
        """
        # Sort the list in ascending order without using any modules
        sorted_list = []
        for i in range(len(self) - 1):
            for j in range(i + 1, len(self)):
                if self[i] > self[j]:
                   self[i], self[j] = self[j], self[i]

        for element in self:
            sorted_list.append(element)

        print(sorted_list)
