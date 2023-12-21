#!/usr/bin/python3
""" Log Parsing """
import sys
def print_data(statusCode, fileSize):
    # sorted_status_code = sorted(statusCode.items(), key=lambda x: int(x[0]))
    print(f"File size : {fileSize}")
    for key, value in sorted(statusCode.items()):
        if value != 0:
          print(f"{key}: {value}")

def parse_log():
    count = 0
    parsed = []
    sorted_status_code = {}
    fileSize = 0
    statusCode = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    try:
        for line in sys.stdin:
            if line == "":
                continue
            count += 1
            parsed = line.split()
            if len(parsed) < 2:
                continue
            if not parsed[-1].isnumeric():
                continue
            if not parsed[-2].isnumeric():
                continue
            fileSize += int(parsed[-1])
            code = parsed[-2]
            if code in statusCode:
                statusCode[code] += 1
            if count % 10 == 0:
                print_data(statusCode, fileSize)

        if count % 10 != 0:
            print_data(statusCode, fileSize)
        elif count == 0:
            print(f"File size : {fileSize}")
    except KeyboardInterrupt:
        print_data(statusCode, fileSize)


if __name__ == "__main__":
    parse_log()
