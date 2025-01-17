from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.snake()
        self.head = self.segments[0]
    def snake(self):
        for p in POSITION:
            self.add(p)


    def add(self,p):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(p)
        self.segments.append(new_segment)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.snake()
        self.head = self.segments[0]

    def extend(self):
        self.add(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
