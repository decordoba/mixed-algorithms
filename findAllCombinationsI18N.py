#!/usr/bin/env python
# Works in python2 and python3

"""
Algorithm that calculates all i18n combinations of a word
Internationalization = I18N = I123456789012345678N

Example with input GOOGLE:
GOOGLE
GOOGLE, GOOG1E, GOO1LE, GOO2E, GO1GLE, GO1G1E, GO2LE, GO3E, G1OGLE, G1OG1E, G1O1LE, G1O2E, G2GLE,
G2G1E, G3LE, G4E.

This is a Dynamic Programming example, here is what it does:
GOOGLE: Let's use the algorithm with prefix G and word OOGLE

Recursive fn returns all possible combinations
G, OOGLE
do same but selecting all possible values of first char:
Input: "OGLE", "O" -> Len(4) => Recursive => Return [OOGLE, OOG1E, OO1LE, OO2E, O1GLE, O1G1E,
                                                     O2LE, O3E]
Input: "GLE", "1O" -> Len(3) => Recursive => Return [1OGLE, 1OG1E, 1O1LE, 1O2E]
Input: "LE", "2G"  -> Len(2) => Recursive => Return [2GLE, 2G1E]
Input: "E", "3L"   -> Len(1) => Return 3LE
Input: "", "4E"    -> Len(0) => Return 4E
** Remember results for OOGLE

Recursive fn returns all possible combinations
GO, OGLE
do same but selecting all possible values of first char:
Input: "GLE", "O" -> Len(3) => Recursive => Return [O + GLE, O + G1E, O + 1LE, O + 2E]
Input: "LE", "1G" -> Len(2) => Recursive => Return [1G + LE, 1G + 1E]
Input: "E", "2L"  -> Len(1) => Return 2L + E
Input: "", "3E"   -> Len(0) => Return 3E
** Remember results for OGLE

Recursive fn returns all possible combinations
GOO, GLE
do same but selecting all possible values of first char:
Input: "LE", "G" -> Len(2) => Recursive => Return [G + LE, G + 1E]
Input: "E", "1L" -> Len(1) => Return 1L + E
Input: "", "2E"  -> Len(0) => Return 2E
** Remember results for GLE

Recursive fn returns all possible combinations
GOOG, LE
do same but selecting all possible values of first char:
Input: "E", "L"  -> Len(1) => Return LE
Input: "", "1E"  -> Len(0) => Return 1E
** Remember results for LE
"""

import sys


words_table = {}


def return_all_i18n(s):
    return recursive_find(s, prefix_can_be_number=False)


def recursive_find(s, prefix_can_be_number=True):
    n = len(s)
    result = []
    for i in range(n):
        prefix = ""
        if i > 0:
            prefix += str(i)
            if not prefix_can_be_number:
                break
        prefix += s[i]

        sub_s = s[i+1:]
        if len(sub_s) < 2:
            sufixes = [sub_s]
        elif sub_s in words_table:
            sufixes = words_table[sub_s]
        else:
            sufixes = recursive_find(sub_s)
            words_table[sub_s] = sufixes
        for sufix in sufixes:
            result.append(prefix + sufix)
    return result


if __name__ == "__main__":
    s = "HelloWorld"
    if len(sys.argv) > 1:
        s = sys.argv[1]
    result = return_all_i18n(s)
    for i18n in result:
        print(i18n)
    print("Length:", len(result))
