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
        self.x_move = random.choice((5, -5))
        self.y_move = DEFAULT_BALL_SPEED
        self.move_speed = speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self, overshoot):
        self.y_move *= -1
        if self.y_move < 0:
            self.y_move = random.choice(RANDOM_BALL_SPEEDS) * -1
        else:
            self.y_move = random.choice(RANDOM_BALL_SPEEDS)
        new_y = self.ycor() - overshoot
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
        self.goto(0, ypos)
        self.y_move = DEFAULT_BALL_SPEED

