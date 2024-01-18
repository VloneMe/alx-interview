#!/usr/bin/python3
"""
 Minimum Operations
"""


def minOperations(n):
    """
    Method for compute the minimum number
    of operations for task Copy All and Paste

    Args:
        n: input value
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    op_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                op_list.append(i)
    return sum(op_list)
