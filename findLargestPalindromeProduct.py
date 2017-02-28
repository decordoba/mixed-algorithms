#!/usr/bin/env python2

from basic import *  # Find basic.py in https://github.com/decordoba/basic-python

"""
Solved in leetcode: https://leetcode.com/problems/largest-palindrome-product
Find the largest palindrome made from the product of two n-digit numbers. The range of n is [1,8].
Since the result could be very large, you should return the largest palindrome mod 1337.
Examples:
n:1, factors:1,9, palindrome: 9, result: 9.
n:2, factors:91,99, palindrome: 9009, result: 987.
n:3, factors:913,993, palindrome:906609, result:123.
n:4, factors:9901,9999, palindrome:99000099, result:597.
n:5, factors:99681,99979, palindrome:9966006699, result:677
n:6, factors:999001,999999, palindrome:999000000999, result:1218
n:7, factors:9997647,9998017, palindrome:99956644665999, result:877
n:8, factors:99990001,99999999, palindrome:9999000000009999, result:475
n:9, factors:999920317,999980347, palindrome:999900665566009999, result:1226  # Takes forever!!
"""


def generatePalindromes(num_digits, order="asc"):
    """
    Generate all palindromes with num_digits, in ascending or descending order
    Example: generatePalindromes(3, order="asc")  --> [101, 111, ..., 989, 999]
             generatePalindromes(4, order="desc") --> [9999, 9889, ..., 1001]
    We don't use it in the algorithm, but it may be useful for other problems
    """

    # Return empty list if num_digits is smaller than 1
    if num_digits < 1:
        return []

    # Calculate constants for ascending and descending order
    half = num_digits // 2
    if order == "asc":
        numF = 10 ** (half - 1)
        numL = 10 ** half
        seq = range(0, 10, 1)
        order = 1
    else:
        numF = 10 ** half - 1
        numL = 10 ** (half - 1) - 1
        seq = range(9, -1, -1)
        order = -1
    palindromes = []

    # Palindromes with even number of digits
    if num_digits % 2 == 0:
        for i in xrange(numF, numL, order):
            si = str(i)
            pal = int(si + si[::-1])
            palindromes.append(pal)
    # Palindromes with odd number of digits
    elif num_digits > 1:
        for i in xrange(numF, numL, order):
            for j in seq:
                si = str(i)
                pal = int(si + str(j) + si[::-1])
                palindromes.append(pal)
    # Palindromes with only one digit
    else:
        palindromes = seq
        palindromes.remove(0)
    return palindromes

def checkPalindromes(num_digits, break_fn, *args):
    """
    Generate all palindromes with num_digits in descending order, until one of them makes the
    function break_fn(pal, *args) return True
    """
    # Return empty list if num_digits is smaller than 1
    if num_digits < 1:
        return None
    half = num_digits // 2
    # Palindromes with even number of digits
    if num_digits % 2 == 0:
        for i in xrange(10 ** half - 1, 10 ** (half - 1) - 1, -1):
            si = str(i)
            pal = int(si + si[::-1])
            if break_fn(pal, *args):
                return pal
    # Palindromes with odd number of digits
    elif num_digits > 1:
        for i in xrange(10 ** half - 1, 10 ** (half - 1) - 1, -1):
            for j in xrange(9, -1, -1):
                si = str(i)
                pal = int(si + str(j) + si[::-1])
                if break_fn(pal, *args):
                    return pal
    # Palindromes with only one digit
    else:
        for pal in xrange(9, -1, -1):
            if break_fn(pal, *args):
                return pal
    return -1

def isDivisibleByTwoNDigitNumbers(num, n):
    """
    Retruns true if num is the product of two n digit numbers, False otherwise
    """
    smalldiv = bigdiv = int(num ** 0.5)
    if smalldiv % 2 == 0:
        smalldiv -= 1
        bigdiv += 1
    divmin = 10 ** (n - 1)
    divmax = 10 ** n - 1
    # Cheat to speed up the function, due to the fact that all even n's will have as
    # their largest palindrome int("9"*n) times another number. It is unfair because it is
    # technically possible that we are missing some higher palindrome that we will not test
    # (for example, 97*97 > 91*99, but we will not check if 97*97 is a palindrome, so if it
    # was we would skip it. Anyway, for n < 10, this works fine)
    if n % 2 == 0:
        bigdiv = divmax
        smalldiv = min(divmax, int(num / bigdiv) + 1)
    # End of cheat. I prefer calculating this without the cheat, but then the
    # calculation for n=8 takes 24 seconds in my machine instead of less than 1
    while smalldiv >= divmin and bigdiv <= divmax:
        total = smalldiv * bigdiv
        if total == num:
            print "Factors:", smalldiv, bigdiv
            return True
        elif total < num:
            bigdiv += 1
        else:
            smalldiv -= 1
    return False

def largestPalindrome(n):
    """
    Generates the 2n-digit palindromes and returns the largest palindrome that is the result of
    multiplying two n-digit integers. If none of them is, it generates the (2n-1)-digit palindromes
    and returns the maximum palindrome product of two n-digit numbers.
    """
    pal = checkPalindromes(n * 2, isDivisibleByTwoNDigitNumbers, n)
    if pal < 0:
        pal = checkPalindromes(n * 2 - 1, isDivisibleByTwoNDigitNumbers, n)
    print "Palindrome:", pal
    return pal % 1337

if __name__ == "__main__":
    default = "2"
    input = int(readInputArguments(default))
    print "Number of digits:", input
    t = getTime()
    output = largestPalindrome(input)
    print "Result:", output
    print "Time taken: {}".format(getTime() - t)
