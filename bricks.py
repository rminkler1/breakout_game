from turtle import Turtle
from constants import *


class Bricks(Turtle):

    def __init__(self, color:str, xpos:int, ypos:int):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(color)
        self.setposition(xpos, ypos)
        self.shapesize(stretch_len=BRICK_WIDTH, stretch_wid=BRICK_HEIGHT)


