#!/usr/bin/env

import math
from basic import *  # Find basic.py in https://github.com/decordoba/basic-python

"""
I had to face this challenge in one of my interviews.
We get a string of numbers (0 to 9) and a number of characters to remove, and we have to remove
that number of characters of the string to form the minimum possible number, without changing the
order of the string.
Examples:
removeNumbersFromString("1234255", 4) --> "1225"
removeNumbersFromString("304756756843942", 6) --> "045543942"
removeNumbersFromString("9876563322", 30) --> ""
removeNumbersFromString("012345", 0) --> "012345"
"""

def getMinimumNumberFromString(numbers_string, remove):
    # Solve obvious cases: remove too big or too small
    if remove <= 0:
        return numbers_string
    if remove >= len(numbers_string):
        return "0"

    # Make sure chars are ordered in ascending order from left to right,
    # as long as we can remove more characters
    i = 0
    while remove > 0 and i < len(numbers_string) - 1:
        if numbers_string[i] > numbers_string[i+1]:
            numbers_string = numbers_string[:i] + numbers_string[i+1:]
            remove -= 1
            if i > 0 and numbers_string[i-1] > numbers_string[i]:
                i -= 1
        else:
            i += 1

    # If we got here it means that all chars are ordered, remove the biggest
    # numbers, which will be at the end
    if remove > 0:
        numbers_string = numbers_string[:-remove]
    return numbers_string


if __name__ == "__main__":
    args = readInputArguments(input="")
    if len(args) > 0:
        numbers_string, remove = parseString(args)[0]
        print getMinimumNumberFromString(numbers_string, int(remove))
    else:
        print "Usage: python {} NUMERIC_STRING CHARS_TO_REMOVE".format(sys.argv[0])