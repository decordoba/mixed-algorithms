#!/usr/bin/env python
# Works in python2 and python3

"""
Cracking the Coding Interview Moderate Problem

The Game of Master Mind is played as follows:
The computer has four slots, and each slot will contain a ball that is red (R), yellow
(Y), green (G) or blue (B). For example, the computer might have RGGB (Slot # 1 is red,
Slots #2 and #3 are green, Slot #4 is blue).
You, the user, are trying to guess the solution. You might, for example, guess YRGB.
When you guess the correct color for the correct slot, you get a "hit". If you guess a
color that exists but is in the wrong slot, you get a "pseudo-hit." Note that a slot that
is a hit can never count as a pseudo-hit.

For example, if the actual solution is RGBY and you guess GGRR, you have one hit and one
pseudo-hit. Write a method that, given a guess and a solution, returns the number of hits
and pseudo-hits.
"""


def evaluate_mastermind_position(position, solution, choices=["R", "G", "B", "Y"]):
    hits = 0
    pseudo_hits = 0

    # Create hash-table with all possible pseudo-hits, and count hits
    ht = {c: 0 for c in choices}
    ht2 = {c: 0 for c in choices}
    for p, s in zip(position, solution):
        if p == s:
            hits += 1
        else:
            ht[p] += 1
            ht2[s] += 1

    # Count pseudo-hits
    for choice in ht:
        ht[choice] = min(ht2[choice], ht[choice])
        pseudo_hits += ht[choice]

    return hits, pseudo_hits


if __name__ == "__main__":
    guess = "RRGB"
    sol = "BGRR"
    print("INPUT:")
    print("Guess: {}\nSolution: {}".format(guess, sol))
    hits, pseudo_hits = evaluate_mastermind_position(guess, sol)
    print("\nOUTPUT:")
    print("Hits: {}\nPseudo-hits: {}".format(hits, pseudo_hits))
