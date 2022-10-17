#!/usr/bin/env python3

"""
For my advanced algorithms class at Washington University in Saint Louis.
Input: matrix nxn of integers, where every row and every column is sorted
       number X
Output: whether X is in the matrix (True) or not (False)
"""

import numpy as np


def is_number_in_matrix(A, X):
    """Returns True if X is in matrix A, False otherwise.

    Expects A's columns and rows to be sorted.
    """
    m = len(A[0])
    n = len(A)
    return recursive_is_number_in_matrix(A, X, 0, m - 1, 0, n - 1)


def recursive_is_number_in_matrix(A, X, xo, xd, yo, yd):
    """Returns True if X is in matrix A from pos (xo, yo) to pos (xd, yd).

    Expects A's columns and rows to be sorted.
    xo and yo refer to the 1st row and column that will be checked in A
    searching for X; xd and yd refer to the last row and column that will
    be checked in search of X.
    """
    if xd - xo < 0 or yd - yo < 0:
        return False
    elif xd - xo == 0 and yd - yo == 0:
        if A[yo][xo] == X:
            print("Found, X = {} = A[{}][{}]!".format(X, A[yo][xo], yo, xo))
        return A[yo][xo] == X
    x = int((xo + xd) / 2)
    y = int((yo + yd) / 2)
    if A[y][x] == X:
        print("Found, X = {} = A[{}][{}]!".format(X, A[y][x], y, x))
        return True
    elif A[y][x] > X:
        r = recursive_is_number_in_matrix(A, X, xo, x - 1, yo, y - 1)
        if not r:
            r = recursive_is_number_in_matrix(A, X, xo, x - 1, y, yd)
        if not r:
            r = recursive_is_number_in_matrix(A, X, x, xd, yo, y - 1)
    else:
        r = recursive_is_number_in_matrix(A, X, x + 1, xd, y + 1, yd)
        if not r:
            r = recursive_is_number_in_matrix(A, X, xo, x, y + 1, yd)
        if not r:
            r = recursive_is_number_in_matrix(A, X, x + 1, xd, yo, y)
    return r


def main():
    """Main program, create matrix and extensively test is_number_in_matrix."""
    # Create matrix of nxn elements, where every column and row is sorted
    n = 100
    matrix = np.zeros((n, n), dtype=int)
    matrix[0, 0] = 1
    print("Generating sorted matrix...")
    for i in range(n):
        for j in range(n):
            if j > 0:
                matrix[i, j] = np.ceil(matrix[i, j - 1] * 1.1)
            else:
                if i > 0:
                    matrix[i, j] = matrix[i - 1, j] + i
    # Find unique numbers in matrix
    print("\nFinding unique numbers in matrix...")
    unique_numbers = np.unique(matrix)
    # Try to find all unique numbers in the matrix
    print("\nSearching all unique numbers in matrix...")
    for i, X in enumerate(unique_numbers):
        print("------- {} ({}) -------".format(i, X))
        if not is_number_in_matrix(matrix, X):
            print("There was an error. {} was not found.".format(X))
            return False
    # Find all non existing numbers in matrix
    print("\nFinding numbers <= {} not found in matrix...".format(n * n))
    non_existing_numbers = []
    for i in range(n * n):
        if i + 1 not in unique_numbers:
            non_existing_numbers.append(i + 1)
    non_existing_numbers = np.array(non_existing_numbers)
    # Check what happens when a number cannot be found
    print("\nSearching non existing numbers in matrix...")
    for i, X in enumerate(non_existing_numbers):
        print("------- {} ({}) -------".format(i, X))
        if is_number_in_matrix(matrix, X):
            print("There was an error. {} was found.".format(X))
            return False
    return True


if __name__ == "__main__":
    main()
