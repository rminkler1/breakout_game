from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, ypos, screen_width):
        super().__init__()
        self.color("white")
        self.setheading(0)
        self.shapesize(stretch_len=10.0, stretch_wid=1.0)
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.sety(ypos)
        self.window_width = screen_width

    def move_right(self):
        if self.window_width / 2 > self.xcor():
            self.forward(20)

    def move_left(self):
        if -(self.window_width / 2) < self.xcor():
            self.back(20)
