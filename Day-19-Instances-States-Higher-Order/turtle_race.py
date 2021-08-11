from turtle import Turtle, Screen
from random import randint

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?  Enter a colour.")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["time", "jim", "slim", "mary", "betty", "bob"]
lane_pos = [-100, -60, -20, 20, 60, 100]

for x in range(0, 6):
    names[x] = Turtle(shape="turtle")
    names[x].color(colours[x])
    names[x].penup()
    names[x].goto(x=-230, y=lane_pos[x])

if user_bet:
    race_is_on = True

while race_is_on:
    for y in range(0, 6):
        random_distance = randint(0, 10)
        names[y].forward(random_distance)
        if names[y].xcor() >= 230:
            race_is_on = False
            if user_bet == names[y].color:
                print(f"Congratulations, you won!  {colours[y]} won the race.")
            else:
                print(f"Unlucky, you lost.  {colours[y]} won the race.")
screen.exitonclick()
