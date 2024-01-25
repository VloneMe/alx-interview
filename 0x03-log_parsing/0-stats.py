#!/usr/bin/python3
"""
Log Parsing Script

This script reads log data from stdin, parses it, and computes metrics such as total file size
and the number of occurrences for specific status codes. Metrics are printed after every 10 lines
or when the script is interrupted by a keyboard signal (CTRL + C).
"""

import sys

if __name__ == '__main__':
    total_file_size, line_count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_code_counts = {code: 0 for code in status_codes}

    def print_statistics(stats: dict, file_size: int) -> None:
        """
        Print computed statistics.

        Args:
            stats (dict): Dictionary containing status code counts.
            file_size (int): Total file size.
        """
        print(f"Total File Size: {file_size}")
        for code, count in sorted(stats.items()):
            if count:
                print(f"{code}: {count}")

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            
            try:
                status_code = data[-2]
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except IndexError:
                pass

            try:
                total_file_size += int(data[-1])
            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_statistics(status_code_counts, total_file_size)
        
        print_statistics(status_code_counts, total_file_size)

    except KeyboardInterrupt:
        print_statistics(status_code_counts, total_file_size)
        raise
