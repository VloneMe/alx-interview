#!/usr/bin/python3

"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be unlocked using their keys.
    
    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    """# Ensure the input is a list """
    if not isinstance(boxes, list):
        return False

    """# Ensure the list is not empty """
    elif not boxes:
        return False

    """# Iterate over the keys """
    for key in range(1, len(boxes) - 1):
        box_checked = False

        """# Check if the key corresponds to a box and is not the same as the box index """
        for idx in range(len(boxes)):
            box_checked = key in boxes[idx] and key != idx
            if box_checked:
                break

        """# If a box couldn't be opened with the current key, return False """
        if not box_checked:
            return box_checked

    """# If all boxes can be opened, return True """
    return True
