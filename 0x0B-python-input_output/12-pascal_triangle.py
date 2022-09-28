#!/usr/bin/python3
"""Defines...."""

def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n."""
    a = []
    h = 0
    for i in range(n):
        b = [1]
        if i >= 1:
            for j in range(i):
                for k in range(j, i):
                    h += a[k][j]
                b.append(h)
                h = 0
        a.append(b)
    return a
