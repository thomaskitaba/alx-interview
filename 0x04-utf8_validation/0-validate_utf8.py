#!/usr/bin/python3
"""
  UTF-8 encoding rules:
  - If it matches 0b110 in the 5 most significant bits,
  it's the start of a 2-byte character.
  - If it matches 0b1110 in the 4 most significant bits,
  - it's the start of a 3-byte character.
  If it matches 0b11110 in the 3 most significant bits
  , it's the start of a 4-byte character.
  - If it doesn't match any of these patterns and doesn't
  start with a 0,
  - indicating a single-byte character, it's considered
  invalid.
"""


def validUTF8(data):
    dataLength = len(data)
    num_bytes = 0
    for num in data:

        if num_bytes == 0:
            if (num >> 5) == 0b110:
                num_bytes = 2
                if (num_bytes != dataLength):
                    return False
            elif (num >> 4) == 0b1110:
                num_bytes = 3
                if (num_bytes != dataLength):
                    return False
            elif (num >> 3) == 0b11110:
                num_bytes = 4
                if (num_bytes != dataLength):
                    return False
            elif (num >> 7) != 0:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1
    return True
