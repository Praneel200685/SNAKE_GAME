from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
dist = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_seg(position)  # Pass position argument properly

    def snake_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(dist)  # Ensures correct movement

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_seg(self, position):  # Expecting a position argument
        segment = Turtle(shape="circle")
        segment.color("yellow", "green")
        segment.penup()
        segment.goto(position)  # Using correct argument
        self.segments.append(segment)

    def extend(self):
        self.add_seg(self.segments[-1].position())  # Correctly adds a new segment
