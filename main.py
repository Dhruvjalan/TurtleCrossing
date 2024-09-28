import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars_list = []
rep = 0

score = Scoreboard()


for i in range(5):
    car = CarManager()
    cars_list.append(car)

player = Player()

screen.listen()
screen.onkey(player.go_forward, "Up")
screen.onkey(player.go_back, "Down")

game_is_on = True
while game_is_on:
    rep += 1
    time.sleep(0.1)
    screen.update()
    if rep % 10 == 0:
        car = CarManager()
        cars_list.append(car)

    if player.ycor() > 280:
        player.goto(0, -280)
        score.inc_score()

    for car_object in cars_list:
        car_object.move(score.level)
        if car_object.distance(player) < 20:
            game_is_on = False
            print("Collision")
            score.game_over()
