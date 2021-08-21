from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(0, 270)
        self.shapesize(0.1, 40)


class Score(Turtle):
    def __init__(self, position, p, al):
        super().__init__()
        self.score = 0
        self.p = p
        self.al = al
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.write(f"Player {self.p}: {self.score}", align=self.al, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Player {self.p}: {self.score}", align=self.al, font=FONT)
