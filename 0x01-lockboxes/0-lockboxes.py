#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be unlocked using their keys.
    
    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not isinstance(boxes, list):
        return False

    elif not boxes:
        return False

    for key in range(1, len(boxes) - 1):
        box_checked = False

        for idx in range(len(boxes)):
            box_checked = key in boxes[idx] and key != idx
            if box_checked:
                break

        if not box_checked:
            return box_checked

    return True
