#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle up
    to the nth row, excluding the first row.
    Returns an empty list if n <= 0.
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(triangle[i - 1]) - 1):
            curr = triangle[i - 1]
            temp.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
