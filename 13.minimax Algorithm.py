import math

# Print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if there's a winner
def check_winner(board):
    for player in ["X", "O"]:
        for row in board:
            if all([cell == player for cell in row]):
                return player
        for col in range(3):
            if all([board[row][col] == player for row in range(3)]):
                return player
        if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
            return player
    return None

# Check if there are any empty spaces left
def check_tie(board):
    return all([cell != " " for row in board for cell in row])

# Minimax function for the AI
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif check_tie(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# AI's move
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        # Player's move
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))
        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue
        board[row][col] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("Player X wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI's move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print("AI O wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

tic_tac_toe()
