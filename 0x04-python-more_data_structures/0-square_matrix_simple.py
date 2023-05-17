#!/bin/usr/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix by squaring each element in the input matrix
    new_matrix = [[x**2 for x in row] for row in matrix]

    return (new_matrix)
