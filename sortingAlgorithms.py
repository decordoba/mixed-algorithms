#!/usr/bin/env python2

import heapq
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
                a[j], a[j + 1] = a[j + 1], a[j]  #Swap
                newSwaps += 1
        if newSwaps == 0:
            break
        numSwaps += newSwaps
    return numSwaps

def insertionSort(a):
    n = len(a)
    numSwaps = 0
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if a[j] <= a[j+1]:
                break
            a[j], a[j + 1] = a[j + 1], a[j]  #Swap
            numSwaps += 1
    return numSwaps

def selectionSort(a):
    n = len(a)
    numSwaps = 0
    for i in range(n):
        min_value = a[i]
        min_pos = i
        for j in range(i + 1, n):
            if a[j] < min_value:
                min_value = a[j]
                min_pos = j
        if i != min_pos:
            a[min_pos] = a[i]
            a[i] = min_value
            numSwaps += 1
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

def quickSort(a):
    return quickRecursive(a, 0, len(a))

def quickRecursive(a, i, j):
    idx_pivot, numSwaps = sortAroundPivot(a, i, j)
    if idx_pivot - i > 1:
        numSwaps += quickRecursive(a, i, idx_pivot)
    if j - idx_pivot > 1:
        numSwaps += quickRecursive(a, idx_pivot, j)
    return numSwaps

def sortAroundPivot(a, i, j):
    pivot = a[(i + j) // 2]
    j -= 1
    numSwaps = 0
    while i < j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if j > i:
            a[i], a[j] = a[j], a[i]  # Swap
            i += 1
            j -= 1
            numSwaps += 1
    return i, numSwaps

def heapSort(a):
    heapq.heapify(a)
    a[:] = [heapq.heappop(a) for i in xrange(len(a))]
    return len(a)

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
    # We don't need to move the elements in a[j] because they are already in place
    i = 0
    # This part is what makes the algorithm inefficient: moving buffer back to a
    while k < k2 and i < len(buffer):
        a[k] = buffer[i]
        k += 1
        i += 1
    return numSwaps


if __name__ == "__main__":
    # Read arguments, if none found use default list
    default = "1 5 2 8 4 14 2 7 4 9 8 1 10 7 4 6 11 0 7 12 6 16 10"
    args = readInputArguments(input=default)
    a = parseString(args, "int")[0]
    print "Original:       {} -> Unsorted".format(a)

    # Bubble sort
    a1 = list(a)
    time = getTime()
    it1 = bubbleSort(a1)
    time = getTime() - time
    print "Bubble sort:    {} -> Sorted in {} iterations ({:3}s)".format(a1, it1, time)

    # Insertion sort
    a2 = list(a)
    time = getTime()
    it2 = insertionSort(a2)
    time = getTime() - time
    print "Insertion sort: {} -> Sorted in {} iterations ({:3}s)".format(a2, it2, time)

    # Selection sort
    a3 = list(a)
    time = getTime()
    it3 = selectionSort(a3)
    time = getTime() - time
    print "Selection sort: {} -> Sorted in {} iterations ({:3}s)".format(a3, it3, time)

    # Merge sort
    a4 = list(a)
    time = getTime()
    it4 = mergeSort(a4)
    time = getTime() - time
    print "Merge sort:     {} -> Sorted in {} iterations ({:3}s)".format(a4, it4, time)

    # Merge sort "in place" (slightly slower)
    a5 = list(a)
    time = getTime()
    it5 = mergeSort2(a5)
    time = getTime() - time
    print "Merge sort 2:   {} -> Sorted in {} iterations ({:3}s)".format(a5, it5, time)

    # Quick sort
    a6 = list(a)
    time = getTime()
    it6 = quickSort(a6)
    time = getTime() - time
    print "Quick sort:     {} -> Sorted in {} iterations ({:3}s)".format(a6, it6, time)

    # Heap sort
    a7 = list(a)
    time = getTime()
    it7 = heapSort(a7)
    time = getTime() - time
    print "Heap sort:      {} -> Sorted in {} iterations ({:3}s)".format(a7, it7, time)
