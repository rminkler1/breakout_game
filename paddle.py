from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, ypos):
        super().__init__()
        self.color("white")
        self.setheading(0)
        self.shapesize(stretch_len=10.0, stretch_wid=1.0)
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.sety(ypos)

    def move_right(self):
        self.forward(20)

    def move_left(self):
        self.back(20)
