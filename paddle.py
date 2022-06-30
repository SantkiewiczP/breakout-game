from turtle import Turtle

PADDLE_LENGTH = 5
PADDLE_WIDTH = 1
DISTANCE = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.color("blue")
        self.penup()
        self.goto(0, -270)

    def move_left(self):
        new_x = self.xcor() - DISTANCE
        self.goto(new_x, self.ycor())
        print(self.position())
        if self.xcor() < -360:
            x_pos, y_pos = self.pos()
            self.goto(x_pos + 20, y_pos)
            print(self.position())

    def move_right(self):
        new_x = self.xcor() + DISTANCE
        self.goto(new_x, self.ycor())
        print(self.position())
        if self.xcor() > 360:
            x_pos, y_pos = self.pos()
            self.goto(x_pos - 20, y_pos)
            print(self.position())

    def set_position(self):
        self.goto(-20, -270)

    def decrease_size_in_half(self, paddle_length):
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=paddle_length/2)
        print(self.turtlesize())



