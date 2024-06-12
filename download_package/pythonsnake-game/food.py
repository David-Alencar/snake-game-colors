from turtle import Turtle, Screen
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color(1, 1, 255)
        self.shapesize(0.5, 0.5)
        self.penup()
        self.setposition(randint(-250, 250), randint(-250, 250))

    def new_color(self):
        self.color(randint(50, 255), randint(50, 255), randint(50, 255))

