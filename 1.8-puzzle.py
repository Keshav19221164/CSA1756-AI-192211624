from heapq import heappop, heappush

# Helper function to print the board
def print_board(board):
    for i in range(3):
        print(board[i*3:(i+1)*3])
    print()

# Function to find the index of the blank space (0)
def find_blank(board):
    return board.index(0)

# Function to calculate the Manhattan distance heuristic
def manhattan_distance(board, goal):
    distance = 0
    for i in range(1, 9):  # Exclude the blank tile (0)
        curr_index = board.index(i)
        goal_index = goal.index(i)
        distance += abs(curr_index // 3 - goal_index // 3) + abs(curr_index % 3 - goal_index % 3)
    return distance

# Function to get the possible moves from the current state
def get_neighbors(board):
    neighbors = []
    blank_index = find_blank(board)
    row, col = divmod(blank_index, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_board = board[:]
            # Swap the blank tile with the adjacent tile
            new_board[blank_index], new_board[new_index] = new_board[new_index], new_board[blank_index]
            neighbors.append(new_board)

    return neighbors

# A* search algorithm
def a_star_search(start, goal):
    open_list = []
    heappush(open_list, (0, start))
    came_from = {}
    g_score = {tuple(start): 0}
    f_score = {tuple(start): manhattan_distance(start, goal)}

    while open_list:
        _, current = heappop(open_list)

        if current == goal:
            path = []
            while tuple(current) in came_from:
                path.append(current)
                current = came_from[tuple(current)]
            path.append(start)
            path.reverse()
            return path

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[tuple(current)] + 1

            if tuple(neighbor) not in g_score or tentative_g_score < g_score[tuple(neighbor)]:
                came_from[tuple(neighbor)] = current
                g_score[tuple(neighbor)] = tentative_g_score
                f_score[tuple(neighbor)] = tentative_g_score + manhattan_distance(neighbor, goal)
                heappush(open_list, (f_score[tuple(neighbor)], neighbor))

    return None

# Initial and goal states
start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8] 
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  

# Run the A* search
solution_path = a_star_search(start_state, goal_state)

# Print the solution path
if solution_path:
    print("Solution found:")
    for step in solution_path:
        print_board(step)
else:
    print("No solution exists.")
