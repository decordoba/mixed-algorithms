#!/usr/bin/env python
# Works in python2 and python3

"""
Easy challenge for an internship at Google. Took me 10 min to write the first part.

Array X is greater than array Y if the first non-matching element in both arrays has a
grater value in X than in Y. For example, [1,2,4,3,5] > [1,2,3,4,5] (because the first
element that does not match, 4 vs 3, is larger for the first list)

A contiguous subarray is defined by an interval of the indices, or in other words, a
subarray that has consecutive indexes.

Write a function Solution(A, K) that given a list A consisting of N integers, and an
integer K, returns the largest contiguous subarray of length K from all the contiguous
subarrays of length K.

Example:
    A = [1, 4, 3, 2, 5], K = 3
    Returns [4, 3, 2] because there are 3 subarrays: [1, 4, 3], [4, 3, 2] and [3, 2, 5]
                              and [4, 3, 2] is the largest.

Constraints: 1<=K<=N<=100, 1<=A[J]<=1000, A contains N distinct numbers

This last constraint is weird, because it means that we only care about the first number
of the subarray, not about any other. Therefore, I solved the algorithm in 2 ways, in one
ignoring this constraint (solution) and in the other following it (solution2).
"""


def solution2(A, K):
    # If A has only distinct elements, the problem is trivial,
    # we just have to find the largest number that appears in
    # position <= len(A) - K, and return the array with such
    # element and the next K - 1 numbers in the list

    # Find and return subarray with largest first number
    maxNum = 0
    maxIdx = -1
    for i in range(len(A) - K + 1):
        if maxNum < A[i]:
            maxNum = A[i]
            maxIdx = i

    return A[maxIdx:maxIdx + K]


def compare_As(A1, A2):
    # Return True if A >= B and False if B < A
    for i in range(len(A1)):
        if A1[i] > A2[i]:
            return False
        elif A1[i] < A2[i]:
            return True
    return False


def solution(A, K):
    # In this solution, I AM ASSUMING THERE MAY BE NOT DISTINCT ELEMENTS IN A
    # unlike the problem suggests. To see the solution assuming that there may
    # not be distinct elements in A, see solution2.

    # Make list of potential largest contiguous subarrays
    maxNum = 0
    listA = []
    for i in range(len(A) - K + 1):
        if maxNum <= A[i]:
            maxNum = A[i]
            listA.append(A[i:i + K])

    # Iterate through all arrays to find largest contiguous subarray
    maxA = None
    for a in listA:
        if a[0] < maxNum:
            continue
        if maxA is None or compare_As(maxA, a):
            maxA = a

    return maxA


def test(case, num):
    print(">>", case)
    print("  ", solution(case, num))
    print("")


if __name__ == "__main__":
    test1 = [0, 1, 2, 3, 4, 5, 6, 7]
    test2 = [7, 6, 5, 4, 3, 2, 1, 0]
    test3 = [0, 1, 2, 3, 2, 1, 0, 8]
    test4 = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 0, 1, 2, 3, 4, 5]

    test(test1, 4)
    test(test2, 4)
    test(test3, 4)
    test(test4, 4)
