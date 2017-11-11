#!/usr/bin/env python
# Works in python2 and python3

"""
Easier Challenge 1 from Microsoft Competition at WashU (12 min)

Matrix Symmetry | 1 point(s)

Matrices and their transposes are among the fundamental elements of the world of scientific
computing. To find the transpose of a matrix, one simply flips the values over the diagonal of the
matrix -- that is, swaps the row and column keys.

For examples, consider these matrices:

1  2        1  2  3
3  4        4  5  6
            7  8  9
Their transposes are:

1  3        1  4  7
2  4        2  5  8
            3  6  9
When a matrix and its transpose are equal, the matrix is said to be symmetric. It is noted that by
definition, 1x1 matrices (a single element) are always symmetric.

For this problem, you are asked to identify which of the given matrices are symmetric, and which
ones are not.

Input definition

An input file for this problem will contain multiple rows. Each row represents a square N x N
matrix in character delimited form. Semicolons (;) delimit rows, and commas (,) delimit columns.

For example, the string "1,2;3,4" represents the matrix:

1  2
3  4

Output definition

Your output should contain one line for each line of input. The output should read "Symmetric" if
the given matrix is a symmetric matrix, and "Not symmetric" in any other case.

Example input

-84,17;-42,-4
36,27;62,55
-89,-63,-30;-63,-69,47;-30,47,-2
2,48;64,-64
-48
13,-15,86,-43,6,54,-42;-15,97,31,-70,-48,-86,3;86,31,89,-66,-88,74,7;-43,-70,-66,49,6,-58,15;6,-48,-88,6,51,40,-43;54,-86,74,-58,40,-7,2;-42,3,7,15,-43,2,79

Example output

Not symmetric
Not symmetric
Symmetric
Not symmetric
Symmetric
Symmetric
"""


def convert_matrix_string_to_list(s):
    rows = s.split(";")
    return [[int(el) for el in row.split(",")] for row in rows]


def is_matrix_symmetric(m):
    # Assume all matrixs are square
    n = len(m)
    # Not fastest way but fastest to code
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[j][i]:
                return False
    return True


if __name__ == "__main__":
    inp = """-84,17;-42,-4
36,27;62,55
-89,-63,-30;-63,-69,47;-30,47,-2
2,48;64,-64
-48
13,-15,86,-43,6,54,-42;-15,97,31,-70,-48,-86,3;86,31,89,-66,-88,74,7;-43,-70,-66,49,6,-58,15;6,-48,-88,6,51,40,-43;54,-86,74,-58,40,-7,2;-42,3,7,15,-43,2,79"""
    print("INPUT:")
    for line in inp.split("\n"):
        print(line)
    print("\nOUTPUT:")

    for line in inp.split("\n"):
        m = convert_matrix_string_to_list(line)
        sym = is_matrix_symmetric(m)
        print("Symmetric" if sym else "Not symmetric")
