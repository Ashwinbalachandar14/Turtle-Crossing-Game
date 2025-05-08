FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.write(align="left",font=FONT,arg=f"Level:{self.level}")

    def level_up(self):
        self.clear()
        self.level+=1
        self.write(align="left", font=FONT, arg=f"Level:{self.level}")
    def game_over(self):
        self.goto(0,0)
        self.write(align="Center",font=FONT,arg="Game Over")

