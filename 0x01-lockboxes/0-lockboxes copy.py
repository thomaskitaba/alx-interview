#!/usr/bin/python3
""" you have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """ check if all boxes can be opened """
    if not boxes or not isinstance(boxes, list):
        return False

    boxSize = len(boxes)
    opened = 1
    for count, row in enumerate(boxes):
        idx = count + 1
        if count <= boxSize - 2:
            if idx in row:
                opened += 1
            # else:
            #     for key in row:
            #         if idx in boxes[key]:
            #             opened += 1

    if opened == boxSize:
        return True
    else:
        return False
