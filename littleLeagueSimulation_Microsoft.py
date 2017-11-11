#!/usr/bin/env python
# Works in python2 and python3

"""
Medium Challenge 2 from Microsoft Competition at WashU (15 min)

Little league simulation | 2 point(s)

In this problem, you will model a simple little league game in which there are a fixed set of
outcomes for a given type of pitch and swing. We will assume that little league pitchers throw
only two types of pitches: Fastball(FB) and Changeup(C). We also assume that little league batters
swing at two speeds: Fast(F) and Slow(S). For this problem, we will use the following pitch, swing,
and outcome tuples:

(FB, F, Homerun)
(C, S, Hit)
(FB, S, Strike)
(C, F, Strike)
The rest of the simulated game largely uses normal baseball rules:

A hit resets the strike count to zero.
If four hits are obtained in a row, a run is scored and the count of hits is decremented.
A homerun results in n+1 runs, where n is the number of hits and the hit count returns to zero.
If three strikes are obtained in a row, an out results.
Three outs end the inning and the simulation (further data can be ignored).
Input definition

An input file for this problem will contain a list of play tuples, containing a pitch (FB or C) and
a swing (F or S). The tuples will be grouped by parenthesis and be comma and space separated. The
full set of plays will be enclosed in a pair of parentheses.

Output definition

Your output should be the integer number of runs scored in the inning represented by the input.

Example input

((FB, S), (C, F), (FB, S), (FB, F), (C, S), (FB, F), (C, F), (FB, S), (C, F), (C, S), (FB, F), (C, S), (FB, S), (C, F), (FB, S))
Example output

5
"""


if __name__ == "__main__":
    inp = "((FB, S), (C, F), (FB, S), (FB, F), (C, S), (FB, F), (C, F), (FB, S), (C, F), (C, S), (FB, F), (C, S), (FB, S), (C, F), (FB, S))"
    print("INPUT:")
    print(inp)
    print("\nOUTPUT:")

    strikes = 0
    runs = 0
    outs = 0
    bases = [0, 0, 0]
    for pitchswing in inp[2:-2].split("), ("):
        pitch, swing = pitchswing.split(", ")
        pitch = 0 if pitch == "C" else 1
        swing = 0 if swing == "S" else 1

        if (pitch + swing) % 2 == 1:
            # Strike
            strikes += 1
            if strikes >= 3:
                outs += 1
                strikes = 0
        elif swing == 1:
            # Homerun
            runs += 1 + sum(bases)
            bases = [0, 0, 0]
            strikes = 0
        else:
            # Hit
            if bases[2] == 1:
                runs += 1
            bases[2] = bases[1]
            bases[1] = bases[0]
            bases[0] = 1
            strikes = 0

        if outs >= 3:
            break

    print(runs)
