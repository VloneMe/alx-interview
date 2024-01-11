#!/usr/bin/python3

def canUnlockAll(boxes):
    # Set to keep track of opened boxes
    opened_boxes = set()

    # Initially, the first box is unlocked
    opened_boxes.add(0)

    # Queue to keep track of boxes to explore
    queue = [0]

    # BFS traversal to unlock boxes
    while queue:
        current_box = queue.pop(0)

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a new box and that box is not already opened
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                queue.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)

# Example usage:
boxes_example = [[1], [2], [3], []]
result = canUnlockAll(boxes_example)
print(result)
