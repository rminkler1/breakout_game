from turtle import Turtle
import random

choice = (10, -10)


class Ball(Turtle):
    def __init__(self, speed, ypos):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.setposition(0, ypos)
        self.speed("fastest")
        self.x_move = random.choice(choice)
        self.y_move = -10
        self.move_speed = speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move()

    def bounce_x(self):
        self.x_move *= -1
        self.move()


