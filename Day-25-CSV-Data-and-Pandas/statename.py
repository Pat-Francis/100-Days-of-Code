from turtle import Turtle


class StateName(Turtle):
    def __init__(self, state_name, x_coord, y_coord):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x_coord, y_coord)
        self.speed("fastest")
        self.write(state_name)
