# AI MODULE
import random

def find_best_move(board, player):
    # Check if a winning move exists
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player  # Simulate placing player's mark
                if check_for_win(board, player):
                    board[row][col] = ' '  # Undo move
                    return row, col
                board[row][col] = ' '  # Undo move

    # check if opponent can win with next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = "X"
                if check_for_win(board, "X"):
                    board[row][col] = ' '  # Undo move
                    return row, col
                board[row][col] = ' '  # Undo move
    

    # No winning move found, proceed with other strategies
    return find_random_move(board)

def check_for_win(board, player):
    # Check horizontal, vertical, and diagonal wins
    for r in range(3):
        if all(board[r][c] == player for c in range(3)):
            return True
    for c in range(3):
        if all(board[r][c] == player for r in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def find_random_move(board):
    empty_spots = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    if not empty_spots:
        return None, None
    return random.choice(empty_spots)