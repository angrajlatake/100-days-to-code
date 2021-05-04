from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

border = Turtle()


score = Score()

screen = Screen()


screen.listen()
screen.onkey(screen.resetscreen, "r")

snake = Snake()
food = Food()
screen.title("Snake")

screen.screensize(600, 600, "black")
border.penup()
border.goto(-300, -300)
border.pencolor("white")
border.pendown()
border.forward(600)
border.left(90)
border.forward(600)
border.left(90)
border.forward(600)
border.left(90)
border.forward(600)
border.left(90)
border.hideturtle()

screen.tracer(0)



screen.update()

screen.listen()

game_is_on =  True

screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #what happens when snake eats the food, the food appears somewhere else
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_point()

#wall collision

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        score.game_over()


screen.exitonclick()