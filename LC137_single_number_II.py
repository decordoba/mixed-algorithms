#!/usr/bin/env python3

"""
Leetcode algorithm #137: https://leetcode.com/problems/single-number-ii/

Asked in Google interviews according to this:
    https://leetcode.com/discuss/interview-experience/124626/Google-onsite-interview-questions/

Given a non-empty array of integers, every element appears three times except for one,
which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99

Below I have implemented the generic solution, where we have k = num times
all numbers is repeated, and t = num times target number is repeated.
"""


def singleNumber(nums:[int], k:int=3, t:int=1) -> int:
    """Given list of numbers, find number repeated only t times.

    All other numbers are repeated k times.
    Only works if k > t.
    """
    assert k > t
    counter = []
    len_c = 0
    for n in nums:
        bin_n = list(("{:0" + str(len_c) + "b}").format(n))
        # adjust length number so they have the same number of bits
        if len_c < len(bin_n):
            counter = [0] * (len(bin_n) - len_c) + counter
            len_c = len(counter)
        # add all bits, reset when we reach k in counter
        for i in range(len_c):
            b = bin_n[i]
            if b == "0":
                continue
            counter[i] = counter[i] + 1
    r = "".join([str((c % k) // t) for c in counter])
    return int(r, 2)


def singleNumber_NSpaceComplexity(nums:[int], k:int=3, t:int=1) -> int:
    """Given list of numbers, find number repeated only t times.

    All other numbers are repeated k times.
    """
    assert k != t
    ht = {}
    for n in nums:
        if n not in ht:
            ht[n] = 0
        ht[n] += 1
    for n in ht:
        if ht[n] == t:
            return n
    return "Error"


def singleNumber_XOR_k3_t1(nums:[int]) -> int:
    """Given list of numbers, find number repeated only once when all other numbers are repeated 3 times.

    How does it work: let's say we get [5, 5, 5, 4]
    first 5 will set first_rep to 5 (0 ^ A = A, A & 1 = A), second_rep to 0 (5 & ~5 = 0)
    second 5 will set first_rep to 0 (A ^ A = 0), second_rep to 5 (0 ^ A = A, A & 1 = A)
    third 5 will set first rep to 0 (5 & ~5 = 0), second_rep to 0 (A ^ A = 0, A & 1 = 0)
    Therefore, after the 3rd repetition of a number, it gets erased from both
    We see here that first_rep saves first appearance of a number, second_rep saves second.
    """
    first_rep = 0
    second_rep = 0
    for n in nums:
        first_rep = (first_rep ^ n) & ~second_rep
        second_rep = (second_rep ^ n) & ~first_rep
    return first_rep


def singleNumber_XOR_k3_t2(nums:[int]) -> int:
    """Given list of numbers, find number repeated only twice when all other numbers are repeated 3 times."""
    first_rep = 0
    second_rep = 0
    for n in nums:
        first_rep = (first_rep ^ n) & ~second_rep
        second_rep = (second_rep ^ n) & ~first_rep
    return second_rep


if __name__ == "__main__":
    inp = [100, 543, 100, 9, 42, 543, 100, 42, 42, 543]
    k = 3
    t = 1
    print("INPUT:            ", inp)
    print("K:                ", k)
    print("T:                ", t)
    print("OUTPUT bit method:", singleNumber(inp, k, t))
    print("OUTPUT ht method :", singleNumber_NSpaceComplexity(inp, k, t))
    print("OUTPUT xor method:", singleNumber_XOR_k3_t1(inp))

    print()

    inp = [100, 19, 19, 543, 9, 100, 9, 42, 543, 100, 42, 42, 543, 19]
    k = 3
    t = 2
    print("INPUT:            ", inp)
    print("K:                ", k)
    print("T:                ", t)
    print("OUTPUT bit method:", singleNumber(inp, k, t))
    print("OUTPUT ht method :", singleNumber_NSpaceComplexity(inp, k, t))
    print("OUTPUT xor method:", singleNumber_XOR_k3_t2(inp))
