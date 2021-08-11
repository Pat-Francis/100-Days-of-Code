from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-290, 260)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)
