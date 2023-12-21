#!/usr/bin/python3

import sys


def print_msg(statusCode, total_file_size):
    """
    Method to print
    Args:
        statusCode: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(statusCode.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
count = 0
statusCode = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            count += 1

            if count <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in statusCode.keys()):
                    statusCode[code] += 1

            if (count == 10):
                print_msg(statusCode, total_file_size)
                count = 0
finally:
    print_msg(statusCode, total_file_size)
