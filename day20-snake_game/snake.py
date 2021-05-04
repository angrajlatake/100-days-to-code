from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake():
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
    def create_snake(self):
        for i in range(0,3):
            self.add_segment()


    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.setx(position)
        self.snake_list.append(snake)

    def extend(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()

        self.snake_list.append(snake)





    def move(self):
        for numb in range(len(self.snake_list) - 1, 0, -1):
            new_postion = self.snake_list[numb - 1].position()
            self.snake_list[numb].goto(new_postion)

        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:

            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:

            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:

            self.head.setheading(RIGHT)

