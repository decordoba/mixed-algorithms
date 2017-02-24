#!/usr/bin/env python2

import math
from basic import *  # Find basic.py in https://github.com/decordoba/basic-python

"""
I had to face this challenge in one of my interviews.
This problem is similar (but easier) to getMinimumNumberFromString, which can be found in
https://github.com/decordoba/mixed-algorithms
We get a integer number greater than zero, and we have to join a pair of two adjacent digits in
such number, taking the mean of both and rounding the number up, to get the maximum possible
number after replacing both adjacent numbers byt the new one.
Examples:
convertNumber(623315) --> 63315  (we do (2+3)/2->2.5->3, and we put the 3 back where 23 was 63315)
convertNumber(567890) --> 67890
convertNumber(631) --> 62
convertNumber(998577) --> 99867
"""

def replaceTwoDigitsByMean(X):
    # Convert X to string
    strX = str(X)
    # Return original number if the length is smaller than 2
    if len(strX) < 2:
        return X

    # Make sure chars are ordered in descending order from left to right.
    # When we find they are not, replace them by the mean of both to get max number
    for i in range(len(strX) - 1):
        if strX[i] < strX[i+1]:
            avg = calculateCeilMean(int(strX[i]), int(strX[i+1]))
            return int(strX[:i] + str(avg) + strX[i+2:])

    # If we reach this point, it means that all chars are ordered.
    # Therefore, replacing the last pair by the mean will give us the max number
    return int(strX[:-2] + calculateCeilMean(int(strX[-2]), int(strX[-1])))

def calculateCeilMean(a, b):
    # Take mean of a and b and apply a ceil. Example: a=3, b=6 --> (3+6)/2=4.5 becomes 5
    return int(math.ceil((a + b) / 2.0))


if __name__ == "__main__":
    args = readInputArguments(input="")
    if len(args) > 0:
        number = parseString(args)[0][0]
        print replaceTwoDigitsByMean(int(number))
    else:
        print "Usage: python {} POSITIVE_INTEGER".format(sys.argv[0])
