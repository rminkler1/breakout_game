from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from bricks import Bricks
import time


# Global Variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BALL_STARTING_SPEED = 0.05
BALL_STARTING_YPOS = -100
PADDLE_STARTING_YPOS = -250
GAME_TITLE = "Breakout!"
BRICK_ROW_COLORS = ["yellow", "green", "orange", "red"]
WALL_OFFSET = 15


# build environment / screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title(GAME_TITLE)
screen.tracer(0)

# Place bricks on screen
# store bricks in a 2d array
rows = [[], [], [], []]

for i, row in enumerate(rows):
    number_of_bricks = int((SCREEN_WIDTH / 70))
    for each_brick in range(number_of_bricks):
        x_pos = (SCREEN_WIDTH / 2) - (each_brick * 70) - 50
        brick = Bricks(BRICK_ROW_COLORS[i], xpos=x_pos, ypos=(i*30)+100)
        rows[i].append(brick)

# place paddle on screen
paddle = Paddle(PADDLE_STARTING_YPOS, SCREEN_WIDTH)

# place ball on screen
ball = Ball(speed=BALL_STARTING_SPEED, ypos=BALL_STARTING_YPOS)



# TODO: paddle collision

# Change paddle position based on key input
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

# TODO: brick collision

# TODO: update scoreboard


while True:
    time.sleep(ball.move_speed)     # Slow the game down
    # Detect wall collisions
    if ball.ycor() > (SCREEN_HEIGHT / 2) - WALL_OFFSET or ball.ycor() < -(SCREEN_HEIGHT / 2) + WALL_OFFSET:
        ball.bounce_y()
    elif ball.xcor() > (SCREEN_WIDTH / 2) - WALL_OFFSET or ball.xcor() < -(SCREEN_WIDTH / 2) + WALL_OFFSET:
        ball.bounce_x()

    ball.move()
    screen.update()

screen.mainloop()
