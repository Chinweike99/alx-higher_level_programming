#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix_simple = []

    for row in matrix:
        squaredRow = []
        for element in row:
            squaredRow.append(element ** 2)

        square_matrix_simple.append(squaredRow)
    return square_matrix_simple
