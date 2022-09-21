#!/usr/bin/python3
"""define matrix mltplication function."""


def matrix_mul(m_a, m_b):
    """Returns the multplication of two matrix"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a is None or len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if m_b is None or len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    sum_t = 0
    raw = []
    new_matrix = []
    for k in range(len(m_a)):
        for i in range(len(m_b[0])):
            for j in range(len(m_a[0])):

                if not isinstance(m_a[k], list):
                    raise TypeError("m_a must be a list of lists")
                if not isinstance(m_b[j], list):
                    raise TypeError("m_b must be a list of lists")
                if (not isinstance(m_a[k][j], int) and
                        not isinstance(m_a[k][j], float)):
                    raise TypeError("m_a should contain only integers or floats")
                if (not isinstance(m_b[j][i], int) and
                        not isinstance(m_b[j][i], float)):
                    raise TypeError('m_b should contain only integers or floats')
                if len(m_a[k]) != len(m_a[0]):
                    raise TypeError('each row of m_a must be of the same size')
                if len(m_b[j]) != len(m_b[0]):
                    raise TypeError('each row of m_b must be of the same size')
                sum_t += m_a[k][j] * m_b[j][i]
            raw.append(sum_t)
            sum_t = 0
        new_matrix.append(raw)
        raw = []
    return (new_matrix)
