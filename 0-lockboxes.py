#!/usr/bin/python3
def canUnlockAll(boxes):
    boxSize = len(boxes)
    opened = 1
    for count, row in enumerate(boxes):
        idx = count + 1
        if count <= boxSize - 2:
            if idx in row:
                opened += 1
                # print(f"idx {idx} | count {count} | row {row} | opened {opened}")

    if opened == boxSize:
        return True
    else:
        return False
