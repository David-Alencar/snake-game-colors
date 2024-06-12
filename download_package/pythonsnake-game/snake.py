from turtle import Turtle, Screen
from random import randint
from time import sleep

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape='square')
            new_segment.color(randint(50, 255), randint(50, 255), randint(50, 255))
            new_segment.penup()
            new_segment.setposition(position)
            self.segments.append(new_segment)
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self, r, g, b):
        new_segment = Turtle(shape='square')
        new_segment.color(r, g, b)
        new_segment.penup()
        new_segment.setposition(self.segments[-1].pos())
        self.segments.append(new_segment)

    @property
    def self_collision(self):
        for parts in self.segments:
            if parts == self.head:
                pass
            else:
                if self.head.distance(parts) < 19:
                    return True

    @property
    def wall_collision(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

