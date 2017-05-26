#!/usr/bin/env python2

"""
A decently difficult code in HackerRank that I took too long to solve.
https://www.hackerrank.com/challenges/two-pluses
The goal is to find, given a grid with spaces and walls, the position of
the two plus signs that can be drawn in the grid without crossing any wall,
whose product is maximized (where the product is defined as the product of
the number of cells that form both plus signs (see Example)).

Example:
Input: GG#BBGG  Maximum_Product: 9*5 = 45
       GG#BBGG
       #####@G
       GG#B@@@
       GG#BG@G
"""

from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def manhattan(pos0, pos1):
    return abs(pos0[0] - pos1[0]) + abs(pos0[1] - pos1[1])

def pluses_overlap(pos0, pos1, arm0, arm1):
    # Returns True if two pluses (defined by their center positions and their arm lengths) overlap,
    # False otherwise. This was the biggest challenge of the problem (for me)
    if manhattan(pos0, pos1) > arm0 + arm1:
        return False
    if pos0[0] == pos1[0] or pos0[1] == pos1[1]:
        return True
    diff_x = abs(pos0[0] - pos1[0])
    diff_y = abs(pos0[1] - pos1[1])
    min_arm = min(arm0, arm1)
    max_arm = max(arm0, arm1)
    if (diff_x <= min_arm and diff_y <= max_arm) or (diff_x <= max_arm and diff_y <= min_arm):
        return True
    return False
    
def pluses_product(arm1, arm2):
    # The goal of the problem is to find the 2 pluses that maximize their product
    return (4 * arm1 + 1) * (4 * arm2 + 1)

def print_grid(grid):
    # Print the grid in a human readable way
    w = len(grid[0].strip())
    print "/" + "-" * w + "\\"
    for row in grid:
        row = row.strip()
        if len(row) == 0:
            continue
        print "|" + row.replace("G", ".") + "|"
    print "\\" + "-" * w + "/"

def create_solution(grid, plus1, plus2, arm1, arm2, symbol1="#", symbol2="@"):
    # Given the grid and the two centres and arm lengths of two pluses, it returns
    # a grid with both pluses drawn using symbol1 and symbol2
    new_grid = [[cell for cell in row.strip()] for row in grid]
    new_grid[plus1[0]][plus1[1]] = symbol1
    for i in range(1, arm1 + 1):
        new_grid[plus1[0] + i][plus1[1]] = symbol1
        new_grid[plus1[0] - i][plus1[1]] = symbol1
        new_grid[plus1[0]][plus1[1] + i] = symbol1
        new_grid[plus1[0]][plus1[1] - i] = symbol1
    new_grid[plus2[0]][plus2[1]] = symbol2
    for i in range(1, arm2 + 1):
        new_grid[plus2[0] + i][plus2[1]] = symbol2
        new_grid[plus2[0] - i][plus2[1]] = symbol2
        new_grid[plus2[0]][plus2[1] + i] = symbol2
        new_grid[plus2[0]][plus2[1] - i] = symbol2
    for i, row in enumerate(new_grid):
        new_grid[i] = "".join(row)
    return new_grid

def extract_grid(input):
    # From input, extract grid, w and h
    input = input.split("\n")
    h, w = [int(x) for x in input[0].split()]
    grid = [row.strip() for row in input[1:]]
    return (w, h, grid)
    
def two_pluses(w, h, grid):
    # Solve the problem and print the solution
    print "GRID:"
    print_grid(grid)
    
    PLUS_MATRIX = [(-1, 0), (0,  -1), (0,  1), (1,  0)]  # pattern for a plus: one up, down, left and right
    max_arm = (min(w, h) - 1) // 2  # max possible plus arm size given the size of the grid
    pluses = [[] for i in range(max_arm + 1)]  # where we will save all the existing pluses in the grid
    
    # save all existing pluses in grid (including the 1-square 'plus')
    spaces = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "G":
                # available cell / space
                spaces += 1
                len_arm = 0
                isPlus = True
                while isPlus:
                    len_arm += 1
                    for offs in PLUS_MATRIX:
                        ii = i + len_arm*offs[0]
                        jj = j + len_arm*offs[1]
                        if ii < 0 or jj < 0 or ii >= h or jj >= w or grid[ii][jj] != "G":
                            len_arm -= 1
                            isPlus = False
                            break
                # if len_arm > 0:
                    # print_grid(create_solution(grid, (i, j), (i, j), len_arm, len_arm))
                while len_arm >= 0:
                    pluses[len_arm].append((i, j))
                    len_arm -= 1

    # find pluses with greater product
    max_plus = 0
    solution = ()
    for i, current_arm1 in enumerate(range(max_arm, -1, -1)):
        # check pluses with same arm length
        plus_value = pluses_product(current_arm1, current_arm1)
        if plus_value < max_plus:
            break
        pluses1 = pluses[current_arm1]
        max_plus_found = False
        for j in range(len(pluses1)):
            for k in range(j + 1, len(pluses1)):
                if not pluses_overlap(pluses1[j], pluses1[k], current_arm1, current_arm1):
                    max_plus = plus_value
                    solution = (pluses1[j], pluses1[k], current_arm1, current_arm1)
                    max_plus_found = True
                    # print_grid(create_solution(grid, pluses1[j], pluses1[k], current_arm1, current_arm1))
                    # raw_input()
                    break
            if max_plus_found:
                break
        # check pluses with different arm length
        if not max_plus_found:
            for current_arm2 in range(current_arm1 - 1, -1, -1):
                plus_value = pluses_product(current_arm1, current_arm2)
                if plus_value < max_plus:
                    break
                pluses2 = pluses[current_arm2]
                max_plus_found = False
                for j in range(len(pluses1)):
                    for k in range(len(pluses2)):
                        if not pluses_overlap(pluses1[j], pluses2[k], current_arm1, current_arm2):
                            max_plus = plus_value
                            solution = (pluses1[j], pluses2[k], current_arm1, current_arm2)
                            max_plus_found = True
                            # print_grid(create_solution(grid, pluses1[j], pluses2[k], current_arm1, current_arm2))
                            # raw_input()
                            break
                    if max_plus_found:
                        break
                if max_plus_found:
                    break

    print "SOLUTION:", max_plus
    print_grid(create_solution(grid, solution[0], solution[1], solution[2], solution[3]))
    print
    
if __name__ == "__main__":
    input = \
    """12 12
    GGGGGGGGGGGG
    GBGGBBBBBBBG
    GBGGBBBBBBBG
    GGGGGGGGGGGG
    GGGGGGGGGGGG
    GGGGGGGGGGGG
    GGGGGGGGGGGG
    GBGGBBBBBBBG
    GBGGBBBBBBBG
    GBGGBBBBBBBG
    GGGGGGGGGGGG
    GBGGBBBBBBBG"""
    (w, h, grid) = extract_grid(input)
    two_pluses(w, h, grid)
    
    input = \
    """12 14
    GGGGGGGGGGGGGG
    GGGGGGGGGGGGGG
    GGBGBGGGBGBGBG
    GGBGBGGGBGBGBG
    GGGGGGGGGGGGGG
    GGGGGGGGGGGGGG
    GGGGGGGGGGGGGG
    GGGGGGGGGGGGGG
    GGBGBGGGBGBGBG
    GGBGBGGGBGBGBG
    GGBGBGGGBGBGBG
    GGBGBGGGBGBGBG"""
    (w, h, grid) = extract_grid(input)
    two_pluses(w, h, grid)

    input = \
    """14 12
    GGGGGGGGGGGG
    GGGGGGGGGGGG
    BGBGGGBGBGBG
    BGBGGGBGBGBG
    GGGGGGGGGGGG
    GGGGGGGGGGGG
    GGGGGGGGGGGG
    GGGGGGGGGGGG
    BGBGGGBGBGBG
    BGBGGGBGBGBG
    BGBGGGBGBGBG
    BGBGGGBGBGBG
    GGGGGGGGGGGG
    GGGGGGGGGGGG"""
    (w, h, grid) = extract_grid(input)
    two_pluses(w, h, grid)