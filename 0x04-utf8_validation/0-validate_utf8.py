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
    """determines if a given data set represents a valid UTF-8 encoding"""
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
