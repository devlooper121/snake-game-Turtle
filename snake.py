from turtle import Turtle
STARTING_SNAKE = [(0,0), (-20,0), (-40,0)]
SPEED = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.speed = SPEED
        self.pause = 0
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_SNAKE:
            self.create_segments(pos)

    def create_segments(self, positions):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(stretch_wid=0.8, stretch_len=0.8)
        new_segment.penup()
        new_segment.goto(positions[0], positions[1])
        self.segments.append(new_segment)

    def move(self):
        if self.pause == 0:
            for seg_no in range((len(self.segments)-1), 0, -1):
                new_x = self.segments[seg_no - 1].xcor()
                new_y = self.segments[seg_no - 1].ycor()
                self.segments[seg_no].goto(new_x, new_y)
            self.head.fd(self.speed)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self):
        last_x = self.segments[-1].xcor()
        last_y = self.segments[-1].ycor()
        next_pos = (last_x, last_y)
        self.create_segments(next_pos)

    def free_mode(self):
        self.move()
        # boundary loop
        h = self.head
        if h.heading() == RIGHT and h.xcor() >= 400:
            h.goto(-400, h.ycor())
        elif h.heading() == LEFT and h.xcor() <= -400:
            h.goto(400, h.ycor())
        elif h.heading() == DOWN and h.ycor() <= -400:
            h.goto(h.xcor(), 400)
        elif h.heading() == UP and h.ycor() >= 400:
            h.goto(h.xcor(), -400)

    def reset(self):
        for snake in self.segments:
            snake.goto(1000,1000)
        self.segments.clear()

        self.create_snake()
        self.head = self.segments[0]
        self.pause = 1

    def play_pause(self):
        if self.pause == 0:
            self.pause = 1
        else:
            self.pause = 0









