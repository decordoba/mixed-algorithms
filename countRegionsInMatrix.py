#!/usr/bin/env python2

"""
I had to face a similar challenge in an interview, and then I found it again in HackerRank.
Given an nxm matrix, with zeros and ones, count the number of ones in the largest
region in the matrix, where a region is a group of adjacent ones (also diagonally).
In this example, I count the number of regions and also return the number of ones it
the largest region.
Example:
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 1
Result: 2 regions, one with only a one (X below), the other with 6 ones (Y below)
Y Y 0 0
0 Y Y 0
0 0 Y 0
X 0 0 Y
"""

import Queue
from basic import *  # Find basic.py in https://github.com/decordoba/basic-python

# Matrix that considers the diagonal cells adjacent
ADJACENT_MATRIX = [(-1, -1), (-1, 0), (-1, 1),
                   (0,  -1),          (0,  1),
                   (1,  -1), (1,  0), (1,  1)]

# Matrix that only considers the cells adjacent horizontally or vertically
# ADJACENT_MATRIX =           [(-1, 0),
#                    (0,  -1),          (0,  1),
#                              (1,  0)]


def countRegions(grid):
    w = len(grid)     # Width table
    h = len(grid[0])  # Height table
    ht = set()        # Hash table
    max_region = 0    # Keeps track of largest region
    num_regions = 0   # Counts regions
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            # We have found a new cell
            if cell == 1 and (i, j) not in ht:
                # Update num_regions
                num_regions += 1
                region = 0  # Counter for number of cells in region
                ht.add((i, j))
                q = Queue.Queue()
                q.put((i, j))
                # We visit and add to ht all the cells in the region
                while not q.empty():
                    region += 1
                    i0, j0 = q.get()
                    for adj_i, adj_j in ADJACENT_MATRIX:
                        ii = i0 + adj_i
                        jj = j0 + adj_j
                        if ii < w and ii >= 0 and jj < h and jj >= 0:
                            if grid[ii][jj] == 1 and (ii, jj) not in ht:
                                ht.add((ii, jj))
                                q.put((ii, jj))
                # Update max_region
                max_region = max(region, max_region)
    return max_region, num_regions


if __name__ == "__main__":
    default = """1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 1"""
    input = readFileArgument(input=default, print_input=True)
    grid = parseString(input, type="int")
    max_region, num_regions = countRegions(grid)
    print("Number of regions: {}\nLargest region:    {}".format(num_regions, max_region))
