#!/usr/bin/env python2

"""
Interesting algorithm from Leetcode:
https://leetcode.com/problems/container-with-most-water
Given n non-negative integers {a1, a2, ..., an}, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms
a container, such that the container contains the most water.

Examples:
[1,2,3,4,5,70,4,3,2,1] --> 15 (from 3 to 3, therefore 3x5=12)

I encourage you to try this one out!! I spent some time working on the graphical
representation of the solution and I think it looks nice!
"""

from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def maxArea2(heights):
    """
    First attempt, I tried to do some tricks to speed it up but it would still timeout
    Still, although slower, it works
    :type heights: List[int]
    :rtype: int
    """
    max_vol = 0
    besti = -1
    bestj = -1
    lenh = len(heights)
    for i, h1 in enumerate(heights):
        if (lenh - 1 - i) * h1 < max_vol:
            continue
        for j in range(lenh - 1, -1, -1):
            if (j - i) * h1 < max_vol:
                break
            h2 = heights[j]
            vol = min(h1, h2) * (j - i)
            if max_vol < vol:
                max_vol = vol
                besti = i
                bestj = j
    return (max_vol, besti, bestj)


def maxArea1(heights):
    """
    Most optimal algorithm, O(n) time complexity
    :type heights: List[int]
    :rtype: int
    """
    max_vol = 0
    besti = -1
    bestj = -1
    i = 0
    j = len(heights) - 1
    while i <= j:
        vol = min(heights[i], heights[j]) * (j - i)
        if max_vol < vol:
            max_vol = vol
            besti = i
            bestj = j
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return (max_vol, besti, bestj)


if __name__ == "__main__":
    # Get input from arguments passed, if any, and parse it
    default = """3 3.5 4 4.5 5 5.5 6 6.5 7 7.5 8 9 10 9 8 7 3 2 1"""
    input = readInputArguments(input=default)
    heights = parseString(input, type="float")[0]

    # Calculate best container and print information
    print("Heights (input): {}".format(heights))
    t1, result1 = timeFunction(maxArea1, heights)  # Measures time taken to run maxArea1(heights)
    t2, result2 = timeFunction(maxArea2, heights)  # Measures time taken to run maxArea2(heights)
    print("Result: max surface = {} \nSee figure to see container".format(result1[0]))
    print("Algorithm 1 runtime: {}s".format(t1))
    print("Algorithm 2 runtime: {}s".format(t2))

    # Plot representation of best container
    max_container_y = [heights[result1[1]], 0, 0, heights[result1[2]]]
    max_container_x = [result1[1] + 1, result1[1] + 1, result1[2] + 1, result1[2] + 1]
    water_level_y = [min(heights[result1[1]], heights[result1[2]]),
                     min(heights[result1[1]], heights[result1[2]])]
    water_level_x = [result1[1] + 1, result1[2] + 1]
    plotLine(heights, range(1, len(heights) + 1), style="--", color="b", label="Heights (input)",
             show=False)
    plotLine(water_level_y, water_level_x, color="c", style=":", label="Water level", show=False)
    plotLine(max_container_y, max_container_x, color="r", label="Maximum container", show=False)
    plotText(min(heights[result1[1]], heights[result1[2]]) / 2.0,
             (result1[2] + result1[1] + 2) / 2.0, result1[0], fontsize="xx-large",
             fontweight="bold", show=True)
    plotLegend(boxed=False)
