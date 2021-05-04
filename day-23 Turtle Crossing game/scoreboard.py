from turtle import Turtle



FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(0,270)

        self.color("black")
        self.hideturtle()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score {self.score}  High Score : {self.high_score} ", align="center", font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font= FONT)

    def add_point(self):
        self.score += 1
        self.update_score()

