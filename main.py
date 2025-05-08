import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
car=CarManager()
score=Scoreboard()
_player=Player()
screen.onkey(_player.Up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    for cars in car.all_cars:
        if cars.distance(_player)<20:
            score.game_over()
            game_is_on=False
    if _player.ycor() > 280:
        _player.start() # Reset player position
        score.level_up()
        car.level_up()

screen.exitonclick()