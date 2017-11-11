#!/usr/bin/env python2

"""
Easy problem from leetcode: https://leetcode.com/submissions/detail/94691998/
The goal is to, given a string, find the length of the longest substring without
repeating characters. For example:

Examples:
"abcabcbb" --> "abc" ==> 3
"bbbbb" --> "b" ==> 1
"pwwkew" --> "wke" ==> 1
"""

from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def lengthOfLongestSubstring1(s):
    """ My first approach to the problem. It was a lot harder to design
    compared to the other solution, as it must update a substring from where
    new characters are added and substracted all the time """
    ht = {}
    substr = ""
    max_substr = 0
    removed = 0
    for i, c in enumerate(s):
        if c in ht and ht[c] - removed >= 0:
            if substr[ht[c] - removed] == c:
                max_substr = max(max_substr, len(substr))
                substr = substr[ht[c] - removed + 1:]
                removed = ht[c] + 1
        ht[c] = len(substr) + removed
        substr += c
    max_substr = max(max_substr, len(substr))
    return max_substr


def lengthOfLongestSubstring2(s):
    """ More optimized (and smarter) solution """
    ht = {}
    max_substr = 0
    idx0 = 0
    for i, c in enumerate(s):
        # If we find a character repeated inside the substring
        if c in ht and ht[c] >= idx0:
            max_substr = max(max_substr, i - idx0)
            idx0 = ht[c] + 1  # Update substring's first character position
        ht[c] = i  # Monitor position where every character was last seen
    max_substr = max(max_substr, len(s) - idx0)
    return max_substr

if __name__ == "__main__":
    default = "asdflkjendsfafinddjhrbans"
    inp = readInputArguments(input=default)


    print "Solving with Algorithm 1: {}".format(lengthOfLongestSubstring1(inp))
    print "Solving with Algorithm 2: {}".format(lengthOfLongestSubstring2(inp))
