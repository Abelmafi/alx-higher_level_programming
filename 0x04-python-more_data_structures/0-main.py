#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3, 5, 5],
    [4, 5, 6, 3, 7],
    [7, 8, 9, 6, 7]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
