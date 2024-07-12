import random
from turtle import Turtle

# Constants
RANDOM_BALL_SPEEDS = (4, 5, 6)
DEFAULT_BALL_SPEED = 5


class Ball(Turtle):
    def __init__(self, speed, ypos):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("teal")
        self.goto(0, ypos)
        self.speed("fastest")
        self.x_move = random.choice((DEFAULT_BALL_SPEED, -DEFAULT_BALL_SPEED))  # random initial start direction
        self.y_move = DEFAULT_BALL_SPEED
        self.move_speed = speed

    def move(self):
        # set new coordinates
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # move the ball to the new coordinates
        self.goto(new_x, new_y)

    def bounce_y(self, overshoot):
        # reverse ball direction in y-axis aka bounce
        self.y_move *= -1

        if self.y_move < 0:
            # if the ball is moving to the left, set a new random speed
            # then make it negative, moving the ball to the left
            self.y_move = random.choice(RANDOM_BALL_SPEEDS) * -1
        else:
            # if the ball is moving to the right, set a new random speed
            self.y_move = random.choice(RANDOM_BALL_SPEEDS)

        # set new y coordinate position.
        # Overshoot is the distance the ball overshot the wall.
        # The ball will hit the wall and travel the distance it overshot the wall in the opposite direction.
        # This should appear as a bounce.
        new_y = self.ycor() - overshoot

        # set new ball y position
        self.sety(new_y)

    def bounce_x(self, overshoot):
        self.x_move *= -1
        if self.x_move < 0:
            self.x_move = random.choice(RANDOM_BALL_SPEEDS) * -1
        else:
            self.x_move = random.choice(RANDOM_BALL_SPEEDS)
        new_x = self.xcor() - overshoot
        self.setx(new_x)

    def reset_pos(self, ypos):
        """
        Move the ball to default starting position and speed.
        """
        # set ball to center screen at determined height
        self.goto(0, ypos)
        # set y motion to default speed
        self.y_move = DEFAULT_BALL_SPEED

