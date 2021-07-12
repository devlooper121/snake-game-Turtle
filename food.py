from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("circle")
        self.color('blue')
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.random_food()

    def random_food(self):
        rand_x = random.choice(range(-380, 380, 10))
        rand_y = random.choice(range(-380, 380, 10))
        self.goto(rand_x, rand_y)
