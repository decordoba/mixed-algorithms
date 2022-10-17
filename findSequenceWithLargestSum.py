#!/usr/bin/env python
# Works in python2 and python3

"""
Cracking the Coding Interview Moderate Problem

You are given an array of integers (both positive and negative).
Find the contiguous sequence with the largest sum. Return the sum.

Input: 2, -8, 3, -2, 4, -10
Output: 3, -2, 4
"""


def find_sequence_with_largest_sum(array):
    max_sum = None
    best_seq = None
    curr_sum = 0
    curr_seq = []
    for n in array:
        curr_sum += n
        if curr_sum <= 0:
            curr_sum = 0
            curr_seq = []
        else:
            curr_seq.append(n)
            if curr_sum > max_sum:
                max_sum = curr_sum
                best_seq = curr_seq
    if max_sum is not None:
        return max_sum, best_seq
    max_sum = max(array)
    return max_sum, [max_sum]


if __name__ == "__main__":
    arr = [2, -8, 3, -2, 4, -10]
    print("INPUT:")
    print(arr)
    sum, seq = find_sequence_with_largest_sum(arr)
    print("\nOUTPUT:")
    print("Sequence: {} (sums {})".format(seq, sum))
