#!/usr/bin/python3

import sys


def print_data(statusCode, fileSize):
    """
    log parsing
    """
    print(f"File size : {fileSize}")
    for key, value in sorted(statusCode.items()):
        if value != 0:
            print(f"{key}: {value}")

count = 0
parsed = []
sorted_status_code = {}
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
      if len(parsed) > 2:
          count += 1
          if count <= 10:
              fileSize += int(parsed[-1])
              code = parsed[-2]

              if code in statusCode.keys():
                  statusCode[code] += 1
          if count == 10:
              print_data(statusCode, fileSize)
              count = 0
finally:
  print_data(statusCode, fileSize)
