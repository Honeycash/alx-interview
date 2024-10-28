#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re
import sys
"""
Task 0. Log parsing
A script that reads stdin line by line and computes metrics.
"""

def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info
import sys


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)
def printStats(file_size, status):
    """printStats
    This function takes the total file size and the
    statues that were called and prints them.
def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.
    Arguments:
        file_size (int): The total file size to be printed.
        status (dict{int, int}): A dictionary of the statues that were called.
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status.items()):
        if value != 0:
            print("{}: {}".format(key, value))

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']
total_file_size = 0
count = 0
possible_status = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}
try:
    for line in sys.stdin:
        args = line.split()

        status_code = int(args[-2])
        file_size = int(args[-1])

def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        for line in sys.stdin():
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)
        if status_code in possible_status:
            possible_status[status_code] += 1

        total_file_size += file_size
        count += 1

if __name__ == '__main__':
    run()
        if count == 10:
            printStats(total_file_size, possible_status)
            count = 0
    printStats(total_file_size, possible_status)
except KeyboardInterrupt:
    raise
finally:
    printStats(total_file_size, possible_status)
