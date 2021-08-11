from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.font = ('Courier', 30, 'bold')
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.left_score, font=self.font)
        self.goto(100, 240)
        self.write(self.right_score, font=self.font)

    def left_point(self):
        self.left_score += 1
        self.update()

    def right_point(self):
        self.right_score += 1

        self.update()
