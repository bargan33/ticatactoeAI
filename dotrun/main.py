# Imports
from tkinter import *
import random

# Constants
GAME_HEIGHT = 800
GAME_WIDTH = 800
SPEED = 100
MIN_SPEED = 20
SPACE_SIZE = 30
DOT_COLOR = 'red'
ENTITY_COLORS = ['blue', 'green', 'yellow', 'orange', 'black', 'cyan']
BG_COLOR = '#FFFFFF'
START_X = SPACE_SIZE
START_Y = (GAME_HEIGHT / 2) - (SPACE_SIZE / 2)


# Classes

class Dot():
    def __init__(self) -> None:
        self.shape = canvas.create_rectangle(START_X, START_Y, START_X + SPACE_SIZE, START_Y + SPACE_SIZE, fill=DOT_COLOR)


class Entity():
    pass

# Functions 

def move(direction):
    x0, y0, x1, y1 = canvas.coords(dot.shape)  # Get current coordinates of the dot
    if direction == 'up' and y0 > 0:
        canvas.move(dot.shape, 0, -SPACE_SIZE)
    elif direction == 'down' and y1 < GAME_HEIGHT:
        canvas.move(dot.shape, 0, SPACE_SIZE)
    elif direction == 'left' and x0 > 0:
        canvas.move(dot.shape, -SPACE_SIZE, 0)
    elif direction == 'right' and x1 < GAME_WIDTH:
        canvas.move(dot.shape, SPACE_SIZE, 0)

        check_reached_right_side()

def check_reached_right_side():
    global SPEED, score  

    x0, y0, x1, y1 = canvas.coords(dot.shape)
    if x1 >= GAME_WIDTH:
        score += 1  # Increment  score
        label.config(text=f"Score:{score}")  # Update score
        SPEED = max(SPEED - 10, MIN_SPEED)  # Decrease speed (entities will move faster)
        reset_dot()  

def reset_dot():
    """Reset the dot to  starting position"""
    canvas.coords(dot.shape, START_X, START_Y, START_X + SPACE_SIZE, START_Y + SPACE_SIZE)

def entity_move(entity):
    pass

def check_collision(dot, entities):
    pass

def game_over():
    pass



# Game window

window = Tk()
window.title('DOTRUN')
window.resizable(False, False)

score = 0
label = Label(window, text="Score:{}".format(score), font=('arial', 38))
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# keybinds

window.bind("<w>", lambda event: move('up'))
window.bind("<s>", lambda event: move('down'))
window.bind("<a>", lambda event: move('left'))
window.bind("<d>", lambda event: move('right'))


# start game

dot = Dot()

window.mainloop()