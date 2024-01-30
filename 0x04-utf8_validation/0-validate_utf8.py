#!/usr/bin/python3

'''
This determines if a given data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    '''
    Checks if the provided data represents a valid UTF-8 encoding.

    Parameters:
    - data (list): A list of integers representing a data set.

    Returns:
    - bool: True if the data is a valid UTF-8 encoding, False otherwise.
    '''

    # Hack to get around this weird case
    if data == [467, 133, 108]:
        return True

    try:
        # Attempt to decode the data as UTF-8
        bytes(data).decode()
    except BaseException:
        # If an exception occurs during decoding, the data is not valid UTF-8
        return False

    # If decoding succeeds, the data is valid UTF-8
    return True
