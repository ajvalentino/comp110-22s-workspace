"""Drawing a brick path to the Old Well with the user's desired amount of flowers."""

__author__ = "730488997"

import turtle
from turtle import Turtle, done, update, tracer
from random import randint


def main() -> None:
    """Entrypoint of my scene."""
    tracer(0, 0)
    tim: Turtle = Turtle()
    tim.speed(9999)
    turtle.title("The Old Well")
    tim.hideturtle()

    tim.pencolor("green")
    rectangle(tim, -325, -275, 250, 650, "green")

    tim.pencolor("skyblue")
    rectangle(tim, -325, -25, 300, 650, "skyblue")

    tim.pencolor("black")

    brickpath(tim, -75, -50, 10)

    oldwell(tim, -50, -25)

    cloud(tim, -312.5, 125)
    cloud(tim, -100, 175)
    cloud(tim, 112.5, 100)

    flowers(tim)

    update()
    done()


def line(t: Turtle, xa: float, ya: float, xb: float, yb: float, color: int) -> None:
    """Draws a line from coordinates xa,ya to xb,yb."""
    t.penup()
    t.goto(xa, ya)
    t.pendown()
    t.goto(xb, yb)
    t.penup()


def rectangle(t: Turtle, x: float, y: float, length: float, width: float, color: str) -> None:
    """Creates a rectangle of desired size and color."""
    t.fillcolor(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()

    t.goto(x + width, y)
    t.goto(x + width, y + length)
    t.goto(x, y + length)
    t.goto(x, y)

    t.end_fill()
    t.penup()


def brickrow(t: Turtle, x: float, y: float, num: int) -> None:
    """Creates a row of desired amount of red bricks."""
    i: int = 0
    
    while i < num:
        rectangle(t, x, y, 25, 50, "firebrick")
        x += 50
        i += 1


def brickpath(t: Turtle, x: float, y: float, num: int) -> None:
    """Creates a brick path with desired amount of rows."""
    i: int = 0
    j: int = 3
    
    while i < num:
        brickrow(t, x, y, j)
        j += 1
        x -= 25
        y -= 25
        i += 1


def oldwell(t: Turtle, x: float, y: float) -> None:
    """Creates the old well."""
    rectangle(t, x, y, 5, 100, "grey")
    rectangle(t, x + 10, y + 5, 5, 80, "grey")
    pillars(t, x, y)
    roof(t, x, y)


def pillars(t: Turtle, x: float, y: float) -> None:
    """Creates the old well's pillars."""
    x += 20
    y += 10
    i: int = 0

    while i < 4:
        rectangle(t, x, y, 65, 6, "lightgrey")
        x += 18
        i += 1


def roof(t: Turtle, x: float, y: float) -> None:
    """Creates the roof of the old well."""
    x += 10
    y += 75
    i: int = 0
    width: int = 80

    while i < 5:
        rectangle(t, x, y, 5, width, "mediumturquoise")
        width -= 10
        x += 5
        y += 5
        i += 1


def cloud(t: Turtle, x: float, y: float) -> None:
    i: int = 0
    t.fillcolor("white")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()

    while i < 2:
        t.forward(50)
        t.right(90)
        t.forward(25)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(25)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        i += 1
    
    t.end_fill()
    t.penup()


def flowers(t: Turtle) -> None:
    """Uses input to create flowers."""
    count: int = howmanyflowers()
    i: int = 0

    while i < count:
        color: str = flowercolor()
        if i == 0:
            x = -275
            y = -100
        elif i == 1:
            x = 265
            y = -100
        elif i == 2:
            x = -200
            y = -75
        else:
            x = 190
            y = -75
        flower(t, x, y, color)
        i += 1


def flower(t: Turtle, x: int, y: int, color: str) -> None:
    """Creates flowers."""
    rectangle(t, x, y, 10, 10, "yellow")
    rectangle(t, x - 10, y, 10, 10, color)
    rectangle(t, x + 10, y, 10, 10, color)
    rectangle(t, x, y + 10, 10, 10, color)
    rectangle(t, x, y - 10, 10, 10, color)
    rectangle(t, x + 2, y - 25, 15, 6, "lightgreen")


def flowercolor() -> str:
    """Decides flower color."""
    colornum: int = randint(1, 4)
    color: str = ""

    if colornum == 1:
        color = "steelblue"
    elif colornum == 2:
        color = "orange"
    elif colornum == 3:
        color = "salmon"
    else:
        color = "blueviolet"
    
    return color


def howmanyflowers() -> int:
    """Asks how many flowers the user wants."""
    num = turtle.numinput("Number of Flowers", "How many flowers would you like from 0 to 4?", minval=0, maxval=4)
    i: int = 0

    while i < 5:
        if num == i:
            return i
        i += 1
    return 0


if __name__ == "__main__":
    main()