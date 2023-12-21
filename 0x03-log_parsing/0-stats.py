#!/usr/bin/python3
""" log parsing """
import sys


def parse_log():
    count = 0
    parsed = []
    fileSize = 0
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
            parsed = line.split()
            count += 1
            fileSize += int(parsed[-1])
            code = parsed[-2]
            if code in statusCode:
                statusCode[code] += 1
            if count % 10 == 0:
                print(f"File size : {fileSize}")
                for key, value in statusCode.items():
                    print(f"{key}: {value}")
    except KeyboardInterrupt:
        print(f"File size : {fileSize}")
        for key, value in statusCode.items():
            print(f"{key}: {value}")
        return


if __name__ == "__main__":
    parse_log()
