NEIGHBORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class MazeSolver:
    def __init__(self, maze, start_pos, end_pos, hearts):
        self.maze = maze
        self.solve_maze(start_pos, end_pos, hearts)
    
    def solve_maze(self, start_pos, end_pos, init_hearts)
        queue = [(start_pos, init_hearts, 0)]
        visited = set()
        while len(queue) > 0:
            pos, hearts, path = queue.pop(0)
            if (pos, hearts) in visited:
                continue
            visited.add((pos, hearts))
            if end_pos == pos:
                return path
            neighbors = self.get_neighbors(pos, hearts, path)
        return None
    
    def get_neighbors(self, pos, hearts, path):
        states = []
        for x, y in NEIGHBORS:
            new_pos = (pos[0] + x, pos[1] + y)
            new_hearts = hearts
            value = get_value_in_maze(new_pos)
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