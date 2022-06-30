from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 35, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.pencolor("white")
        self.score = 0
        self.lives = 3
        self.__update_scoreboard__()

    def add_points(self, points):
        self.score += points
        self.__update_scoreboard__()

    def clear_scoreboard(self):
        self.score = 0
        self.__update_scoreboard__()

    def __update_scoreboard__(self):
        self.clear()
        self.goto(270, 250)
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)
        self.goto(-300, 250)
        self.write(f"Lives:{self.lives}", align=ALIGNMENT, font=FONT)
