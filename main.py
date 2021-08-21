from turtle import Screen
from pads import Paddle
from scoreboard import Border, Score
from ball import Ball
import time
import random
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

bord = Border()
ball = Ball()
p1_score = Score((-370, 267), 1, "left")
p2_score = Score((370, 267), 2, "right")

pad_1 = Paddle((350, 0))
pad_2 = Paddle((-350, 0))

screen.onkeypress(pad_1.up, "Up")
screen.onkeypress(pad_1.down, "Down")
screen.onkeypress(pad_2.up, "w")
screen.onkeypress(pad_2.down, "s")

game_is_on = True
first_press = False

while game_is_on:
    screen.update()
    ball.move()
    if ball.distance(pad_1) < 50 and 335 < ball.xcor() < 350:
        ball.setheading(-ball.heading() + 180)
        ball.speedup()
    if ball.distance(pad_2) < 50 and -335 > ball.xcor() > -350:
        ball.setheading(-ball.heading() + 180)
        ball.speedup()
    if ball.xcor() > 400:
        p1_score.increase()
        ball.ball_reset()
        screen.update()
        time.sleep(3)
    elif ball.xcor() < -400:
        p2_score.increase()
        ball.ball_reset()
        screen.update()
        time.sleep(3)







screen.exitonclick()