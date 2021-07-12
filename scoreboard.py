from turtle import Turtle
import random
with open("data.txt", mode='r') as game_data:
    HIGH = int(game_data.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.high_score = HIGH
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-380, 360)
        self.write(f"score : {self.score}    High score : {self.high_score}", align="left", font=("arial", 20, "bold"))

    def increase_score(self):
        self.score += 8
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        with open("data.txt", mode="w") as write_data:
            write_data.write(f"{self.high_score}")



