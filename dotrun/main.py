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
BG_COLOR = '#C0C0C0'
NO_SPAWN_COLOR = '#90EE90'
START_X = SPACE_SIZE
START_Y = (GAME_HEIGHT / 2) - (SPACE_SIZE / 2)
SPAWN_TIME = 2000
MIN_SPAWN_TIME = 250
GAME_OVER = False
NO_SPAWN_ZONE =  2 * SPACE_SIZE


# Classes

class Dot():
    def __init__(self) -> None:
        self.shape = canvas.create_rectangle(START_X, START_Y, START_X + SPACE_SIZE, START_Y + SPACE_SIZE, fill=DOT_COLOR)


class Entity():
     def __init__(self) -> None:
        self.color = random.choice(ENTITY_COLORS)
        self.length = random.randint(2, 4) * SPACE_SIZE  
        self.x = random.randint(2 * SPACE_SIZE, GAME_WIDTH - self.length - (2 * SPACE_SIZE))
        self.y = -random.randint(1, 4) * SPACE_SIZE
        self.shape = canvas.create_rectangle(self.x, self.y, self.x + SPACE_SIZE, self.y + self.length, fill=self.color, tag='entity')

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
    global SPEED, SPAWN_TIME, score  

    x0, y0, x1, y1 = canvas.coords(dot.shape)
    if x1 >= GAME_WIDTH:
        score += 1  # Increment  score
        label.config(text=f"Score:{score}")  # Update score
        SPEED = max(SPEED - 10, MIN_SPEED)  # Decrease speed (entities will move faster)
        SPAWN_TIME = max(SPAWN_TIME - 100, MIN_SPAWN_TIME)
        reset_dot()  

def reset_dot():
    """Reset the dot to  starting position"""
    canvas.coords(dot.shape, START_X, START_Y, START_X + SPACE_SIZE, START_Y + SPACE_SIZE)

def move_entities():
    for entity in entities:
        canvas.move(entity.shape, 0, SPACE_SIZE / 2)

    window.after(SPEED, move_entities)

def spawn_entity():
    if not GAME_OVER:
        new_entity = Entity()
        entities.append(new_entity)
        window.after(SPAWN_TIME, spawn_entity)  # Schedule next spawn

        


def start_game():
    spawn_entity()  # Start spawning entities
    move_entities()  # Start moving entities

def check_collision():
    dot_coords = canvas.coords(dot.shape)  # [x1, y1, x2, y2] for the dot
    for entity in entities:
        entity_coords = canvas.coords(entity.shape)  # [x1, y1, x2, y2] for the entity
        # Check if the dot and ane entity collide
        if (dot_coords[2] > entity_coords[0] and
            dot_coords[0] < entity_coords[2] and
            dot_coords[3] > entity_coords[1] and
            dot_coords[1] < entity_coords[3]):
            game_over()  # end game if yes
            return

    window.after(50, check_collision)  # check collisions every 50 ms


def game_over():
    global GAME_OVER
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font='arial, 50', fill='red', text='GAME OVER \n Score: {}'.format(score) ,tag='gameover')
    GAME_OVER = True





# Game window

window = Tk()
window.title('DOTRUN')
window.resizable(False, False)

score = 0
label = Label(window, text="Score:{}".format(score), font=('arial', 38))
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

canvas.create_rectangle(0, 0, NO_SPAWN_ZONE, GAME_HEIGHT, fill=NO_SPAWN_COLOR, outline='')
canvas.create_rectangle(GAME_WIDTH - NO_SPAWN_ZONE, 0, GAME_WIDTH, GAME_HEIGHT, fill=NO_SPAWN_COLOR, outline='')

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
entities = []  # Initialize a list for entities



dot = Dot()
start_game()
check_collision()

window.mainloop()