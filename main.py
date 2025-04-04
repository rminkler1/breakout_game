import time
from turtle import Screen

from ball import Ball
from bricks import Bricks
from constants import *
from paddle import Paddle
from scoreboard import Scoreboard


class Game:

    def __init__(self):
        # setup game elements
        self.rows_of_bricks = [[], [], [], []]
        self.level = 0

        # track time to adjust sleep cycle
        self.start_time = time.time()

        # build environment / screen
        self.screen = Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor(BG_COLOR)
        self.screen.title(GAME_TITLE)
        self.screen.tracer(0)

        # place scoreboard
        self.scoreboard = Scoreboard(SCREEN_HEIGHT, STARTING_BALL_COUNT)

        # place bricks on screen
        self.place_bricks()

        # place paddle on screen
        self.paddle = Paddle(PADDLE_STARTING_YPOS, SCREEN_WIDTH, PADDLE_STRETCH, screen=self.screen)

        # place ball on screen
        self.ball = Ball(speed=BALL_STARTING_SPEED, ypos=BALL_STARTING_YPOS)

    def run(self):
        # Change paddle position based on key input
        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_right, "Right")
        self.screen.onkeypress(self.paddle.move_left, "Left")

        # Gameplay begins here
        while self.scoreboard.balls > 0:

            # sleep based on the delay time minus the time that has already passed.
            # Reduces the impact of processing time on the gameplay while slowing things down to an appropriate speed.
            sleep_time = self.ball.move_speed - (time.time() - self.start_time)
            if sleep_time > 0:
                time.sleep(sleep_time)  # Slow the game down

            # Get current time to know how much time has elapsed
            self.start_time = time.time()

            self.ball.move()

            """
            Wall and paddle Collision logic
            Detect when the ball has passed the boundary
            Calculate how far the ball has gone beyond the edge -- y_diff or x_diff
            Move the ball double that distance in the opposite direction (bounce)
                * bounce* 1x gets ball back to edge 2x gets ball bounce distance
            Reverse the ball's movement
            """

            # handle wall collisions
            self.wall_collisions()

            # handle paddle collisions
            self.paddle_collision()

            # handle brick collisions
            self.brick_collision()

            # handle ball leaves bottom of screen
            if self.ball.ycor() < SCREEN_BOTTOM:
                # reset ball position, paddle position, and lose one ball
                self.ball.reset_pos(BALL_STARTING_YPOS)
                self.paddle.reset_pos()
                self.scoreboard.balls -= 1

            # update scoreboard and redraw screen
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
        bricks_per_row = SCREEN_WIDTH // BRICK_WIDTH_PX

        for i, row_ in enumerate(self.rows_of_bricks):
            for each_brick in range(bricks_per_row):
                x_pos = HALF_SCREEN - (each_brick * BRICK_WIDTH_PX) - 50
                brick_ = Bricks(BRICK_ROW_COLORS[i], xpos=x_pos, ypos=(i * 30) + 100)
                self.rows_of_bricks[i].append(brick_)

    def brick_collision(self):
        # Detect brick collision and count remaining bricks to detect end of level
        remaining_bricks = 0
        for row in self.rows_of_bricks:
            remaining_bricks += len(row)
            for brick in row:
                # 43 compensates for the round ball hitting brick corners
                if self.ball.distance(brick) < 43 and brick.ycor() - 20 < self.ball.ycor() < brick.ycor() + 20:
                    brick.sety(SCREEN_HEIGHT)  # move the brick off-screen
                    row.remove(brick)  # delete the brick from memory
                    self.scoreboard.score += 10
                    self.ball.bounce_y(0)

        if remaining_bricks == 0:
            self.level += 1
            paddle_width = max(3, PADDLE_STRETCH - self.level)
            self.ball.reset_pos(BALL_STARTING_YPOS)
            self.place_bricks()
            self.paddle.shapesize(stretch_len=paddle_width, stretch_wid=1.0)

    def wall_collisions(self):
        # Detect roof collision
        if self.ball.ycor() > SCREEN_TOP and self.ball.y_move > 0:
            y_diff = self.ball.ycor() - SCREEN_TOP
            self.ball.bounce_y(y_diff * 2)

        # Detect right wall collisions
        if self.ball.xcor() > SCREEN_RIGHT and self.ball.x_move > 0:
            x_diff = self.ball.xcor() - SCREEN_RIGHT
            self.ball.bounce_x(x_diff * 2)

        # Detect left wall collisions
        if self.ball.xcor() < SCREEN_LEFT and self.ball.x_move < 0:
            x_diff = self.ball.xcor() - SCREEN_LEFT
            self.ball.bounce_x(x_diff * 2)

    def paddle_collision(self):

        # Detect collision with paddle top
        if (    self.ball.ycor() < PADDLE_TOP                           # ball is below paddle top
                and self.ball.distance(self.paddle) < PADDLE_WIDTH      # ball is within the paddle width
                and self.ball.y_move < 0                                # ball is moving down (negative y)
        ):
            y_diff = self.ball.ycor() - PADDLE_TOP                      # ball distance beyond paddle top
            # bounce off sides or top of paddle

            # the ball enters from the top of the paddle, it can not exceed 10px into the paddle..
            if y_diff > -10:
                self.ball.bounce_y(y_diff * 2)                          # bounce off top of paddle
            else:
                self.ball.bounce_x(self.ball.x_move * 3)                # bounce off side of paddle


if __name__ == '__main__':
    game = Game()
    game.run()
