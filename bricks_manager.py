from turtle import Turtle

COLUMNS = 14
ROWS = 8


class BricksManager:
    def __init__(self):
        super().__init__()
        self.width = 2.5
        self.height = 0.75
        self.bricks_list = []

    def lay_bricks(self):
        y_post = 50
        x_post = -380
        colors = ["yellow", "yellow", "green", "green", "orange", "orange", "red", "red"]
        for row in range(ROWS):
            color = colors[row]
            for col in range(COLUMNS):

                y_pos = (self.width * 10) * row
                x_pos = (self.height * 77) * col

                brick = Turtle(shape="square")
                brick.shapesize(stretch_wid=self.height, stretch_len=self.width)
                brick.color(color)
                brick.penup()
                brick.goto(x_post + x_pos, y_post + y_pos)
                self.bricks_list.append(brick)

                # print(f"X: {row}: {x_post + x_pos} Y: {col}: {y_post + y_pos}")

    def destroy_brick(self, brick):
        self.bricks_list.remove(brick)

