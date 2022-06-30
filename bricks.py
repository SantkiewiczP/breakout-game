from turtle import Turtle


class Brick(Turtle):

    def __init__(self):
        super().__init__()
        pass

    def lay_bricks(self):
        # 8 rows
        # 14 columns
        # from top: 2 rows red, 2 rows orange, 2 rows green and 2 rows yellow
        pass

    def destroy_brick(self):
        # when making contact with the ball
        # if yellow: +1 point
        # if green: +3 points
        # if orange: +5 points
        # if red: +7 points
        # if no more bricks left: lay the brick again, level 2 begins

        pass