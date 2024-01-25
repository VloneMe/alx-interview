#!/usr/bin/python3
"""
Log parsing script.

This script reads log data from standard input, extracts information such as
HTTP status codes and file sizes, and then prints statistics based on the parsed data.
"""

import sys

def print_stats(statistics: dict, total_size: int) -> None:
    """
    Print total file size and HTTP status code statistics.

    Args:
    - statistics (dict): Dictionary containing HTTP status codes and their counts.
    - total_size (int): Total file size.

    Returns:
    - None
    """
    print("Total file size: {:d}".format(total_size))
    for code, count in sorted(statistics.items()):
        if count:
            print("{}: {}".format(code, count))

if __name__ == '__main__':
    # Initialization
    total_size, line_count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_statistics = {code: 0 for code in status_codes}

    try:
        # Reading log data line by line
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            
            try:
                # Extracting status code and updating status statistics
                code = data[-2]
                if code in status_statistics:
                    status_statistics[code] += 1
            except IndexError:
                # Handling IndexErrors, e.g., if the line doesn't have enough elements
                pass
            
            try:
                # Extracting file size and updating total file size
                total_size += int(data[-1])
            except (IndexError, ValueError):
                # Handling IndexErrors (if line doesn't have enough elements) and ValueErrors (if file size is not an integer)
                pass
            
            # Printing stats every 10 lines
            if line_count % 10 == 0:
                print_stats(status_statistics, total_size)
        
        # Printing final stats
        print_stats(status_statistics, total_size)

    except KeyboardInterrupt:
        # Handling KeyboardInterrupt to print stats before raising the exception
        print_stats(status_statistics, total_size)
        raise
