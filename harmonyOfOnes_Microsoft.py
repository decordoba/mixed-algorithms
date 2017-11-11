#!/usr/bin/env python
# Works in python2 and python3

"""
Easier Challenge 1 from Microsoft Competition at WashU (10 min)

Harmony of Ones | 1 point(s)

In this problem, you will be given two numbers as input. The numbers are constrained to being
signed 32-bit, non-negative integers. Your program should compute the number of times the set bits
are in the same position for both numbers. Essentially, this means counting the number of times
there is a "1" in the same base-2 place for both the first and second integer. As an example,
consider input "7,3". The numbers "7,3" are in decimal; in binary 7 is "111" and 3 is "011".
For that example, your program should output 2 because there is a set bit in the same base-2
place twice.

Input definition

The first line of an input file for this problem will be N, the number of test cases to solve.
It is noted that 100 <= N <= 500

The next N lines will be in the following format:

"x,y" where x and y are both positive integers, i.e. 1 <= X, Y <= MAXINT.

Output definition

Your output should have N lines; each line should be an integer that is the count of the number
of places where there are 1s in the binary representations of both numbers.

Example input

3
31,65
7,3
7,7

Example output

1
2
3
"""


if __name__ == "__main__":
    inp = """3
31,65
7,3
7,7"""
    print("INPUT:")
    for line in inp.split("\n"):
        print(line)
    print("\nOUTPUT:")
    lines = inp.split("\n")
    cases = int(lines[0])
    for i in range(cases):
        n1, n2 = lines[i + 1].split(",")
        n1, n2 = bin(int(n1))[2:], bin(int(n2))[2:]
        if len(n1) != len(n2):
            if len(n1) < len(n2):
                n1, n2 = n2, n1
            n2 = ("0" * (len(n1) - len(n2))) + n2
        total = 0
        for c1, c2 in zip(n1, n2):
            if c1 == "1" and c2 == "1":
                total += 1
        print(total)
