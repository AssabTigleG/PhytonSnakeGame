from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("cyan")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.refresh()

    def refresh(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)
