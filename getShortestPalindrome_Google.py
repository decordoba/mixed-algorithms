#!/usr/bin/env python
# Works in python2 and python3

"""
Algorithm from a Google interview.
Find shortest palindrome that can be created from another string,
adding any characters in any position in the string. The only requirement
is that no letters in the original string can be removed or their
order can be changed.

Example: abc --> abcba
         hello --> hoelleoh
         badfa --> bafdfab
         batrbmnal --> blatrbmnmbrtalb
"""


def get_shortest_palindrome(s):
    # Recursive function
    if len(s) <= 1:
        return s
    if len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[1] + s

    c0 = s[0]
    cn = s[-1]

    if c0 == cn:
        return c0 + get_shortest_palindrome(s[1:-1]) + cn
    else:
        p1 = get_shortest_palindrome(s[:-1])
        p2 = get_shortest_palindrome(s[1:])
        if len(p1) <= len(p2):
            return cn + p1 + cn
        else:
            return c0 + p2 + c0


if __name__ == "__main__":
    inp = "abc"
    outp = get_shortest_palindrome(inp)
    print("IN:  {}\nOUT: {}".format(inp, outp))

    inp = "hello"
    outp = get_shortest_palindrome(inp)
    print("IN:  {}\nOUT: {}".format(inp, outp))

    inp = "decordoba"
    outp = get_shortest_palindrome(inp)
    print("IN:  {}\nOUT: {}".format(inp, outp))

    inp = "batrbmnal"
    outp = get_shortest_palindrome(inp)
    print("IN:  {}\nOUT: {}".format(inp, outp))
