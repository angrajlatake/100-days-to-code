import turtle
from random import randint

tl = turtle.Turtle()
tl2 = turtle.Turtle()
screen = turtle.Screen()
tl.speed(0)
tl2.speed(0)
heading = range(0,361,5)
index = 0
turtle.colormode(255)

def choose_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)


for i in heading:
    tl.color(choose_color())
    tl.setheading(heading[index])
    tl.circle(100)



    tl2.color(choose_color())
    tl2.setheading(heading[index])
    tl2.circle(50)


    index += 1


screen.exitonclick()