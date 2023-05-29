#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    current_matrix = matrix.copy()

    for index in range(len(matrix)):
        current_matrix[index] = list(map(lambda x: x**2, matrix[index]))

    return (current_matrix)
