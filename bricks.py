from turtle import Turtle


class Bricks(Turtle):
    def __init__(self, color, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(color)
        self.setposition(xpos, ypos)
        self.shapesize(stretch_len=3.0, stretch_wid=1.0)


