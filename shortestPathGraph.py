#!/usr/bin/env python2

import Queue
from collections import defaultdict
from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


"""
Challenge from HackerRank. https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach
We have an undirected graph consisting of n nodes where each node is labeled from 1 to n and
the edge between any two nodes is always of length 6. Given a node s, calculate the shortest
distance from s to all the other nodes in the graph. Then print a single line of n-1
space-separated integers listing all the distances (ordered sequentially by node number).
If a node is disconnected from s, print -1 for that distance.
"""


class Graph:
    """
    Class to create and handle graphs. Thought just to solve the problem, not flexible
    """
    def __init__(self, n, cost_edge):
        self.n = n
        self.cost_edge = cost_edge
        self.edges = defaultdict(lambda: [])

    def addConnection(self, node0, node1):
        # Add connection between node 1 and node0, and between node0 and node1
        self.edges[node0].append(node1)
        self.edges[node1].append(node0)

    def findAllDistances(self, root):
        # Create map of distances to root
        distances = [-1] * self.n
        distances[root] = 0
        # Create queue
        q = Queue.Queue()
        q.put(root)        
        # Run BFS while there are nodes in the queue
        # This will explore all the graph once and get all distances from root
        while not q.empty():
            node = q.get()
            height = distances[node]
            for child in self.edges[node]:
                if distances[child] == -1:
                    q.put(child)
                    distances[child] = height + self.cost_edge
        # Pop the root to print
        distances.pop(root)
        print(" ".join(map(str, distances)))


class World:
    """
    Class to solve the problem, more flexible than Graph (and therefore, longer and more complex
    code), and also faster, I suspect because defaultdict is not too fast
    """
    def __init__(self, num_nodes, cost_edge):
        self.default_cost = cost_edge
        self.num_nodes = num_nodes
        self.neighbors = {}
        self.pathlengths = {}

    def addConnection(self, node0, node1):
        # Could be simplified with defaultdict, to avoid checking for exceptions
        try:
            self.neighbors[node0][node1] = None
            self.pathlengths[node0][node1] = 1
        except KeyError:
            self.neighbors[node0] = {node1: None}
            self.pathlengths[node0] = {node1: 1}
        try:
            self.neighbors[node1][node0] = None
            self.pathlengths[node1][node0] = 1
        except KeyError:
            self.neighbors[node1] = {node0: None}
            self.pathlengths[node1] = {node0: 1}

    def findAllDistances(self, node):
        # Finds distances from node ot every other node
        # node -1 will never be reached, therefore, the whole graph will be searched
        self.BFS(node, -1)
        buff = ""
        for n in range(self.num_nodes):
            if n == node:
                continue
            if n not in self.pathlengths[node]:
                buff += "{} ".format(-1)
            else:
                buff += "{} ".format(self.pathlengths[node][n])
        print buff[:-1]

    def BFS(self, state0, goal):
        # Add initial state to the queue
        queue = [(state0, 0)]
        visited = {}
        # Run while there are nodes in the queue
        while len(queue) > 0:

            # Pop the first state in the queue
            (current_state, current_path_length) = queue.pop(0)

            # Skip it if we have already visited it
            if current_state in visited:
                continue

            # Add the state to the visited nodes
            visited[current_state] = current_path_length

            # Save min length of path between state0 and current_state
            self.savePathLength(state0, current_state, current_path_length)

            # Check if we have reached the goal and return path if we have
            if current_state == goal:
                return current_path_length

            # Add all neighbors of current state to queue
            for neighbor_state in self.getNeighbors(current_state):
                queue.append((neighbor_state, current_path_length + self.default_cost))

        # Return empty list if no path was found from start to goal states
        return -1

    def savePathLength(self, node0, node1, path_length):
        # Could be simplified with defaultdict, to avoid checking for exceptions
        try:
            self.pathlengths[node0][node1] = path_length
        except KeyError:
            self.pathlengths[node0] = {node1: path_length}
        try:
            self.pathlengths[node1][node0] = path_length
        except KeyError:
            self.pathlengths[node1] = {node0: path_length}

    def getNeighbors(self, state):
        return self.neighbors[state]


if __name__ == "__main__":
    input = \
"""2
10 10
1 2
1 3
2 4
3 5
4 6
5 7
7 8
8 9
9 10
6 10
1
3 1
2 3
2"""

    lines = input.split("\n")
    t = int(lines[0])
    idx = 1
    for i in range(t):
        n, m = [int(x) for x in lines[idx].split()]
        idx += 1
        edge_cost = 6
        graph = Graph(n, edge_cost)
        world = World(n, edge_cost)
        for i in xrange(m):
            x, y = [int(x) for x in lines[idx].split()]
            idx += 1
            graph.addConnection(x-1,y-1)
            world.addConnection(x - 1, y - 1)
        s = int(lines[idx])
        idx += 1
        printSeparator("*")
        print "Graph Results:"
        t0 = getTime()
        graph.findAllDistances(s-1)
        print "Time: {}s".format(getTime() - t0)
        printSeparator()
        print "World Results:"
        t1 = getTime()
        world.findAllDistances(s - 1)
        print "Time: {}s".format(getTime() - t1)
    printSeparator("*")