#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for x in range(len(matrix)):
            for i in range(len(matrix[x])):
                if i != len(matrix[x]) - 1:
                    end_space = ' '
                else:
                    end_space = ''
                print("{:d}".format(matrix[x][i]), end=end_space)
            print()
