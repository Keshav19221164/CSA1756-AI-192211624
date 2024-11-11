import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node_position, goal_position):
    return abs(node_position[0] - goal_position[0]) + abs(node_position[1] - goal_position[1])

def a_star(start, end, grid):
    start_node = Node(start)
    end_node = Node(end)
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        ]
        
        for offset in neighbors:
            neighbor_pos = (current_node.position[0] + offset[0], current_node.position[1] + offset[1])

            if neighbor_pos[0] < 0 or neighbor_pos[0] >= len(grid) or neighbor_pos[1] < 0 or neighbor_pos[1] >= len(grid[0]):
                continue

            if grid[neighbor_pos[0]][neighbor_pos[1]] != 0:
                continue

            neighbor_node = Node(neighbor_pos, current_node)
            
            if neighbor_node.position in closed_set:
                continue
            
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, end_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if any(open_node for open_node in open_list if open_node.position == neighbor_node.position and open_node.f <= neighbor_node.f):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)

path = a_star(start, end, grid)
print("Path found:", path)
