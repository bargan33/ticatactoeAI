#basic python snake
import random
from tkinter import *

WIDTH = 800
HEIGHT = 800
SPEED = 100
MIN_SPEED = 20
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = 'blue'
COOKIE_COLOR = 'red'
BG_COLOR = '#FFFFFF'

# Classes
class Snake:
    def __init__(self) -> None:
        self.bodysize = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range (0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag='snake')
            self.squares.append(square)

class Cookie:
    def __init__(self, snake_coordinates) -> None:
        while True:
            x = random.randint(0, (WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x, y]

            overlapping = False
            for part in snake_coordinates:
                if part[0] == x and part[1] == y:
                    overlapping = True
                    break

            if not overlapping:
                break

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COOKIE_COLOR, tag='cookie')



# Funcs

def next_move(snake, cookie):
    x, y = snake.coordinates[0]
    if dir == 'up':
        y -= SPACE_SIZE
    elif dir == 'down':
        y += SPACE_SIZE
    elif dir == 'left':
        x -= SPACE_SIZE
    elif dir == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == cookie.coordinates[0] and y == cookie.coordinates[1]:
        global score, SPEED
        score += 1

        label.config(text="Score:{}".format(score))  
        canvas.delete('cookie')
        cookie = Cookie(snake.coordinates)

        if score % 5 == 0 and SPEED > MIN_SPEED:
            SPEED = max(SPEED - 5, MIN_SPEED)
        
    else:
        del(snake.coordinates[-1])
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_col(snake):
        game_over()
    

    else:
        window.after(SPEED, next_move, snake, cookie)

def change_dir(new_dir):
    global dir

    if new_dir == 'left' and dir != 'right':
        dir = new_dir

    elif new_dir == 'right' and dir != 'left':
        dir = new_dir
    
    elif new_dir == 'up' and dir != 'down':
        dir = new_dir

    elif new_dir == 'down' and dir != 'up':
        dir = new_dir
    

def check_col(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= WIDTH:
        return True
    elif y < 0 or y >= HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
        
    return False
    

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font='arial, 50', fill='red', text='GAME OVER \n Score: {}'.format(score) ,tag='gameover')


window = Tk()
window.title('SSSSnake')
window.resizable(False, False)

score = 0
dir = 'down'
label = Label(window, text="Score:{}".format(score), font=('arial', 38))
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Up>', lambda event: change_dir('up'))
window.bind('<Down>', lambda event: change_dir('down'))
window.bind('<Left>', lambda event: change_dir('left'))
window.bind('<Right>', lambda event: change_dir('right'))

snake = Snake()
cookie = Cookie(snake.coordinates)

next_move(snake, cookie)

window.mainloop()