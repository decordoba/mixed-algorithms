
"""
Simple problem seen on Leetcode to practice semaphores

There is a mall with m entrances, n exits, and there can be at most x people inside.
Design the system so that
"""

class Mall(object):
    def __init__(self, m, n, x):
        self.m = m  # num entrances
        self.n = n  # num exits
        self.x = x  # max num customers
        self.semaphore =

    def enter(self, entrance_num):
        if entrance_num >= self.m:
            print("ERROR: Entrances must be numbers from 0 to {}".format(self.m - 1))
            return False
        if
