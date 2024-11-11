from collections import deque

# Class to represent a state in the water jug problem
class JugState:
    def __init__(self, x, y):
        self.x = x  # Amount of water in jug X
        self.y = y  # Amount of water in jug Y

    def __repr__(self):
        return f"({self.x}, {self.y})"

# Function to check if the state has been visited
def is_visited(state, visited):
    return (state.x, state.y) in visited

# BFS to solve the water jug problem
def water_jug_solver(cap_x, cap_y, target):
    # Initial state
    initial_state = JugState(0, 0)
    queue = deque([initial_state])
    visited = set()
    visited.add((0, 0))

    while queue:
        current_state = queue.popleft()
        
        # Print the current state
        print(f"Visiting: {current_state}")
        
        # Check if the target has been reached
        if current_state.x == target or current_state.y == target:
            print(f"Reached target: {current_state}")
            return True

        # Possible operations
        possible_moves = [
            JugState(cap_x, current_state.y),  # Fill jug X
            JugState(current_state.x, cap_y),  # Fill jug Y
            JugState(0, current_state.y),      # Empty jug X
            JugState(current_state.x, 0),      # Empty jug Y
            # Pour from X to Y
            JugState(max(0, current_state.x - (cap_y - current_state.y)),
                     min(cap_y, current_state.x + current_state.y)),
            # Pour from Y to X
            JugState(min(cap_x, current_state.x + current_state.y),
                     max(0, current_state.y - (cap_x - current_state.x)))
        ]

        # Enqueue valid and unvisited states
        for move in possible_moves:
            if not is_visited(move, visited):
                visited.add((move.x, move.y))
                queue.append(move)
    
    print("No solution found.")
    return False

# Test the program
if __name__ == "__main__":
    jug_x_capacity = 4  # Capacity of jug X
    jug_y_capacity = 3  # Capacity of jug Y
    target_amount = 2   # Target amount to be measured

    water_jug_solver(jug_x_capacity, jug_y_capacity, target_amount)
