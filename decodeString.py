#!/usr/bin/env python3

"""
Leetcode algorithm #394: https://leetcode.com/problems/decode-string

Asked in Google interviews according to this:
    https://leetcode.com/discuss/interview-experience/124626/Google-onsite-interview-questions/

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets
are well-formed, etc. Furthermore, you may assume that the original data does not contain any
digits and that digits are only for those repeat numbers, k. For example, there won't be input
like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""


def decodeString(s: str) -> str:
    """Given string s with format 3[a2[c]]xyz2[m] return accaccaccxyzmm."""
    subs = ""
    num = 0
    idx = 0
    stack_num = []
    stack_subs = []
    while idx < len(s):
        v = s[idx]
        idx += 1
        # if we enter a [], save current values to stack
        if v == "[":
            stack_num.append(num)
            num = 0
            stack_subs.append(subs)
            subs = ""
        # if we leave a [], calculate subs based on current subs and last stack value
        elif v == "]":
            prev_subs = stack_subs.pop()
            prev_num = stack_num.pop()
            subs = prev_subs + (subs * prev_num)
        # remember numbers, save to num
        elif v.isdigit():
            num = num * 10 + int(v)
        # remember characters, save to subs
        elif v.isalpha():
            subs += v
        # this should never happen if the input is correct
        else:
            raise Exception("Unexpected input string '{}'".format(s))
    return subs


def decodeStringRecursive(s: str) -> str:
    """Given string s with format 3[a2[c]]xyz2[m] return accaccaccxyzmm.
    
    Recursive algorithm.
    """
    r, idx = recursive_task(s, 0)
    return r


def recursive_task(s, idx):
    """For s, return value of decoded string until first unpaired ']' or until end of string counting from idx.

    If idx <> 0, s[idx - 1] will always be '['.
    """
    subs = ""
    num = 0
    while idx < len(s):
        v = s[idx]
        idx += 1
        # if we enter a [], calculate contents of [] (recursively), multiply by num and add to subs
        if v == "[":
            tmp_subs, idx = recursive_task(s, idx)
            subs = subs + (tmp_subs * num)
            num = 0
        # if we leave a [], return result of contents of []
        elif v == "]":
            return subs, idx
        # remember numbers, save to num
        elif v.isdigit():
            num = num * 10 + int(v)
        # remember characters, save to subs
        elif v.isalpha():
            subs += v
        # this should never happen if the input is correct
        else:
            raise Exception("Unexpected input string '{}'".format(s))
    return subs, idx


if __name__ == "__main__":
    inp = "abc10[d]2[e3[fg]h2[i]]jk2[l]"
    print("INPUT:           ", inp)
    print("OUTPUT stack:    ", decodeString(inp))
    print("OUTPUT recursive:", decodeStringRecursive(inp))
