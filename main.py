from turtle import Screen, numinput
from scoreboard import ScoreBoard
from snake import Snake
from food import Food

import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Snake Game!")

game_type = numinput(title="Welcome to Classic Snake Game.",prompt="0. for Box Mode\n1. for Free Mode" )
game_mode = game_type

screen.tracer(0)

snake = Snake()
food = Food()
sc_board = ScoreBoard()


screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.play_pause, key="space")

speed = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(speed)
    snake.free_mode()

    # food eating

    if food.distance(snake.head) < 15:
        food.random_food()
        snake.add_segment()
        sc_board.increase_score()
    # collision with body
    for snk in snake.segments[3::1]:
        if snake.head.distance(snk) < 20:
            snake.reset()
            sc_board.reset_score()

    # colision with wall
    if game_mode == 0:
        if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
            snake.reset()
            sc_board.reset_score()




screen.exitonclick()
