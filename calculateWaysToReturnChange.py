#!/usr/bin/env python2

"""
Interesting code similar to countPathsStaircase.py.
https://www.hackerrank.com/challenges/coin-change

The goal is to find the number of ways of returning change for N units (our money goal)
using a list of coins given (we assume we have infinite coins of each type available).

Example: Goal: 6, Coins: [1, 2, 3] => Result: 7
(1+1+1+1+1+1), (1+1+1+1+2), (1+1+1+3), (1+2+3), (3+3), (2+2+2), (1+1+2+2)
"""

from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def calculate_change_combinations_smart(goal, coins):
    """
    Most efficient algorithm, similar to countPathsStaircase.py,
    but in this case the order of the sum does not matter.
    """
    combinations = [0] * goal
    for coin in coins:
        combinations[coin - 1] += 1
        for i in range(goal):
            prev_pos = i - coin
            if prev_pos >= 0:
                combinations[i] += combinations[prev_pos]

    return combinations[-1]


def calculate_change_combinations(goal, coins):
    """
    This is my original approach to the problem. It is slightly less efficient
    that calculate_change_combinations_smart but it basically does exactly the
    same. In this case, we can observe ht and see what coins were added.
    """

    # Technically there is no need for sorting, I kept it because this was my original algorithm
    coins.sort()
    ht = {}
    for coin_value in coins:
        ht[coin_value] = [0] * goal
        try:
            ht[coin_value][coin_value - 1] = 1
        except IndexError:
            pass

    for i in range(goal):
        for j in range(len(coins)):
            coin_j = coins[j]
            prev_pos = i - coin_j
            if prev_pos >= 0:
                for k in range(j, len(coins)):
                    coin_k = coins[k]
                    ht[coin_j][i] += ht[coin_k][prev_pos]

    num_combinations = 0
    for coin_value in coins:
        num_combinations += ht[coin_value][-1]

    return num_combinations


if __name__ == "__main__":
    # Get input from arguments passed, if any, and parse it
    # Format: goal money \n list of coin values to reach such value
    default = """100
1 2 5 10 50 100"""
    input = readInputArguments(input=default)
    parsed_input = parseString(input, type="int")
    if len(parsed_input) == 1:
        money_goal = parsed_input[0][0]
        coins = parsed_input[0][1:]
    else:
        money_goal, coins = parsed_input
        money_goal = money_goal[0]

    # Run algorithm and measure performance
    t1, num_comb1 = timeFunction(calculate_change_combinations, money_goal, coins)
    t2, num_comb2 = timeFunction(calculate_change_combinations_smart, money_goal, coins)

    print("Money goal: {} units\nAvailable coins: {}".format(money_goal, coins))
    print("Number of coin combinations to reach the goal: {}\n".format(num_comb1))
    print("Time taken with marginally slower algorithm: {} seconds".format(t1))
    print("Time taken with marginally faster algorithm: {} seconds".format(t2))
    print("Both solution give the same result? {}".format("YES" if num_comb1 == num_comb2 else "NO"))
