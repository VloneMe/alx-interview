#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle up to the nth row.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize Pascal's Triangle with the first row

    for i in range(1, n):
        row = [1]
        for j in range(len(triangle[i - 1]) - 1):
            row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        row.append(1)
        triangle.append(row)

    return triangle

# Example usage:
result = pascal_triangle(5)
print(result)
