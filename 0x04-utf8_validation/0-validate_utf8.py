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
    """ Number of bytes in the current UTF-8 character """
    num_bytes = 0

    for num in data:
        # Check if it's the start of a new character
        if num_bytes == 0:
            # Count the number of bytes in this character
            if (num >> 5) == 0b110:
                num_bytes = 2
            elif (num >> 4) == 0b1110:
                num_bytes = 3
            elif (num >> 3) == 0b11110:
                num_bytes = 4
            # If it's a single byte character, move to the next integer
            elif (num >> 7) != 0:
                return False
        else:
            # If the current byte doesn't start with 10, it's invalid
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

        return True