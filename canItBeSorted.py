#!/usr/bin/env python2

"""
Awesome algorithm from HackerRank, which allowed me to learn about the
meaning of Parity of Permutation: https://www.hackerrank.com/challenges/larrys-array
The goal is to find if it is possible to sort an array when the only operation
permitted is to rotate left three consecutive elements (ABC -> BCA -> CAB -> ABC).

Example:
Given 1 6 5 2 4 3 -> 1 5 2 6 4 3 -> 1 2 6 5 4 3 -> 1 2 5 4 6 3 -> 1 2 4 6 5 3 ->
-> 1 2 4 5 3 6 -> 1 2 4 3 6 5 -> 1 2 3 6 4 5 -> 1 2 3 6 4 5 -> 1 2 3 4 5 6 => YES

I started solving it just sorting them using the rotation method, but it is possible to
use Parity of Permutation to determine whether if it is sortable or not much faster.
See https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html for more.
"""

from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def attempt_sequence_sorting(seq):
    """
    Return True if the sequence can be sorted, False otherwise
    It also sorts seq, but if this is not possible, the last two elements
    may remain unsorted
    """
    end_sort = len(seq) - 2
    i = 0
    while i < end_sort:
        if seq[i] > seq[i + 1]:
            tmp = seq[i]
            seq[i] = seq[i + 1]
            seq[i + 1] = seq[i + 2]
            seq[i + 2] = tmp
            if i > 0:
                i -= 1
        else:
            i += 1
            # Controls case where last number in seq < two previous numbers
            if i == end_sort and seq[i - 1] > seq[i + 1]:
                i -= 1
                tmp = seq[i]
                seq[i] = seq[i + 1]
                seq[i + 1] = seq[i + 2]
                seq[i + 2] = tmp
        # print i, seq
    return seq[i] <= seq[i + 1]


def can_it_be_sorted(seq):
    """
    Count number of inversions to determine if the list is sortable or not.
    It will be for an even number of inversions
    """
    inversions = 0
    for i, s in enumerate(seq):
        for j in range(i + 1, len(seq)):
            if s > seq[j]:
                inversions += 1
    return inversions % 2 == 0


if __name__ == "__main__":
    # Get input from arguments passed, if any, and parse it
    default = """17 16 15 12 19 20 33 40 10 21 29 30 11"""
    input = readInputArguments(input=default)
    seq = parseString(input, type="float")[0]
    print("Input:           {}".format(seq))

    # Test both algorithms
    can_be_sorted1 = can_it_be_sorted(seq)
    can_be_sorted2 = attempt_sequence_sorting(seq)

    # Print results
    print("Sorting attempt: {}".format(seq))
    if can_be_sorted1:
        print("YES, it is sortable")
    else:
        print("NO, it is not sortable")
    if can_be_sorted2:
        print("YES, it is sortable")
    else:
        print("NO, it is not sortable")
