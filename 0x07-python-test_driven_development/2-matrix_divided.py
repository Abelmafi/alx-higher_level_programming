#!/usr/bin/python3
""" Define matrix divider functions."""


def matrix_divided(matrix, div):
    """Returns new matrix which is the division of matrix by div."""
    
    new_matrix = []
    if (not isinstance(div, int)) and (not isinstance(div, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for i in range(len(matrix)):
        a = []
        if not isinstance(matrix[i], list):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(matrix[i]) != len(matrix[0]):
                raise TypeError('Each row of the matrix must have the same size')
        for j in range(len(matrix[i])):
            if (not isinstance(j, int)) and (not isinstance(j, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            a.append(round(matrix[i][j] / div, 2))
        new_matrix.append(a)
    return (new_matrix)
