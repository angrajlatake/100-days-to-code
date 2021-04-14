import turtle
from turtle import Turtle, Screen
from random import randint, choice

tl = Turtle()
screen = Screen()



tl.speed(10)
tl.pensize(20)
tl.shape("arrow")

def choose_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)




directions = [90, 180, 270, 360]
turtle.colormode(255)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


for i in range(500):
    tl.color(choose_color())
    tl.setheading(choice(directions))
    tl.forward(40)

screen.exitonclick()
