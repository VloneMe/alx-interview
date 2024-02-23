#!/usr/bin/python3

"""This script provides a function to rotate a 2D matrix in-place."""


def rotate_2d_matrix(m):
    """Rotate a 2D matrix in-place.

    Args:
        m (list of lists): The 2D matrix to rotate.

    Returns:
        None. The rotation is done in-place.
    """
    """Rotate the given 2D matrix in-place."""
    n = len(m)  # Calculate the size of the matrix
    temp1, temp2 = 0, 0  # Initialize temporary variables for swapping

    for j in range(0, len(m) // 2 + 1):
        # Iterate through the layers of the matrix
        for i in range(j, n - 1):
            # Iterate through elements in the current layer
            """Swap elements to perform the rotation."""
            temp1 = m[i][n - 1]
            m[i][n - 1] = m[j][i]
            temp2 = m[n - 1][n - 1 - i + j]
            m[n - 1][n - 1 - i + j] = temp1
            temp1 = m[n - 1 - i + j][j]
            m[n - 1 - i + j][j] = temp2
            m[j][i] = temp1
        n -= 1  # Decrease the size of the matrix for next layer rotation
