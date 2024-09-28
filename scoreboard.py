from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.level = 1
        self.goto((-250,250))
        self.write(f"Level = {self.level}",False, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Level = {self.level}",False, font=FONT)

    def inc_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False, font=FONT)
