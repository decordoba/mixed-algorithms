#!/usr/bin/env python3

"""
Asked in Google interviews according to this:
    https://leetcode.com/discuss/interview-experience/124626/Google-onsite-interview-questions/

We get a list of numbers, ordered, every number appears 3 times
except one which appears 2 (or 1 times). Find the number that appears less than 3 times.

Example:
[7,7,7,8,8,8,10,10,10,11,11,12,12,12,15,15,15] -> Return 11

Expected runtime complexity: O(log(n))
"""


def missingNumber(nums):
    left, right= 0, len(nums)
    mid = (right - left) // 2
    ...