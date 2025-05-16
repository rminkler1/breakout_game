from turtle import Turtle

from constants import *


class Scoreboard(Turtle):
    def __init__(self, balls):
        super().__init__()
        self.penup()
        self.color("gray")
        self.speed("fastest")
        self.cursor_home()
        self.hideturtle()
        self.starting_balls = balls
        self.balls = balls
        self.score = 0

        self.draw_scoreboard()

    def draw_scoreboard(self):
        """
        Draw the scoreboard at the top of the screen
        """
        self.clear()
        self.cursor_home()
        scoreboard_text = f"SCORE: {self.score}                     BALLS REMAINING: {max(0, self.balls - 1)}"
        self.write(arg=scoreboard_text, align=ALIGNMENT, font=FONT)

    def game_pause_message(self, screen_message: str):
        """
        Write Message in center of screen
        """
        self.cursor_center()
        self.write(arg=screen_message, align="center", font=BIG_FONT)

    def cursor_home(self):
        """
        Move cursor to top of screen
        """
        self.setposition(0, (SCREEN_HEIGHT // 2) - SCOREBOARD_POSITION)

    def cursor_center(self):
        """
        Move cursor to center of screen
        """
        self.setposition(0, 0)

    def reset(self):
        self.score = 0
        self.balls = self.starting_balls
        self.clear()
