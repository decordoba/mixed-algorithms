#!/usr/bin/env python2

import math
from basic import *  # Find basic.py in https://github.com/decordoba/basic-python

"""
I had to face this challenge in one of my interviews.
We get 3 2D point that make a triangle ABC (ax, ay, bx, by, cx, cy). We also get another point P
(px, py) and have to return True if the point is inside the triangle and False if it is not or if
the triangle is impossible.

Examples:
isPointInTrinagle(0,0,1,1,0,1,1,1) --> False
isPointInTrinagle(0,5,4,0,5,6,2,1) --> False
isPointInTrinagle(0,5,4,0,5,6,2,3) --> True
"""

def isPointInTrinagle(ax, ay, bx, by, cx, cy, px, py):
    """
    Returns True if a point P is inside a triangle ABC, and False otherwise
    Expects a correct triangle (A+B>C, C+A>B, B+C>A)
    """
    pointOutside = False
    pointOutside |= isPointOutsideTriangle(ax, ay, bx, by, cx, cy, px, py)
    pointOutside |= isPointOutsideTriangle(bx, by, cx, cy, ax, ay, px, py)
    pointOutside |= isPointOutsideTriangle(cx, cy, ax, ay, bx, by, px, py)
    return not pointOutside

def isPointOutsideTriangle(ax, ay, bx, by, cx, cy, px, py):
    """
    Returns True if a point P is outside a triangle ABC by calculating the AB line (y=mx+n) and
    checking if C and P are at different sides of such line. If False is returned does not mean
    that the point is inside the triangle, we would have to check this for all three pairs AB,
    BC, CA. If True is returned, P is definitely outside ABC.
    """
    # We avoid dividing by a negative number. Here AB is a vertical line so we only compare x's
    if ax - bx == 0:
        if px == ax:
            return False
        if (px < ax and cx > ax) or (px > ax and cx < ax):
            return True
        return False
    # Calculate line AB: y=mx+n
    m = (ay - by) / (ax - bx)
    n = ay - m * ax
    # Find y coordinate of px and cs with line AB
    exact_cy = m * cx + n
    exact_py = m * px + n
    # P is in the line AB
    if exact_py == py:
        return False
    # The triangle is a line, because C is in the line AB
    if exact_cy == cy:
        return True
    # P is definitely outside the triangle ABC
    if (exact_py < py and exact_cy > cy) or (exact_py > py and exact_cy < cy):
        return True
    # P is might be inside or outside the triangle ABC (see above explanation)
    return False

def getDistance(p0x, p0y, p1x, p1y):
    """
    Gets the distance between two points
    """
    return math.sqrt((p0x - p1x)**2 + (p0y - p1y)**2)

def isTriangle(ax, ay, bx, by, cx, cy):
    """
    Checks if triangle ABC is a triangle or not. Therefore, (A+B>C, C+A>B, B+C>A).
    For example, a=(0,0), b=(0,2), c=(0,4) is not a triangle
    """
    ab = getDistance(ax, ay, bx, by)
    bc = getDistance(bx, by, cx, cy)
    ca = getDistance(cx, cy, ax, ay)
    return ab + bc > ca and ab + ca > bc and ca + bc > ab


if __name__ == "__main__":
    (ax, ay) = (0, 2)
    (bx, by) = (2, 4)
    (cx, cy) = (4, 0)
    (px, py) = (2, 2)

    args = readInputArguments(input="")
    if len(args) > 0:
        ax, ay, bx, by, cx, cy, px, py = parseString(args, "int")[0]
        print "Using input: A={}, B={}, C={}, P={}".format((ax, ay), (bx, by), (cx, cy), (px, py))
    else:
        print "Usage: python {} AX AY BX BY CX CY PX PY".format(sys.argv[0])
        print "No input arguments. Using default input: A={}, B={}, C={}, P={}".format((ax, ay),
                                                                                       (bx, by),
                                                                                       (cx, cy),
                                                                                       (px, py))

    if not isTriangle(ax, ay, bx, by, cx, cy):
        print "[{}, {}, {}] is not a triangle".format((ax, ay), (bx, by), (cx, cy))
    else:
        if isPointInTrinagle(ax, ay, bx, by, cx, cy, px, py):
            print "{} is inside the triangle [{}, {}, {}]".format((px, py), (ax, ay),
                                                                  (bx, by), (cx, cy))
        else:
            print "{} is NOT inside the triangle [{}, {}, {}]".format((px, py), (ax, ay),
                                                                      (bx, by), (cx, cy))
