#!/usr/bin/python3
"""
you have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened
    """
    if not boxes or not isinstance(boxes, list):
        return False

    pocket = [0]
    key_count = -100
    while len(pocket) != key_count:
        # move one step and if you have key enter the room
        # then collect the keys in the room and put it in your pocket
        # to enter the next room check if you have the key in your pocket
        key_count = len(pocket)
        for ky, row in enumerate(boxes):
            # check if i have the ky in my pocket
            if ky in pocket:
                # collect keys
                for key in boxes[ky]:
                    if key not in pocket and key < len(boxes):
                        pocket.append(key)

    return len(pocket) == len(boxes)
    