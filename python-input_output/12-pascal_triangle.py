#!/usr/bin/python3
"""comment"""


def pascal_triangle(n):
    """Return Pascal's triangle of n rows."""
    if n <= 0:
        return []

    triangle = [[1]]

    for row_num in range(1, n):
        prev_row = triangle[row_num - 1]
        row = [1]

        for i in range(1, row_num):
            row.append(prev_row[i - 1] + prev_row[i])

        row.append(1)
        triangle.append(row)

    return triangle
