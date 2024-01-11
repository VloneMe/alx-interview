#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and may contain keys to other boxes.
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
    if type(boxes) is not list:
        return False

    elif (len(boxes)) == 0:
        return False

    for key in range(1, len(boxes) - 1):
        boxes_checeyed = False

        for idx in range(len(boxes)):
            boxes_checked = key in boxes[idx] and key != idx

            if boxes_checked:
                break

        if boxes_checked is False:
            return boxes_checked
            
    return True
