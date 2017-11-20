#!/usr/bin/env python
# Works in python2 and python3

"""
Algorithm from a Google interview.
Find length of shortest path in a maze from start_position to end_position.
Three possible values in maze: 0=space, 1=wall, 6=enemy (takes one life from player)
We want to find shortest path length, knowing that we can never consume all our lifes,
but there is no penalty for spending all but one.
"""

NEIGHBORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class MazeSolver:
    def __init__(self, maze, start_pos, end_pos, hearts):
        self.maze = maze
        path = self.solve_maze(start_pos, end_pos, hearts)
        print("Path length: {}".format(path))
    
    def solve_maze(self, start_pos, end_pos, init_hearts):
        queue = [(start_pos, init_hearts, 0)]
        visited = set()
        while len(queue) > 0:
            pos, hearts, path = queue.pop(0)
            if (pos, hearts) in visited:
                continue
            visited.add((pos, hearts))
            if end_pos == pos:
                return path
            queue += self.get_neighbors(pos, hearts, path)
        return None
    
    def get_neighbors(self, pos, hearts, path):
        states = []
        for x, y in NEIGHBORS:
            new_pos = (pos[0] + x, pos[1] + y)
            new_hearts = hearts
            value = self.get_value_in_maze(new_pos)
            if value is None:
                continue
            if value == 1:
                continue
            if value == 6:
                if new_hearts <= 1:
                    continue
                new_hearts -= 1
            states.append((new_pos, new_hearts, path + 1))
        return states
    
    def get_value_in_maze(self, pos):
        w = len(self.maze[0])
        h = len(self.maze)
        x, y = pos
        if x < 0 or x >= w or y < 0 or y >= h:
            return None
        return self.maze[y][x]


if __name__ == "__main__":
    maze = [[0, 1, 0, 0, 0],
            [0, 6, 0, 6, 0],
            [0, 0, 0, 1, 0]]
    start_pos = (0, 0)
    end_pos = (4, 2)
    print("Maze:")
    for line in maze:
        print(line)
    print("Start position: {}".format(start_pos))
    print("End position:   {}".format(end_pos))
    print("Hearts: {}".format(1))
    MazeSolver(maze, start_pos, end_pos, 1)
    print("Hearts: {}".format(2))
    MazeSolver(maze, start_pos, end_pos, 2)
    print("Hearts: {}".format(3))
    MazeSolver(maze, start_pos, end_pos, 3)
