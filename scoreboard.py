from turtle import Turtle

FONT = ("Courier", 80, "normal")
L_SCORE_POSITION = (-100, 200)
R_SCORE_POSITION = (100, 200)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def increase_lscore(self):
        self.l_score += 1
        self.write_score()

    def increase_rscore(self):
        self.r_score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(L_SCORE_POSITION)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(R_SCORE_POSITION)
        self.write(self.r_score, align="center", font=FONT)
