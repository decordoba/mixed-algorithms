#!/usr/bin/env python2

"""
Easy challenge for an internship at Google. Took me 15 min to write it.
(I should have invested a bit more time though, I did not optimize it as much
as I should have, and it was quite obvious how to do it, I thought I'd have
the chance to resubmit it again later, like in HackerRank, but that was not the case).

One string is strictly smaller than another when the frequency of occurrences
of the smallest character is less than the frequency of occurrence of the smallest
character in the comparison string.

For example, string "debc" is smaller than string "aaa" because the smallest
character in "debc" is "b", with a frequency of 1, and the smallest character
in "aaa" is "a", but with a frequency of 3.

Write a function solution(A, B) that, given a string A (which contains M strings
separated by " ") and string B (which contains N strings separated by " "), return
an array C of N integers. For J in 0..N-1, C[J] specifies the number of strings
in A strictly smaller than B[J].

Example:
    A = "abcd aabc bd", B = "aaa aa"
    Returns [3, 2] because all words in A are strictly smaller than "aaa"
                           and "abcd" and "bd" are strictly smaller than "aa"

Constraints: 1<=N<=10000, 1<=M<=10000, 1<=length_any_word_in_A_or_B<=10
             All the words only have lowercase English alphabet letters
"""

import random
import string
from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def calculateValue(s):
    # s: string without spaces
    smallest = None
    num = 0
    for c in s:
        if smallest is None or c < smallest:
            smallest = c
            num = 1
        elif c == smallest:
            num += 1
    return num


def calculateString(A):
    # A: string of words
    Alist = A.split()
    values = []
    for a in Alist:
        values.append(calculateValue(a))
    return values


def solution(A, B):
    valuesA = calculateString(A)
    valuesB = calculateString(B)

    result = []
    for b in valuesB:
        num = 0
        for a in valuesA:
            if a < b:
                num += 1
        result.append(num)

    return result


# I did not submit this, but it is possible to speed up the above
# code with a hash table. Hopefully it is not necessary, as we have
# at most 10000, so at most O(M*N +M + N) (this would produce O(11M + 11N))
# Empirically, the time difference is really big! 7s become 0.05s in the worst case
def solution_faster(A, B):
    valuesA = calculateString(A)
    valuesB = calculateString(B)

    result = []
    ht = {}
    for b in valuesB:
        if b not in ht:
            num = 0
            for a in valuesA:
                if a < b:
                    num += 1
            ht[b] = num
        else:
            num = ht[b]
        result.append(num)

    return result


def generate_random_sentence(num_words=10000, max_len_word=10, min_len_word=1):
    sentence = ""
    for i in range(num_words):
        len_word = random.randint(min_len_word, max_len_word)
        sentence += ''.join(random.choice(string.ascii_lowercase) for _ in range(len_word))
        if i < num_words - 1:
            sentence += " "
    return sentence


if __name__ == "__main__":
    A = generate_random_sentence(num_words=10000)
    B = generate_random_sentence(num_words=10000)

    t1, sol1 = timeFunction(solution, A, B)
    t2, sol2 = timeFunction(solution_faster, A, B)

    print("Time taken with slow algorithm: {} seconds".format(t1))
    print("Time taken with fast algorithm: {} seconds".format(t2))

    print("Both solution give the same result? {}".format("YES" if sol1 == sol2 else "NO"))
