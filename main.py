import time
from turtle import Screen

from ball import Ball
from bricks import Bricks
from paddle import Paddle
from scoreboard import Scoreboard

# Global Variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BALL_STARTING_SPEED = 0.02  # default 0.02
BALL_STARTING_YPOS = -200
PADDLE_STARTING_YPOS = -250
PADDLE_STRETCH = 10
GAME_TITLE = "Breakout!"
BRICK_ROW_COLORS = ["#F4EDCC", "#A4CE95", "#6196A6", "#5F5D9C"]
WALL_OFFSET = 10
STARTING_BALL_COUNT = 4

game_over_text = "GAME OVER!"
rows_of_bricks = [[], [], [], []]
level = 0
paddle_width = PADDLE_STRETCH

# build environment / screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title(GAME_TITLE)
screen.tracer(0)

# place scoreboard
scoreboard = Scoreboard(SCREEN_HEIGHT, STARTING_BALL_COUNT)


def place_bricks():
    """
    Place bricks on screen
    Store bricks in a 2d array
    """
    global rows_of_bricks
    rows_of_bricks = [[], [], [], []]
    for i, row in enumerate(rows_of_bricks):
        number_of_bricks = int((SCREEN_WIDTH / 70))
        for each_brick in range(number_of_bricks):
            x_pos = (SCREEN_WIDTH / 2) - (each_brick * 70) - 50
            brick = Bricks(BRICK_ROW_COLORS[i], xpos=x_pos, ypos=(i * 30) + 100)
            rows_of_bricks[i].append(brick)


# place bricks on screen
place_bricks()

# place paddle on screen
paddle = Paddle(PADDLE_STARTING_YPOS, SCREEN_WIDTH, PADDLE_STRETCH, screen=screen)

# place ball on screen
ball = Ball(speed=BALL_STARTING_SPEED, ypos=BALL_STARTING_YPOS)

# Change paddle position based on key input
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

# Gameplay begins here
while scoreboard.balls > 0:
    time.sleep(ball.move_speed)  # Slow the game down
    ball.move()

    """
    Wall and paddle Collision logic
    Detect when the ball has hit or passed the edge of wall/paddle y_diff or x_diff
    Calculate how far the ball has gone beyond the edge
    Move the ball double that distance in the opposite direction (bounce)
        * bounce* 1x gets ball back to edge 2x gets ball bounce distance
    Reverse the ball's movement
    """

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
    if ball.distance(paddle) < (10 * paddle_width) and ball.ycor() < PADDLE_STARTING_YPOS + 20 and ball.y_move < 0:
        y_diff = int(ball.ycor() - (PADDLE_STARTING_YPOS + 20))
        if y_diff > -10:
            ball.bounce_y(y_diff * 2)
        else:
            ball.bounce_x(ball.x_move * 3)

    # Detect ball hits bottom of screen
    if ball.ycor() < -(SCREEN_HEIGHT / 2) - 100:
        ball.reset_pos(BALL_STARTING_YPOS)
        paddle.reset_pos()
        scoreboard.balls -= 1

    # Detect brick collision and count remaining bricks to detect end of level
    remaining_bricks = 0
    for row in rows_of_bricks:
        remaining_bricks += len(row)
        for brick in row:
            # 43 compensates for the round ball hitting brick corners
            if ball.distance(brick) < 43 and brick.ycor() - 20 < ball.ycor() < brick.ycor() + 20:
                brick.sety(SCREEN_HEIGHT)  # move the brick off screen
                row.remove(brick)  # delete the brick from memory
                scoreboard.score += 10
                ball.bounce_y(0)
    if remaining_bricks == 0:
        level += 1
        paddle_width = max(3, PADDLE_STRETCH - level)
        ball.reset_pos(BALL_STARTING_YPOS)
        place_bricks()
        paddle.shapesize(stretch_len=paddle_width, stretch_wid=1.0)

    # update scoreboard
    scoreboard.draw_scoreboard()
    screen.update()

scoreboard.game_over(game_over_text)

screen.mainloop()
