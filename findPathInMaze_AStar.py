#!/usr/bin/env

from heapq import *
from basic import *  # Find basic.py in https://github.com/decordoba/basic-python

"""
I found this challenge in HackerRank, and I thought it would be interesting to save my A star implementation.
In this example, the algorithm finds the shortest path between two points in a maze.
"""

def AStar(world, state0, goal, cost0=0, heuristic_function=None):
    """
    A* or A star is a path finding algorithm which will always find a path
    if it exists (it is complete), and it will always find the optimal path
    if the heuristic_function is consistent (heur(x) <= heur(y) + dist(x, y))
    and admissible (it never overestimates the actual minimal cost of reaching
    the goal).
    If the heuristic function is not given, or it is set to None, we will be
    doing Uniform Cost Search, which is also optimal but may take more time in
    average to reach the target, as it does not prefer states closer to it.
    """
    # Add initial state to the queue
    priority_queue = []
    heappush(priority_queue, (0, state0, [state0], cost0))
    visited = {}
    # Run while there are nodes in the queue
    while len(priority_queue) > 0:
        # Pop the state with the smallest priority number in the queue
        (current_priority, current_state, current_path, current_cost) = heappop(priority_queue)
        # Skip it if we have already visited it
        if current_state in visited:
            continue
        # Add the state to the visited nodes
        visited[current_state] = current_cost
        # Check if we have reached the goal and return path and cost if we have
        if current_state == goal:
            return (current_path, current_cost)
        # Add all neighbors of current state to queue
        for neighbor_state in getNeighbors(current_state, world):
            cost = current_cost + getCost(current_state, neighbor_state, world)
            heuristic = 0
            if heuristic_function is not None:
                heuristic = heuristic_function(current_state, goal, world)
            priority = cost + heuristic
            path = list(current_path)
            path.append(neighbor_state)
            heappush(priority_queue, (priority, neighbor_state, path, cost))
    # Return empty path and cost=-1 if no path was found
    return ([], -1)

def getCost(prev_state, new_state, world):
    # Return cost of going from prev_state to new_state
    return getManhattanDistance(prev_state, new_state)

def getHeuristic(state, goal, world):
    # Return lower bound of actual distance to goal
    return getManhattanDistance(state, goal)

def getManhattanDistance(state0, state1):
    # Return minimum possible distance between two states
    return abs(state0[0] - state1[0]) + abs(state0[1] - state1[1])

def getNeighbors(state, world):
    # Return all neighbors (states next to our state) that are valid in world
    valid_coord = {" ", "A", "B"}
    neighbors = []
    for i in [+1, -1]:
        state0 = state[0] + i
        if state0 >= world.min_state[0] and state0 <= world.max_state[0]:
            if world.getCoord(state0, state[1]) in valid_coord:
                neighbors.append((state0, state[1]))
        state1 = state[1] + i
        if state1 >= world.min_state[1] and state1 <= world.max_state[1]:
            if world.getCoord(state[0], state1) in valid_coord:
                neighbors.append((state[0], state1))
    return neighbors

class World:
    """
    Class to save variables and handle the maze
    """
    def __init__(self, maze):
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])
        self.min_state = (0, 0)
        self.max_state = (self.height-1, self.width-1)

    def getCoord(self, i, j):
        return self.maze[i][j]

    def setCoord(self, i, j, ch):
        self.maze[i] = self.maze[i][:j] + ch + self.maze[i][j + 1:]

if __name__ == "__main__":
    if __name__ == "__main__":
        default = """35 35
35 1
37 37
#####################################
#       # # #           #   #     # #
# ####### # ### # ### ### ####### # #
#       #       # #     #     # #   #
##### ##### ### # # # ### ##### # ###
#   # # # #   # # # #   # #   # #   #
# ### # # # ### ##### ### # ### ### #
#       #     #   #   #     # # #   #
### ######### ####### ### ### # # # #
#             #       # #   #     # #
# # ##### # ### # # ### # ### ### # #
# # #     # # # # #     #   # # # # #
# # # ####### # ######### ### # ### #
# # # #     #   #     #     #   #   #
### ### # ##### ##### ### ### ##### #
#     # # #     # #     # #   # # # #
# # # # # ### ### ### ### # # # # # #
# # # # #                 # # #     #
### ####### # # ##### ### # ### #####
#       # # # #     #   #     # #   #
##### # # ######### ########### # ###
#   # #           # #     #   # #   #
# ### ##### ######### ##### # # ### #
# #   #      #        #     #       #
# # # ##### ### # # # # #############
# # #   #     # # # #       #   # # #
# # ### ### # # # ######### ### # # #
# #   # #   # # #   # #   # # #     #
# ### ### ##### ### # # ##### # #####
#       #   #     # #     #   # #   #
### # ##### ##### ### ### # ### # ###
# # # # # # # #     # #   # #   # # #
# # ### # # # # ######### # # # # # #
#   #   #   #                 #     #
# # # # ### ### ####### ### ### ### #
#B# # #       #   #       #   # #  A#
#####################################"""
        # Get maze data
        input = readFileArgument(input=default).split("\n")
        start_pos = tuple([int(i) for i in input[0].split()])
        end_pos = tuple([int(i) for i in input[1].split()])
        size = tuple([int(i) for i in input[2].split()])
        maze = input[3:]
        # Print initial maze
        print "INPUT MAZE"
        for line in maze:
            print line
        printSeparator()
        # Create world
        world = World(maze)
        # Find path using A star (A*)
        (path, length) = AStar(world, start_pos, end_pos, heuristic_function=getHeuristic)
        # Print results
        print "Shortest path length: {}".format(length)
        print "Shortest path: {}".format(path)
        printSeparator()
        # Create map with path
        for coord in path:
            if coord != start_pos and coord != end_pos:
                world.setCoord(coord[0], coord[1], "@")
        # Print maze with path
        print "OUTPUT MAZE"
        for line in world.maze:
            print line