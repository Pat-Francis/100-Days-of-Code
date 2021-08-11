from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

WIDTH = 800
HEIGHT = 600
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
score = Score()
ball = Ball()

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "o")
screen.onkey(right_paddle.down, "l")

game_running = True
while game_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.update()

    # Detect collision with ball and top/bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddles
    if ball.xcor() > 325 and ball.distance(right_paddle) < 50 or ball.xcor() < -325 and ball.distance(left_paddle) < 50:
        ball.x_bounce()

    # Detect right_paddle miss, increment left players score
    if ball.xcor() > 380:
        ball.x_bounce()
        ball.reset_position()
        score.left_point()

    # Detect left_paddle miss, increment right players score
    if ball.xcor() < -380:
        ball.x_bounce()
        ball.reset_position()
        score.right_point()

screen.exitonclick()
