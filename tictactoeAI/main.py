# imports
import tkinter as tk

# define constants
BUTTON_HEIGHT = 7
BUTTON_WIDTH = 10
BUTTON_FONT = ('Helvetica', 14, 'bold')


# define the game board and initial conditions
board = [[' ', ' ', ' ',],[' ', ' ', ' ',], [' ', ' ', ' ',]]
current_player = "X"
game_over = False
buttons  = [[None for _ in range(3)] for _ in range (3)]



def create_window():
    window = tk.Tk()
    window.title("Tic-Tac-Toe")

    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text='', font=BUTTON_FONT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                               padx=0, pady=0, relief='flat', borderwidth=0,
                               command=lambda row=i, col=j: on_click(row, col))
            button.grid(row=i, column=j)
            buttons[i][j] = button

    return window


def on_click(row, col):
    global current_player, game_over
    if board[row][col] == " " and not game_over:
        board[row][col] = current_player
        text_color = 'blue' if current_player == 'X' else 'red'
        buttons[row][col].config(text=current_player, fg=text_color, state="disabled")
        buttons[row][col].update()
        print(f"Button clicked at row {row}, column {col}")

    # check if the game was won
    if check_winner(current_player):
        print(f"Player {current_player} wins!")
        game_over = True
    elif check_draw():
        print("Draw!")
        game_over = True
    else:
        current_player = "O" if current_player == "X" else "X"

def check_winner(player):
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw():
    if not any(" " in row for row in board):
        return True
    return False


if __name__ == "__main__":
    game_window = create_window()
    game_window.mainloop()