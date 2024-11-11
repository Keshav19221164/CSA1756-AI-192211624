N = 8  # Size of the chessboard (8x8 for the 8-queens problem)

# Function to print the solution
def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

# Function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

# Function to solve the N-queens problem using backtracking
def solve_nqueens(board, col):
    # Base case: If all queens are placed, return True
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = True  # Place the queen

            # Recursively place the rest of the queens
            res = solve_nqueens(board, col + 1) or res

            board[i][col] = False  # Backtrack

    return res

# Initialize the board with False (no queens placed)
board = [[False for _ in range(N)] for _ in range(N)]

# Call the function to solve the 8-queens problem
if not solve_nqueens(board, 0):
    print("No solution exists")
