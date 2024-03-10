from turtle import Turtle
import random

random_ball_speeds = (11, 10, 9)


class Ball(Turtle):
    def __init__(self, speed, ypos):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.setposition(0, ypos)
        self.speed("fastest")
        self.x_move = random.choice((10, -10))
        self.y_move = -10
        self.move_speed = speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        if self.y_move < 0:
            self.y_move = random.choice(random_ball_speeds) * -1
        else:
            self.y_move = random.choice(random_ball_speeds)

    def bounce_x(self):
        self.x_move *= -1
        if self.x_move < 0:
            self.x_move = random.choice(random_ball_speeds) * -1
        else:
            self.x_move = random.choice(random_ball_speeds)


