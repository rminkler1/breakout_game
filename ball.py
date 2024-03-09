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
        # self.x_move = random.choice(choice)
        # self.y_move = random.choice(choice)
        # self.move_speed = speed


