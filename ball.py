from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.head = random.randint(0, 360)
        self.penup()
        self.speed = 0.7
        self.color("white")
        self.shape("circle")
        self.setheading(self.head)

    def move(self):
        self.forward(self.speed)
        if self.ycor() >= 255 or self.ycor() <= -283:
            self.setheading(-self.heading())

    def speedup(self):
        self.speed += 0.1

    def ball_reset(self):
        self.goto(0, 0)
        self.speed = 0.7
        self.setheading(random.randint(0, 360))