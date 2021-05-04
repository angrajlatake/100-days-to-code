from turtle import Turtle
import random
location = (random.choice(range(-280, 280, 20)), random.choice(range(-280, 280, 20)))
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1)
        self.color("blue")
        self.speed(0)
        self.goto(random.choice(range(-280, 280, 20)), random.choice(range(-280, 280, 20)))

    def refresh(self):
        self.goto(random.choice(range(-280, 280, 20)), random.choice(range(-280, 280, 20)))
