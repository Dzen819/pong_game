from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5)
        self.setpos(position)
        self.setheading(90)

    def up(self):
        if self.ycor() < 210:
            self.forward(20)

    def down(self):
        if self.ycor() > -240:
            self.backward(20)