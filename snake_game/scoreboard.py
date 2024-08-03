from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as highscore:
            self.highscore = int(highscore.read())
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align= "center", font= ("cumbria", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(f"{self.score}")
                self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align= "center", font=("cumbria", 24, "normal"))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

