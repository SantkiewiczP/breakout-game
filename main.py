from turtle import Screen, Turtle
from ball import Ball
from bricks_manager import BricksManager
from paddle import Paddle
from scoreboard import Scoreboard
import time


def write_text(text):
    game_over_text = Turtle()
    game_over_text.color("blue")
    game_over_text.hideturtle()
    game_over_text.goto(0, -50)
    game_over_text.write(f"{text}", align="center", font=("Courier", 100, 'bold'))


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball()
bricks_manager = BricksManager()
screen.listen()

bricks_manager.lay_bricks()

screen.onkeypress(fun=paddle.move_left, key="a")
screen.onkeypress(fun=paddle.move_right, key="d")

ball_hits = 0
game_is_on = True
orange_row_hit = False
red_row_hit = False
hit_brick = True
last_time = time.time_ns()
while game_is_on:
    current_time = time.time_ns()
    delta = (current_time - last_time) / 1000000.0
    last_time = current_time
    screen.update()

    ball.move(delta)

    ball_speed = 1.25
    if 4 <= ball_hits < 12:
        ball_speed += 0.25
    if ball_hits >= 12:
        ball_speed += 0.25
    if orange_row_hit:
        ball_speed += 0.25
    if red_row_hit:
        ball_speed += 0.25

    ball.set_speed(ball_speed)

    # Detect if ball collides with upper wall
    if ball.ycor() > 280:
        ball.bounce_y()
    # Detect if ball collides with walls and bounce
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    # Detect if ball collides with paddle and bounce:
    if hit_brick and ball.distance(paddle) < 50 and ball.ycor() < -250:
        ball.bounce_y()
        hit_brick = False

    # Detect if ball went past the paddle
    if ball.ycor() < -300:
        scoreboard.lives -= 1
        scoreboard.__update_scoreboard__()
        paddle.set_position()
        ball.set_position()
        if scoreboard.lives == 0:
            write_text("GAME OVER")
            game_is_on = False

    # Detect if ball collides with bricks, bounce and add points based on the brick color
    for brick in bricks_manager.bricks_list:
        if ball.distance(brick) < 25 and ball.xcor() > 0 or ball.distance(brick) < 25 and ball.xcor() < 0:
            hit_brick = True
            brick.hideturtle()
            ball.bounce_y()
            bricks_manager.destroy_brick(brick)
            ball_hits += 1
            if brick.color() == ("yellow", "yellow"):
                scoreboard.add_points(1)
            elif brick.color() == ("green", "green"):
                scoreboard.add_points(3)
            elif brick.color() == ("orange", "orange"):
                scoreboard.add_points(5)
                orange_row_hit = True
            elif brick.color() == ("red", "red"):
                scoreboard.add_points(7)
                red_row_hit = True

        # if no more bricks left - game is done, well done!
        if len(bricks_manager.bricks_list) == 0:
            write_text("YOU WON!")
            game_is_on = False

screen.exitonclick()
