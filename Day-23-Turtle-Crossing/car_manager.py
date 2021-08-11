import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            start_x = 300
            start_y = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.speed("fastest")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(start_x, start_y)
            self.all_cars.append(new_car)

    def update(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
