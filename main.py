import tkinter as tk
import ttt_ai as ai  # Assuming this is the filename for your AI module

# Define constants
BUTTON_HEIGHT = 7
BUTTON_WIDTH = 10
BUTTON_FONT = ('Helvetica', 14, 'bold')

# Define the game board and initial conditions
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False
buttons = [[None for _ in range(3)] for _ in range(3)]

def create_window():
    window = tk.Tk()
    window.title("Tic-Tac-Toe")

    result_label = tk.Label(window, text="", font=BUTTON_FONT)
    result_label.grid(row=3, column=0, columnspan=3)

    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text='', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                               padx=0, pady=0, relief='flat', borderwidth=0,
                               command=lambda row=i, col=j, label=result_label: on_click(row, col, label))
            button.grid(row=i, column=j)
            buttons[i][j] = button

    return window

def on_click(row, col, label):
    global current_player, game_over
    if board[row][col] == ' ' and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, fg='blue' if current_player == 'X' else 'red')
        update_game_state(row, col, label)

def update_game_state(row, col, label):
    global current_player, game_over
    if check_winner(current_player):
        label.config(text=f"Player {current_player} wins!")
        game_over = True
    elif check_draw():
        label.config(text="Draw!")
        game_over = True
    else:
        switch_player()
        if current_player == "O" and not game_over:
            ai_move(label)

def ai_move(label):
    row, col = ai.find_best_move(board, 'O')
    if row is not None:
        board[row][col] = 'O'
        buttons[row][col].config(text='O', fg='red')
        update_game_state(row, col, label)

def switch_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'

def check_winner(player):
    return any(
        all(board[r][c] == player for c in range(3)) for r in range(3)
    ) or any(
        all(board[r][c] == player for r in range(3)) for c in range(3)
    ) or all(
        board[i][i] == player for i in range(3)
    ) or all(
        board[i][2-i] == player for i in range(3)
    )

def check_draw():
    return all(all(cell != ' ' for cell in row) for row in board)

if __name__ == "__main__":
    game_window = create_window()
    game_window.mainloop()
