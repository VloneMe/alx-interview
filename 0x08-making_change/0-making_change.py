#!/usr/bin/python3
"""Make change challenge"""


def make_change(coins, total):
    """
    Calculate the minimum number of coins needed to reach a total.

    Args:
        coins (list): List of available coin denominations.
        total (int): Total amount needed.

    Returns:
        int: Minimum number of coins needed to reach total,
        or -1 if not possible.
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    sum = 0
    i = 0
    counter = 0
    num_coins = len(coins)

    while sum < total and i < num_coins:
        while coins[i] <= total - sum:
            sum += coins[i]
            counter += 1
            if sum == total:
                return counter
        i += 1

    return -1
