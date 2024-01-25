#!/usr/bin/python3

import sys
import signal

# Define the status codes to track
STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}

# Initialize variables for metrics
total_file_size = 0
status_code_counts = {code: 0 for code in STATUS_CODES}
lines_processed = 0

def print_statistics():
    """
    Print statistics based on the metrics collected.
    """
    print(f"Total file size: {total_file_size}")
    for code in sorted(STATUS_CODES):
        count = status_code_counts.get(code, 0)
        if count > 0:
            print(f"{code}: {count}")

def process_line(line):
    """
    Process a single line and update metrics.
    """
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        global total_file_size, lines_processed
        total_file_size += file_size
        lines_processed += 1

        if status_code in STATUS_CODES:
            status_code_counts[status_code] += 1

    except (ValueError, IndexError):
        # Skip lines that do not match the specified format
        pass
