import colorgram
from turtle import Turtle, Screen
import turtle
from random import choice

turtle.colormode(255)
colors = colorgram.extract('download.jpeg', 30)
list_of_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    list_of_colors.append((r,g,b))




tl = Turtle()
screen = Screen()
tl.speed(0)
tl.shape("circle")


for i in range(10):
    tl.penup()
    tl.setx(-300)
    tl.sety(-300+ (50 * i))
    for i in range(10):
        tl.color(choice(list_of_colors))
        tl.dot(20)

        tl.forward(50)


tl.hideturtle()

screen.exitonclick()