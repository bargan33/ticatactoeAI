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


# Classes

class Dot():
    pass

class Entity():
    pass

# Functions 

def move():
    pass

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

canvas = Canvas(window, bg=BG_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.mainloop()