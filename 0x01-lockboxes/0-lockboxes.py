def canUnlockAll(boxes):
    if not boxes or not isinstance(boxes, list):
        return False

    # Initializing a set to keep track of opened boxes
    opened_boxes = {0}

    # Initialize a variable to track the previous number of opened boxes
    prev_count = -1

    # Iterate until no new boxes can be opened
    while len(opened_boxes) != prev_count:
        prev_count = len(opened_boxes)
        for box in range(len(boxes)):
            if box in opened_boxes:
                for key in boxes[box]:
                    if key < len(boxes):
                        opened_boxes.add(key)

    # Check if all boxes can be opened
    return len(opened_boxes) == len(boxes)
