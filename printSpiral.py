#!/usr/bin/env python3.5

"""
Algorithm from a Google interview I did to get an internship there
"""


def print_spiral(m, clockwise=True):
    # Assume rectangular matrix
    w = len(m[0])  # Matrix width
    h = len(m)  # Matrix height
    depth = 0  # Current depth in the spiral
    x, y = 0, 0  # Initial position
    dire = 0  # Initial direction (Left)
    offset = 1  # Whether we add (clockwise) or substract (counter clockwise)
    if not clockwise:
        dire = 1  # Initial direction (Down)
        offset = -1  # Whether we add (clockwise) or substract (counter clockwise)

    r = []
    for i in range(w * h):
        r.append(str(m[y][x]))
        if dire % 4 == 0:  # Right
            x += 1
            if x + depth >= w: # Right edge case
                x -= 1
                y += offset
                dire += offset
        elif dire % 4 == 1:  # Down
            y += 1
            if y + depth >= h:  # Bottom edge case
                y -= 1
                x -= offset
                dire += offset
        elif dire % 4 == 2:  # Left
            x -= 1
            if x - depth < 0:  # Left edge case
                x += 1
                y -= offset
                dire += offset
                if clockwise:
                    depth += 1
        elif dire % 4 == 3:  # Up
            y -= 1
            if y - depth < 0:  # Top edge case
                y += 1
                x += offset
                dire += offset
                if not clockwise:
                    depth += 1
        # To prevent mods of negative numbers
        while dire <= 0:
            dire += 4
    print(" ".join(r))


if __name__ == "__main__":
    m = [[ 1, 2, 3, 4],
         [14,15,16, 5],
         [13,20,17, 6],
         [12,19,18, 7],
         [11,10, 9, 8]]

    print("Clockwise:         "),
    print_spiral(m, clockwise=True)
    print("Counter clockwise: "),
    print_spiral(m, clockwise=False)