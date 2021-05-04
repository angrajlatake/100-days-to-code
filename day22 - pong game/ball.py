from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.speed(3)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.setposition(0, random.randint(-280, 280))
        self.
    def move(self):
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        self.goto(newx, newy)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        list = [-1, 1]
        bounce_angle = random.choice(list)
        self.x_move *= -1
        self.y_move *= bounce_angle

    def reset_postion(self):
        self.goto(0, random.randint(-280, 280))
        self.paddle_bounce()
