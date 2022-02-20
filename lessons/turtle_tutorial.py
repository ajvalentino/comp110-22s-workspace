"""Learning how to use turtles."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

side_length: float = 300

leo.speed(50)
colormode(255)
leo.fillcolor(100, 100, 100)
leo.hideturtle()
leo.penup()
leo.goto(-150, 120)
leo.pendown()
leo.begin_fill()

i: int = 0
while i < 3:
    leo.forward(side_length)
    leo.right(120)
    i += 1

leo.end_fill()


bob: Turtle = Turtle()

colormode(255)
bob.fillcolor(255, 255, 255)
bob.speed(1000)
bob.penup()
bob.goto(-150, 120)
bob.pendown()

i: int = 0
while i < 200:
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.right(121)
    i += 1

done()