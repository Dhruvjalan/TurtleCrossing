from turtle import Turtle
from random import randrange
COLORS = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.penup()
        self.color(COLORS[randrange(0, len(COLORS))])
        self.goto(280, randrange(-280, 230))

    def move(self, level):
        dec_x = STARTING_MOVE_DISTANCE + (level-1)*MOVE_INCREMENT
        self.goto((self.xcor()-dec_x, self.ycor()))
