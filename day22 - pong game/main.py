from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


score = Score()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

border = Turtle()


border.penup()
border.speed(0)
border.pencolor("white")

border.goto(-400, -300)
border.pendown()
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)
border.forward(800)
border.left(90)
border.forward(600)
border.hideturtle()



screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "q")
screen.onkey(l_paddle.go_down, "a")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() >290 or ball.ycor() < - 290 :
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()


    if ball.xcor() > 360 :
        ball.reset_postion()
        score.add_point_left()
        time.sleep()
    if ball.xcor() < -360 :
        ball.reset_postion()
        score.add_point_right()
        time.sleep(3)

    if score.score_left == 10 or score.score_right == 10 :
        game_is_on = False
        score.game_over()

screen.exitonclick()