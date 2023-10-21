from turtle import Turtle

WIDTH = 20
HEIGHT = 600
LENGTH_PADDLE = 5
KEYSTROKE_STEPSIZE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.pu()
        self.color("white")
        self.goto(position)
        #self.resizemode("user")
        self.shapesize(stretch_wid=LENGTH_PADDLE, stretch_len=1)

    def go_up(self):
        if (self.ycor() <= HEIGHT / 2 - KEYSTROKE_STEPSIZE * 4):
            self.goto(self.xcor(), self.ycor() + KEYSTROKE_STEPSIZE)

    def go_down(self):
        if (self.ycor() >= -HEIGHT / 2 + KEYSTROKE_STEPSIZE * 4):
            self.goto(self.xcor(), self.ycor() - KEYSTROKE_STEPSIZE)

