import turtle
from turtle import Turtle, Screen
import random
# import colorgram
timmy = Turtle()
turtle.colormode(255)


# Challenge 1 - Draw a Square
def challenge1():
    for x in range(0, 4):
        timmy.forward(100)
        timmy.right(90)


# Challenge 2 - Draw a dashed line
def challenge2():
    for x in range(15):
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()


# Challenge 3 - Draw different consecutive shapes (triangle to decagon)
def challenge3():
    degrees = 360

    for sides in range(3, 11):
        timmy.pencolor((random.random(), random.random(), random.random()))
        for x in range(sides):
            timmy.forward(100)
            timmy.right(degrees/sides)


# Challenge 4 - Random Walk
def challenge4():
    directions = [0, 90, 180, 270]
    timmy.pensize(10)
    timmy.speed("fastest")
    for x in range(200):
        timmy.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        timmy.setheading(random.choice(directions))
        timmy.forward(20)


# Challenge 5 - Spirograph
def challenge5():
    timmy.speed("fastest")
    rings = 60
    degrees = 360
    for x in range(0, rings):
        timmy.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        timmy.circle(100)
        timmy.left(degrees/rings)


def hirst_painting():
    # rgb = []
    # Uses colorgram.py to extract color pallet from source image
    # colors = colorgram.extract('image.jpg', 30)
    # Pulls rgb values from colorgram and appends to rgb list as tuple
    # for color in colors:
    #     r = color.rgb.r
    #     g = color.rgb.g
    #     b = color.rgb.b
    #     stripped_color = (r, g, b)
    #     rgb.append(stripped_color)

    color_list = [(227, 224, 219), (210, 156, 102), (57, 98, 133), (157, 81, 52), (138, 159, 192), (51, 174, 121),
                  (232, 201, 101), (158, 167, 39), (121, 190, 175), (202, 135, 153), (66, 39, 33), (75, 113, 88),
                  (26, 48, 67), (133, 29, 48), (127, 81, 91), (181, 93, 109), (197, 93, 74), (117, 37, 24), (5, 68, 50),
                  (56, 31, 45), (231, 203, 0), (74, 132, 199), (161, 191, 224), (31, 65, 105), (26, 164, 170),
                  (16, 84, 56), (149, 210, 192)]

    timmy.speed("fastest")
    timmy.penup()
    timmy.goto(-300,-300)
    timmy.pendown()
    timmy.hideturtle()
    dots = 10
    y_coord = -300

    for y in range(dots):
        timmy.penup()
        timmy.goto(-300, y_coord)
        timmy.pendown()
        for x in range(dots):
            color = random.choice(color_list)
            timmy.dot(20, color)
            timmy.penup()
            timmy.forward(50)
            timmy.pendown()
        y_coord += 50


hirst_painting()

screen = Screen()
screen.exitonclick()

