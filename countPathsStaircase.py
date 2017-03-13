#!/usr/bin/env python2

"""
I found this code in HackerRank and found it really interesting. Tricky but so simple.
https://www.hackerrank.com/challenges/ctci-recursive-staircase
From a staircase with a number of steps, and knowing we can walk up only a certain
number of steps at a time, return how many different combinations of steps can be
performed to reach the end of the staircase.

Examples:
count_paths_staircase(3, [1, 2, 3]) --> 4: (1,1,1), (1,2), (2,1), (3)
count_paths_staircase(7, [2, 3]) --> 3: (2,2,3), (2,3,2), (3,2,2)
"""

from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def count_paths_staircase(length_staircase, possible_actions):
    """
    In a staircase of length_staircase steps, we can walk up possible_actions steps
    at one time, return how many different combinations of steps can be performed
    to reach each of the steps in the staircase starting from the bottom
    """
    path = [0] * length_staircase
    # First we add our possible_actions to our path count
    for i in possible_actions:
        path[i - 1] = 1
    # Compute number of path combinations to every step
    for i in range(length_staircase):
        for j in possible_actions:
            k = i + j
            if k >= length_staircase:
                continue
            path[k] += path[i]
    return path


if __name__ == "__main__":
    default = \
"""1 2 3
1
3
7
12"""
    input = readFileArgument(input=default)
    grid = parseString(input, type="int")
    print "Input:"
    print input
    
    allowed_actions = grid[0]
    list_staircases = grid[1:]
    longest_staircase = max(list_staircases)[0]
    
    print "\nOutput:"
    paths = count_paths_staircase(longest_staircase, allowed_actions)
    for i in list_staircases:
        print paths[i[0] - 1]