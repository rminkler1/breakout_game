import time
from turtle import Screen

from ball import Ball
from bricks import Bricks
from paddle import Paddle
from scoreboard import Scoreboard
from constants import *


class Game:
    def __init__(self):
        # setup game elements
        self.rows_of_bricks = [[], [], [], []]
        self.level = 0

        # build environment / screen
        self.screen = Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title(GAME_TITLE)
        self.screen.tracer(0)

        # place scoreboard
        self.scoreboard = Scoreboard(SCREEN_HEIGHT, STARTING_BALL_COUNT)

    def run(self):
        # place bricks on screen
        self.place_bricks()

        # place paddle on screen
        paddle = Paddle(PADDLE_STARTING_YPOS, SCREEN_WIDTH, PADDLE_STRETCH, screen=self.screen)

        # place ball on screen
        ball = Ball(speed=BALL_STARTING_SPEED, ypos=BALL_STARTING_YPOS)

        # Change paddle position based on key input
        self.screen.listen()
        self.screen.onkeypress(paddle.move_right, "Right")
        self.screen.onkeypress(paddle.move_left, "Left")

        # Gameplay begins here
        while self.scoreboard.balls > 0:
            time.sleep(ball.move_speed)  # Slow the game down
            ball.move()

            """
            Wall and paddle Collision logic
            Detect when the ball has hit or passed the edge of wall/paddle
            Calculate how far the ball has gone beyond the edge -- y_diff or x_diff
            Move the ball double that distance in the opposite direction (bounce)
                * bounce* 1x gets ball back to edge 2x gets ball bounce distance
            Reverse the ball's movement
            """

            # Detect roof collision
            if ball.ycor() > HALF_SCREEN - WALL_OFFSET and ball.y_move > 0:
                y_diff = int(ball.ycor() - ((SCREEN_HEIGHT / 2) - WALL_OFFSET))
                ball.bounce_y(y_diff * 2)

            # Detect right wall collisions - extra 10 px needed to bounce off wall
            if ball.xcor() > HALF_SCREEN - WALL_OFFSET - 10 and ball.x_move > 0:
                x_diff = int(ball.xcor() - (HALF_SCREEN - WALL_OFFSET - 10))
                ball.bounce_x(x_diff * 2)

            # Detect left wall collisions
            if ball.xcor() < -HALF_SCREEN + WALL_OFFSET and ball.x_move < 0:
                x_diff = int(ball.xcor() + (HALF_SCREEN - WALL_OFFSET))
                ball.bounce_x(x_diff * 2)

            # Detect collision with paddle top
            if ball.distance(paddle) < (10 * PADDLE_STRETCH) and ball.ycor() < PADDLE_STARTING_YPOS + 20 and ball.y_move < 0:
                y_diff = int(ball.ycor() - (PADDLE_STARTING_YPOS + 20))
                # bounce off sides or top of paddle
                if y_diff > -10:
                    ball.bounce_y(y_diff * 2)
                else:
                    ball.bounce_x(ball.x_move * 3)

            # Detect ball hits bottom of screen
            if ball.ycor() < -HALF_SCREEN - 100:
                ball.reset_pos(BALL_STARTING_YPOS)
                paddle.reset_pos()
                self.scoreboard.balls -= 1

            # Detect brick collision and count remaining bricks to detect end of level
            remaining_bricks = 0
            for row in self.rows_of_bricks:
                remaining_bricks += len(row)
                for brick in row:
                    # 43 compensates for the round ball hitting brick corners
                    if ball.distance(brick) < 43 and brick.ycor() - 20 < ball.ycor() < brick.ycor() + 20:
                        brick.sety(SCREEN_HEIGHT)  # move the brick off-screen
                        row.remove(brick)  # delete the brick from memory
                        self.scoreboard.score += 10
                        ball.bounce_y(0)
            if remaining_bricks == 0:
                self.level += 1
                paddle_width = max(3, PADDLE_STRETCH - self.level)
                ball.reset_pos(BALL_STARTING_YPOS)
                self.place_bricks()
                paddle.shapesize(stretch_len=paddle_width, stretch_wid=1.0)

            # update scoreboard
            self.scoreboard.draw_scoreboard()
            self.screen.update()

        self.scoreboard.game_over(GAME_OVER_TEXT)

        self.screen.mainloop()

    def place_bricks(self):
        """
        Place bricks on screen
        Store bricks in a 2d array
        """
        # calculate the number of bricks that can fit on screen in each row
        bricks_per_row = int((SCREEN_WIDTH / BRICK_WIDTH_PX))

        for i, row_ in enumerate(self.rows_of_bricks):
            for each_brick in range(bricks_per_row):
                x_pos = HALF_SCREEN - (each_brick * BRICK_WIDTH_PX) - 50
                brick_ = Bricks(BRICK_ROW_COLORS[i], xpos=x_pos, ypos=(i * 30) + 100)
                self.rows_of_bricks[i].append(brick_)

if __name__ == '__main__':
    game = Game()
    game.run()