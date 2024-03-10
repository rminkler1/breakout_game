import time
from turtle import Screen

from ball import Ball
from bricks import Bricks
from paddle import Paddle

# Global Variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BALL_STARTING_SPEED = 0.02
BALL_STARTING_YPOS = -200
PADDLE_STARTING_YPOS = -250
PADDLE_STRETCH = 10
GAME_TITLE = "Breakout!"
BRICK_ROW_COLORS = ["yellow", "green", "orange", "red"]
WALL_OFFSET = 10

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
        brick = Bricks(BRICK_ROW_COLORS[i], xpos=x_pos, ypos=(i * 30) + 100)
        rows[i].append(brick)

# place paddle on screen
paddle = Paddle(PADDLE_STARTING_YPOS, SCREEN_WIDTH, PADDLE_STRETCH, screen=screen)

# place ball on screen
ball = Ball(speed=BALL_STARTING_SPEED, ypos=BALL_STARTING_YPOS)

# Change paddle position based on key input
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

while True:
    time.sleep(ball.move_speed)  # Slow the game down
    ball.move()

    # Detect roof collision
    if ball.ycor() > (SCREEN_HEIGHT / 2) - WALL_OFFSET and ball.y_move > 0:
        y_diff = int(ball.ycor() - ((SCREEN_HEIGHT / 2) - WALL_OFFSET))
        ball.bounce_y(y_diff * 2)

    # Detect right wall collisions - extra 10 px needed to bounce off wall
    if ball.xcor() > (SCREEN_WIDTH / 2) - WALL_OFFSET - 10 and ball.x_move > 0:
        x_diff = int(ball.xcor() - ((SCREEN_WIDTH / 2) - WALL_OFFSET - 10))
        ball.bounce_x(x_diff * 2)

    # Detect left wall collisions
    if ball.xcor() < -(SCREEN_WIDTH / 2) + WALL_OFFSET and ball.x_move < 0:
        x_diff = int(ball.xcor() + ((SCREEN_WIDTH / 2) - WALL_OFFSET))
        ball.bounce_x(x_diff * 2)

    # Detect collision with paddle top
    if ball.distance(paddle) < (10 * PADDLE_STRETCH) and ball.ycor() < PADDLE_STARTING_YPOS + 20 and ball.y_move < 0:
        y_diff = int(ball.ycor() - (PADDLE_STARTING_YPOS + 20))
        ball.bounce_y(y_diff * 2)

    # TODO: brick collision

    # TODO: update scoreboard

    screen.update()

screen.mainloop()
