from turtle import Turtle, Screen
from random import randint

def check_location():
    pass
screen = Screen()
screen.setup(500, 400)
screen.title("Welcome to the turtle race")
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
y_positions = [0, 30, -30, 60, -60, 90, -90]
all_turtles = []
for i in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[i])
    all_turtles.append(new_turtle)

continue_race = True
finish_line = Turtle()
finish_line.penup()
finish_line.goto(220,90)
finish_line.pendown()
finish_line.goto(220, -90)
user_input = screen.textinput(title= "Make a Bet!", prompt= "Choose the color of the turtle you want to bet on: ")

while continue_race:
    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            continue_race = False
            winning_turtle = (colors[all_turtles.index(turtle)]).title()

        distance = randint(0, 10)
        turtle.forward(distance)



if winning_turtle == user_input.title():
    print("You won!")
else:
    print(f"Your {user_input} turtle lost!")

print(f"{winning_turtle} is the winning turtle.")
screen.exitonclick()