from collections import deque


class Agent:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        self.start = self.find_symbol('S')
        self.goal = self.find_symbol('G')

    def find_symbol(self, symbol):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == symbol:
                    return (r, c)
        return None

    def is_within_bounds(self, position):
        r, c = position
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_wall(self, position):
        r, c = position
        return self.grid[r][c] == '#'

    def get_neighbors(self, position):
        r, c = position

        moves = [
            (-1, 0),  # UP
            (1, 0),   # DOWN
            (0, -1),  # LEFT
            (0, 1)    # RIGHT
        ]

        neighbors = []

        for dr, dc in moves:
            new_pos = (r + dr, c + dc)

            if self.is_within_bounds(new_pos) and not self.is_wall(new_pos):
                neighbors.append(new_pos)

        return neighbors

    def print_grid(self):
        for row in self.grid:
            print(" ".join(row))
        print()

    def mark_path(self, path):
        for r, c in path:
            if self.grid[r][c] not in ('S', 'G'):
                self.grid[r][c] = '*'


def bfs(agent):  # ← fixed parameter name
    start = agent.start
    goal = agent.goal

    frontier = deque([start])
    visited = set([start])
    parent = {}

    nodes_expanded = 0
    goal_found = False

    while frontier:
        current = frontier.popleft()

        if current == goal:
            goal_found = True
            break
        nodes_expanded += 1
        for neighbor in agent.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                frontier.append(neighbor)

    if not goal_found:
        return None, nodes_expanded

    # Reconstruct path
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    return path, nodes_expanded


if __name__ == "__main__":
    grid = [
        ['S', '.', '.', '.', '.'],
        ['#', '#', '.', '#', '.'],
        ['.', '.', '.', '#', '.'],
        ['.', '#', '#', '#', '.'],
        ['.', '.', '.',  '.','G']
    ]

    agent = Agent(grid)

    print("Original Grid:\n")
    agent.print_grid()

    path, nodes_expanded = bfs(agent)

    if path is None:
        print("No path found.")
    else:
        print("Solved!")
        # for pos in path:
        #     print(pos)
        print(f"\nPath length (steps): {len(path) - 1}")
        print(f"Nodes expanded: {nodes_expanded}")

        agent.mark_path(path)

        print("\nGrid with path marked (*):")
        agent.print_grid()
