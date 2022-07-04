from turtle import Turtle

PADDLE_LENGTH = 5
PADDLE_WIDTH = 1
DISTANCE = 25


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
        if self.xcor() < -360:
            x_pos, y_pos = self.pos()
            self.goto(x_pos + DISTANCE, y_pos)

    def move_right(self):
        new_x = self.xcor() + DISTANCE
        self.goto(new_x, self.ycor())
        if self.xcor() > 360:
            x_pos, y_pos = self.pos()
            self.goto(x_pos - DISTANCE, y_pos)

    def set_position(self):
        self.goto(-20, -270)


