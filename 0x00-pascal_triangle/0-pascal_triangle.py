#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing Pascal's Triangle with n rows,
    or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        temp_row = [1]
        for j in range(len(triangle[i - 1]) - 1):
            temp_row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        temp_row.append(1)
        triangle.append(temp_row)

    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
print(result)
