import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
level = 0
cars = CarManager()
player = Player()
screen.listen()
screen.onkey(player.up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.create_car()
    cars.update()

    # Detect if the turtle comes into contact with a car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect if the turtle gets to the finish line, if so increment car speed
    if player.finish_check():
        player.go_to_start()
        cars.speed_up()

    screen.update()
screen.exitonclick()