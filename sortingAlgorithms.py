#!/usr/bin/env python2

from basic import *  # Find basic.py in https://github.com/decordoba/basic-python

"""
A sample of the sorting algorithms that I have implemented for different algorithms
"""

def bubbleSort(a):
    n = len(a)
    numSwaps = 0
    for i in range(n):
        newSwaps = 0
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
                newSwaps += 1
        if newSwaps == 0:
            break
        numSwaps += newSwaps
    return numSwaps

def mergeSort(a):
    b, swaps = mergeRecursive(a)
    # Save ordered list in original list a
    for i in range(len(a)):
        a[i] = b[i]
    return swaps

def mergeRecursive(a):
    len_a = len(a)
    if len_a <= 1:
        return (a, 0)
    len_b = len_a//2
    len_c = len_a - len_b
    b, sw1 = mergeRecursive(a[:len_b])
    c, sw2 = mergeRecursive(a[len_b:])
    sw3 = 0
    i = 0
    j = 0
    buff = []
    while i < len_b and j < len_c:
        if b[i] > c[j]:
            buff.append(c[j])
            j += 1
            sw3 += len_b - i
        else:
            buff.append(b[i])
            i += 1
    while i < len_b:
        buff.append(b[i])
        i += 1
    while j < len_c:
        buff.append(c[j])
        j += 1
    return buff, sw1 + sw2 + sw3


if __name__ == "__main__":
    # Read arguments, if none found use default list
    default = "1 5 2 8 4 2 7 4 9 8 1 10 7 4 6"
    args = readInputArguments(input=default)
    a = parseString(args, "int")[0]
    print "Original:    {} -> Unsorted".format(a)

    # Bubble sort
    a1 = list(a)
    it1 = bubbleSort(a1)
    print "Bubble sort: {} -> Sorted in {} iterations".format(a1, it1)

    # Merge sort
    a2 = list(a)
    it2 = mergeSort(a2)
    print "Merge sort:  {} -> Sorted in {} iterations".format(a2, it2)


####################################################################################################
## After this line, less optimal algorithms (that I didn't have the heart to delete) can be found ##
####################################################################################################

def mergeSort2(a):
    # Like mergeSort but performs swaps over a. Slower than mergeSort
    return mergeRecursive2(a, 0, len(a) // 2, len(a))

def mergeRecursive2(a, i, j, k):
    if i == j:
        return 0
    half1 = (j - i) / 2.0
    half2 = (k - j) / 2.0
    numSwaps = mergeRecursive2(a, i, int(i + half1), int(i + 2 * half1))
    numSwaps += mergeRecursive2(a, j, int(j + half2), int(j + 2 * half2))
    k1 = j
    k2 = k
    k = i
    buffer = []
    while i < k1 and j < k2:
        if a[i] > a[j]:
            buffer.append(a[j])
            j += 1
            numSwaps += k1 - i
        else:
            buffer.append(a[i])
            i += 1
    while i < k1:
        buffer.append(a[i])
        i += 1
    while j < k2:
        buffer.append(a[j])
        j += 1
    i = 0
    # This part is what makes the algorithm inefficient: putting buffer in a
    while k < k2:
        a[k] = buffer[i]
        k += 1
        i += 1
    return numSwaps
