#!/usr/bin/python3
"""
Log parsing script.

This script reads log data from standard input, extracts information such as
HTTP status codes and file sizes, and then
prints statistics based on the parsed data.
"""

import sys


def print_stats(stats: dict, file_size: int) -> None:
    """
    Print file size and HTTP status code statistics.

    Args:
    - stats (dict): Dictionary containing HTTP status codes and their counts.
    - file_size (int): Total file size.

    Returns:
    - None
    """
    print("File size: {:d}".format(file_size))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


if __name__ == '__main__':
    # Initialization
    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    try:
        # Reading log data line by line
        for line in sys.stdin:
            count += 1
            data = line.split()

            try:
                # Extracting status code and updating stats
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                # Handling IndexErrors, e.g.,
                # if the line doesn't have enough elements
                pass

            try:
                # Extracting file size and updating total file size
                filesize += int(data[-1])
            except (IndexError, ValueError):
                # Handling IndexErrors
                # (if line doesn't have enough elements) and
                # ValueErrors (if file size is not an integer)
                pass

            # Printing stats every 10 lines
            if count % 10 == 0:
                print_stats(stats, filesize)

        # Printing final stats
        print_stats(stats, filesize)

    except KeyboardInterrupt:
        # Handling KeyboardInterrupt to print stats
        # before raising the exception
        print_stats(stats, filesize)
        raise
