from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def reset():
    # tim.home()
    tim.reset()


screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(reset, "c")
screen.exitonclick()
