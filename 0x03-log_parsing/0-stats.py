#!/usr/bin/python3
""" Log Parsing """
import sys


def print_data(statusCode, fileSize):
    print(f"File size: {fileSize}")
    for key, value in sorted(statusCode.items()):
        if value != 0:
            print(f"{key}: {value}")


def parse_log():
    count = 0
    fileSize = 0
    statusCode = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    try:
        for line in sys.stdin:
            parsed = line.split()
            if len(parsed) >= 2: and parsed[-1].isdigit() and parsed[-2] in statusCode:
                count += 1
                fileSize += int(parsed[-1])
                statusCode[parsed[-2]] += 1

                if count % 10 == 0:
                    print_data(statusCode, fileSize)
                    count = 0
                    fileSize = 0
                    statusCode = {code: 0 for code in statusCode}
    finally:
        print_data(statusCode, fileSize)


if __name__ == "__main__":
    parse_log()
