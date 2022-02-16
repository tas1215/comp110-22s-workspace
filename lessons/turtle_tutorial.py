"""This is the set up for turtle."""

from turtle import Turtle, colormode, done
import turtle
leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()
colormode(255)
leo.color(99, 204, 250)
leo.penup()
leo.goto(-150, -120)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()

bob.color(0, 0, 0)
bob.penup()
bob.goto(-150, -120)
bob.pendown()
bob.speed(75)

side_length: float = 300.0

i: int = 0
while (i < 75):
    bob.forward(side_length)
    bob.left(123)
    bob.forward(side_length)
    bob.left(121)
    bob.forward(side_length)
    bob.left(120.5)
    i = i + 1
done()