#!/usr/bin/env python2

"""
Leetcode algorithm categorized as hard, which surprisingly was really
easy to solve: https://leetcode.com/problems/trapping-rain-water
The problem is that, given n non-negative integers representing an
elevation map where the width of each bar is 1, compute how much water
it is able to trap after raining (see picture in url).

Example:
Given [0,1,0,2,1,0,1,3,2,1,2,1], 6 units of water get trapped: 1 in the
3rd position, 1 in the 5th, 2 in the 6th, 1 in the 7th, and 1 in the 9th.

This problem is quite similar to waterContainers.
"""

from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def calculateRainWater(heights):
    """
    Returns the amount of water trapped in a 2D ground defined by heights
    :type heights: List[int]
    :rtype: tuple: (int, List[int])
    """
    if len(heights) <= 0:
        return 0
    i = 0
    j = len(heights) - 1
    max_height_l = heights[i]
    max_height_r = heights[j]
    water = 0
    water_list = [0] * len(heights)
    # Increment i and decrement j until they both meet at the highest point
    while i < j:
        if heights[i] <= heights[j]:
            i += 1
            curr_idx = i
            curr_height = heights[i]
            if curr_height >= max_height_l:
                max_height_l = curr_height
        else:
            j -= 1
            curr_idx = j
            curr_height = heights[j]
            if curr_height >= max_height_r:
                max_height_r = curr_height
        max_height = min(max_height_l, max_height_r)
        water_here = max(max_height - curr_height, 0)
        water += water_here
        water_list[curr_idx] = water_here
    return (water, water_list)

if __name__ == "__main__":
    # Get input from arguments passed, if any, and parse it
    default = """0 1 0 2 1 0 1 3 2 1 2 1"""
    input = readInputArguments(input=default)
    heights = parseString(input, type="float")[0]
    
    # Calculate algorithm
    water, water_list = calculateRainWater(heights)
    
    print "Water volume:", water    
    # Plot the ground and the water in the solution
    ground_y = duplicateAllElementsList(heights)
    ground_x = [0] + duplicateAllElementsList(range(1, len(heights))) + [len(heights)]
    water_y = duplicateAllElementsList([water_list[i] + heights[i] for i in range(len(heights))])
    water_x = ground_x
    plotLine(water_y, water_x, style=":", color="c", axis=[min(ground_x), max(ground_x), min(ground_y) - 1, max(ground_y) + (max(ground_y) - min(ground_y))], label="Rain water", show=False)
    plotLine(ground_y, ground_x, color="k", label="Ground shape", show=False)
    plotLegend()
    plotText(max(ground_y) + (max(ground_y) - min(ground_y)) * 0.33, len(heights) / 2.0, "Rain water volume: {}".format(water), fontsize="xx-large", fontweight="bold", show=True)