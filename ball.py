from turtle import Turtle

#SIZE = 20
INITIAL_SPEED = [10, 10]
HEIGHT = 600
SPEED_FACTOR = 0.9
BALL_INITIAL_SPEED = 0.1


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.pu()
        self.color("white")
        self.goto(position)
        self.ball_speed = BALL_INITIAL_SPEED
        #self.shapesize(stretch_wid=SIZE, stretch_len=SIZE)
        self.speed = INITIAL_SPEED

    def move(self):
        self.goto(self.xcor() + self.speed[0],
                  self.ycor() + self.speed[1])

    def bounce_y(self):
        self.speed[1] *= -1

    def bounce_x_rpaddle(self):
        self.speed[0] = -(abs(self.speed[0]))
        self.ball_speed *= SPEED_FACTOR

    def bounce_x_lpaddle(self):
        self.speed[0] = abs(self.speed[0])
        self.ball_speed *= SPEED_FACTOR

    def reset_position(self):
        self.goto((0, 0))
        self.speed[0] *= -1
        self.ball_speed = BALL_INITIAL_SPEED
