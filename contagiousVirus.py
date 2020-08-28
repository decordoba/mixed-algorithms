#!/usr/bin/env python

"""
From Leetcode
We receive a matrix with 0s and 1s. A 1 means infected, a 0 means healthy.
Any cell will get the virus if 2 or more of the adjacent individuals (not diagonally) are infected.
Which of your individuals end up infected after the infection has spread as far as it can?
Return the resulting matrix.

Example:
In:     00000000
        01010000
        00010000
        01001000
        00010010
        00001000
        00001001
        01000000

Out:    00000000
        01111111
        01111111
        01111111
        01111111
        01111111
        01111111
        01111111

I don't know where I got this problem from exactly, I had it in my laptop unfinished and revently (Aug 2020) I finished.
I have not even been ablt to check if this is the most optimal solution, although I am pretty sure it is.
"""


from basic.basic import *  # Find basic.py in https://github.com/decordoba/basic-python


class Farm(object):
    def __init__(self, world):
        self.world = [[int(x) for x in row] for row in world]
        self.h = len(world)
        self.w = len(world[0])
        self.neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def get(self, x, y):
        return self.world[y][x]

    def set(self, x, y, value=1):
        self.world[y][x] = value

    def out_of_bounds(self, x, y):
        return x >= self.w or y >= self.h or x < 0 or y < 0

    def predict_infection(self):
        # for every cell that is not 1, get neighbors that could infect it and save it to ht
        # if the cell has 2+ infected neighbors, set it to 1
        ht = {}
        for y in range(self.h):
            for x in range(self.w):
                if self.get(x, y) == 0:
                    is_sick, neigh = self.gets_sick(x, y)
                    if is_sick:
                        self.set(x, y, value=1)
                    else:
                        ht[(x, y)] = neigh
        # iterate until infection stops, ht contains all cells not yet infected
        # after every iteration, remove new infections from ht
        virus_spread = True
        while virus_spread and len(ht) > 0:
            virus_spread = False
            for x, y in list(ht.keys()):
                sick_neighbors = 0
                for neigh in ht[(x, y)]:
                    if self.get(*neigh) == 1:
                        sick_neighbors += 1
                        if sick_neighbors >= 2:
                            self.set(x, y, value=1)
                            del ht[(x, y)]
                            virus_spread = True
                            break
        return self.world
    
    def gets_sick(self, x, y):
        # check all neighbors, return whether it cell gets infected
        # and if not the neighbors that may infect the cell in the future
        neighbors = []
        sick_neighbors = 0
        for i, j in self.neighbors:
            cell = (x + i, y + j)
            if self.out_of_bounds(cell[0], cell[1]):
                continue
            if self.get(cell[0], cell[1]) == 1:
                sick_neighbors += 1
                if sick_neighbors >= 2:
                    return True, None
            neighbors.append((cell[0], cell[1]))
        return False, neighbors


if __name__ == "__main__":
    default = \
'''00000000
01010000
00010000
01001000
00010010
00001000
00001001
01000000'''
    inp = readFileArgument(default, print_input=False)
    inp = [list(line) for line in inp.split("\n")]
    print("INPUT:\n{}".format(indentString(printNice(inp, print_result=False))))
    f = Farm(inp)
    outp = f.predict_infection()
    print("OUTPUT:\n{}".format(indentString(printNice(outp, print_result=False))))
