from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
BALL_SIZE = 20
CONTACT_SIZE = 50
EDGE_THRESHOLD = 80
INITIAL_SPEED = 0.1

screen = Screen()
screen.title("Pong")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
game_is_on = True

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_is_on:
    screen.update()
    sleep(ball.ball_speed)
    ball.move()

    #Collision with top/bottom walls
    if (ball.ycor() > HEIGHT / 2 - BALL_SIZE or
        ball.ycor() < -HEIGHT / 2 + BALL_SIZE):
        ball.bounce_y()

    #Collision with paddles
    #Right paddle
    if (ball.distance(r_paddle) < CONTACT_SIZE and
         ball.xcor() > WIDTH / 2 - EDGE_THRESHOLD):
        ball.bounce_x_rpaddle()

    #Left paddle
    if (ball.distance(l_paddle) < CONTACT_SIZE and
        ball.xcor() < -WIDTH / 2 + EDGE_THRESHOLD):
        ball.bounce_x_lpaddle()

    #Collision with right wall
    if ball.xcor() > WIDTH / 2 - BALL_SIZE:
        ball.reset_position()
        scoreboard.increase_lscore()

    #Collision with left wall
    if ball.xcor() < -WIDTH / 2 + BALL_SIZE:
        ball.reset_position()
        scoreboard.increase_rscore()

screen.exitonclick()
