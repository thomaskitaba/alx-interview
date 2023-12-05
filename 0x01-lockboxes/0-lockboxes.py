def canUnlockAll(boxes):
    """
    Check if all boxes can be opened
    """
    if not boxes or not isinstance(boxes, list):
        return False

    numberOfRoom = len(boxes)
    pocket = [0]  # Start with the key to room 0
    key_count = -1  # Variable to track the number of keys in the pocket

    while numberOfRoom >= 0:
        key_count = len(pocket)  # Record the current number of keys
        for ky, row in enumerate(boxes):
            if ky in pocket:  # Check if the key to the room is in the pocket
                for key in boxes[ky]:  # Collect keys in the room
                    if key not in pocket and key <= len(boxes):
                        pocket.append(key)  # Add new keys to the pocket
            numberOfRoom -= 1  # Move to the next room

    return len(pocket) == len(boxes)  # Return True if all rooms can be opened
