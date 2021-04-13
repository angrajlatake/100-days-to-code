
from random import randint

from turtle import Turtle, Screen

moves = 0


tl = Turtle()
screen = Screen()

tl.shapesize(2)
sides = 3
screen.colormode(255)
while sides != 11:
    tl.color(randint(0,256),
             randint(0,256),
             randint(0,256),)
    for i in range(sides):
        tl.forward(100)
        tl.right(360/sides)

    sides +=1

screen.exitonclick()







