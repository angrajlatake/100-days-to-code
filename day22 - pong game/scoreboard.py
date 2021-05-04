from turtle import Turtle





class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(0,300)

        self.color("white")

        self.score_left = 0
        self.score_right = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score {self.score_left} : {self.score_right}", align="center", font = ("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def add_point_left(self):
        self.score_left += 1
        self.update_score()

    def add_point_right(self):
        self.score_right += 1
        self.update_score()