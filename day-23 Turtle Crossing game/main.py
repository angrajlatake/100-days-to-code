import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Score()
screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            score.reset()
            car_manager.reset()
            player.reset_posotion()
            time.sleep(5)


    if player.is_at_finish():
        score.add_point()
        player.reset_posotion()
        car_manager.level_up()


screen.exitonclick()