#!/usr/bin/env python2

"""
Longest Common Subsequence (LCS)
Well known dynamic programming problem that I used to have a hard time wrapping
my head around to find the optimal solution (brute force is easy, duh).
We get two strings or lists a and b, and have to find the length of the longest
shared subsequence. Interestingly enough, brute force does not take a lot longer
than the dynamic programming approach.

Example:
a = "helloworld", b = "myworkshell", sol = 4 ("hell")
a = "helloworld", b = "myworkshetl", sol = 3 ("wor")
"""

import sys
import random
import string
from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def lcs_bruteforce(a, b):
    max_subseq_len = 0
    max_subseq_idx = 0
    for i in range(len(a)):
        for j in range(len(b)):
            subseq_len = 0
            try:
                while a[i + subseq_len] == b[j + subseq_len]:
                    subseq_len += 1
            except IndexError:
                pass
            if subseq_len > max_subseq_len:
                max_subseq_len = subseq_len
                max_subseq_idx = i
    return max_subseq_len, a[max_subseq_idx:max_subseq_idx + max_subseq_len]

def lcs_dynamic(a, b):
    map = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    max_subseq_len = 0
    max_subseq_idx = 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                map[i][j] = map[i - 1][j - 1] + 1
                if map[i][j] > max_subseq_len:
                    max_subseq_len = map[i][j]
                    max_subseq_idx = i
    return max_subseq_len, a[max_subseq_idx - max_subseq_len:max_subseq_idx]

def lcs_dynamic_print_map(a, b):
    map = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    max_subseq_len = 0
    max_subseq_idx = 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                map[i][j] = map[i - 1][j - 1] + 1
                if map[i][j] > max_subseq_len:
                    max_subseq_len = map[i][j]
                    max_subseq_idx = i
    printable_map = [[" ", "|"] + list(b), ["-", "+"] + ["-"] * len(b)]
    for i, row in enumerate(map):
        if i == 0:
            continue
        printable_map.append([a[i - 1], "|"] + row[1:])
    printNice(printable_map)
    return max_subseq_len, a[max_subseq_idx - max_subseq_len:max_subseq_idx]


if __name__ == "__main__":
    # Get input from arguments passed, if any, and parse it
    # Format: goal money \n list of coin values to reach such value
    default = """supercalifragilisticohelloespialidoso tregunamecoidesdecorumsatishellodee"""
    input = readInputArguments(input=default).split()
    if len(input) < 2:
        num = 8000
        print "Generating two inputs with size {} (the computation may take a few minutes...)".format(num)
        available_chars = string.ascii_lowercase
        input = ["".join([random.choice(available_chars) for _ in range(num)]),
                 "".join([random.choice(available_chars) for _ in range(num)])]
    a = input[0]
    b = input[1]
    
    
    # Run algorithm and measure performance
    t1, answ1 = timeFunction(lcs_bruteforce, a, b)
    t2, answ2 = timeFunction(lcs_dynamic, a, b)
    
    # Run algorithm and print map (if it is not too big)
    if len(a) < 50 and len(b) < 50:
        len_substr, substr = lcs_dynamic_print_map(a, b)
        print "Input string 1: \"{}\"\nInput string 2: \"{}\"".format(a, b)
    else:
        len_substr, substr = answ1
    
    print "Substring: \"{}\" with length: {}\n".format(substr, len_substr)
    print "Time taken with brute force algorithm: {} seconds".format(t1)
    print "Time taken with dynamic algorithm:     {} seconds".format(t2)
    print "Both solution give the same result? {}".format("YES" if answ1 == answ2 else "NO")
