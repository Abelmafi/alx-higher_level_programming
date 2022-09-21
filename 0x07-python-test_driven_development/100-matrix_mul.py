#!/usr/bin/python3
"""define matrix mltplication function."""


def matrix_mul(m_a, m_b):
    """Returns the multplication of two matrix"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a is None or m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not all(len(m_a[0]) == len(raw) for raw in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(m_b[0]) == len(raw) for raw in m_b):
        raise TypeError('each row of m_b must be of the same size')
    if m_b is None or m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")
    sum_t = 0
    raw = []
    new_matrix = []
    for k in range(len(m_a)):
        for i in range(len(m_b[0])):
            for j in range(len(m_a[0])):
                sum_t += m_a[k][j] * m_b[j][i]
            raw.append(sum_t)
            sum_t = 0
        new_matrix.append(raw)
        raw = []
    return (new_matrix)
