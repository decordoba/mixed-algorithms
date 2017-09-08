#!/usr/bin/env python2

"""
https://www.hackerrank.com/contests/womens-codesprint-3/challenges/hackathon-shirts

Input:
    The first line contains an integer denoting q (the number of queries). The subsequent lines describe each query in the following format:
    1. The first line contains an integer denoting n (the number of participants).
    2. The second line contains n space-separated unique integers describing the respective values of [s0,s1,...,sn-1] (the size preferences
       each participant).
    3. The third line contains an integer denoting v (the number of vendors).
    4. Each line j of the v subsequent lines contains two space-separated integers describing the respective values of smallest_j and
       largest_j for the range of sizes sold by vendor j.

Output:
    Print q lines of output where each line k contains the number of appropriately-sized shirts Jessica procures in the kth query.

Example:
    Input:                  Output:                 Explanation:
        2                       3                       2 querys
        5                       1                       1st query has 5 users that want Tshirts with sizes (2,3,6,9,13) and 4 vendors
        2 3 6 9 13                                      4 vendors sell Tshirts of size 3-7, 4-8, 14-16, 10-13
        4                                               We can get only 3 of the 5 Tshirts: 3 (in 3-7), 6 (in 4-8), 13 (in 10-13), but not 2, 9
        3 7                                             2nd query, we can only get size 3 (3-4) but not 2
        4 8
        14 16
        10 13
        2
        3 2
        2
        3 4
        4 5
"""

import math
import sys

def original_solution():
    result = ""
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n = int(raw_input().strip())
        sizes = map(int, raw_input().strip().split(' '))
        v = int(raw_input().strip())
        ht = {}
        ht2 = {}
        for a1 in xrange(v):
            smallest, largest = raw_input().strip().split(' ')
            smallest, largest = [int(smallest), int(largest)]
            if smallest in ht:
                ht[smallest] = max(ht[smallest], largest)
            else:
                ht[smallest] = largest
                
        k = sorted(ht.keys())
        prevk = k[0]
        mink = ht[prevk]
        for i in k:
            if i <= mink + 1 and prevk != i:
                mink = max(mink, ht[i])
                ht[prevk] = mink
                del(ht[i])
            else:
                prevk = i
                mink = ht[i]
        k = sorted(ht.keys())

        sizes.sort()
        idx = 0
        total = 0
        try:
            for s in sizes:
                if s < k[idx]:
                    continue
                while ht[k[idx]] < s:
                    idx += 1
                if s >= k[idx]:
                    total += 1
        except IndexError:
            pass

        result += "{}\n".format(total)
    return result


def best_solution():
    t = int(raw_input())
    result = ""

    for case in range(t):
        n = int(raw_input())
        users = map(int, raw_input().split())
        users.sort()
        m = int(raw_input())
        ranges = []
        for i in xrange(0, m):
            b,e = map(int, raw_input().split())
            ranges.append((b, True))
            ranges.append((e, False))
        
        ranges = sorted(ranges)

        sizes_found = 0
        idx_users = 0
        overlapped_ranges = 0
        for size, range_beginning in ranges:
            if range_beginning:  # beginning of vendor's sizes range
                if overlapped_ranges == 0:
                    start_point = size
                overlapped_ranges += 1
            else:  # end of vendor's sizes range
                overlapped_ranges -= 1

            if overlapped_ranges == 0:   # a group of overlapped ranges ended
                end_point = size
                while idx_users < n and users[idx_users] <= end_point:
                    if users[idx_users] >= start_point:
                        sizes_found += 1
                    idx_users += 1

        result += "{}\n".format(sizes_found)
    return result


if __name__ == "__main__":
    sample_input = """2
5
2 3 6 9 13
4
3 7 
4 8
14 16
10 13
2
3 2
2
3 4
4 5"""
    sample_output = """3
1"""

    print "------------------------------------"
    print "Try the following Sample Input: \n{}".format(sample_input)
    print "____________________________________"
    print "Expected result: \n{}\n".format(sample_output)
    print "------------------------------------"
    print "Try it using original_solution():"
    sol = original_solution()
    print "____________________________________"
    print "Result: \n{}".format(sol)
    print "------------------------------------"
    print "Try it using best_solution():"
    sol = best_solution()
    print "____________________________________"
    print "Result: \n{}".format(sol)
    print "------------------------------------"