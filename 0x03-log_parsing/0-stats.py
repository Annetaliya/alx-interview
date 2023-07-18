#!/usr/bin/python3

import sys
import signal

def print_statistics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    def signal_handler(sig, frame):
        print_statistics(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) != 10:
                continue

            try:
                file_size = int(parts[9])
                status_code = int(parts[7])
            except ValueError:
                continue

            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()

