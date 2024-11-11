from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, depth=0):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.depth = depth
        self.parent = None

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if (self.missionaries > 0 and self.missionaries < self.cannibals) or \
           (self.missionaries < 3 and (3 - self.missionaries) < (3 - self.cannibals)):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def get_possible_moves(self):
        moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
        possible_states = []
        for m, c in moves:
            if self.boat == 1:  # Boat on the left bank
                new_state = State(self.missionaries - m, self.cannibals - c, 0, self.depth + 1)
            else:  # Boat on the right bank
                new_state = State(self.missionaries + m, self.cannibals + c, 1, self.depth + 1)
            if new_state.is_valid():
                new_state.parent = self
                possible_states.append(new_state)
        return possible_states

    def __eq__(self, other):
        return self.missionaries == other.missionaries and \
               self.cannibals == other.cannibals and \
               self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __str__(self):
        return f"({self.missionaries}, {self.cannibals}, {self.boat})"

def bfs(initial_state):
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            return path[::-1]  # Return reversed path

        for next_state in current_state.get_possible_moves():
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)

    return None

# Initial state: 3 missionaries, 3 cannibals, and the boat on the left bank
initial_state = State(3, 3, 1)
solution_path = bfs(initial_state)

if solution_path:
    print("Solution found!")
    for state in solution_path:
        print(state)
else:
    print("No solution found.")
