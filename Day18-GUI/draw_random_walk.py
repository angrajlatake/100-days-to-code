from turtle import Turtle, Screen
import random

tl = Turtle()
screen = Screen()
tl.speed(10)
tl.pensize(20)
tl.shape("arrow")


directions = [90, 180, 270, 360]

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


for i in range(500):
    tl.color(random.choice(colours))
    tl.setheading(random.choice(directions))
    tl.forward(40)

screen.exitonclick()
