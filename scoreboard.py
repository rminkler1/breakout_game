from turtle import Turtle
from constants import *




class Scoreboard(Turtle):
    def __init__(self, screen_height, balls):
        super().__init__()
        self.penup()
        self.color("gray")
        self.speed("fastest")
        self.goto(0, (screen_height // 2) - SCOREBOARD_POSITION)
        self.hideturtle()
        self.balls = balls
        self.score = 0

        self.draw_scoreboard()


    def draw_scoreboard(self):
        self.clear()
        scoreboard_text = f"SCORE: {self.score}                     BALLS REMAINING: {max(0, self.balls - 1)}"
        self.write(arg=scoreboard_text, align=ALIGNMENT, font=FONT)

    def game_over(self, screen_message):
        self.setposition(0, 0)
        self.write(arg=screen_message, align="center", font=BIG_FONT)