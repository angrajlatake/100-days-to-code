from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def move_back():
    tim.backward(10)


screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_back, "Down")
screen.onkey(turn_right, "Right")
screen.onkey(turn_left, "Left")
screen.onkey(screen.resetscreen, "c")
screen.exitonclick()