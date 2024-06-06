from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(height= 600, width= 800)
screen.title("PONG")


screen.listen()

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()




screen.onkey(fun= r_paddle.move_up, key= "Up")
screen.onkey(fun= r_paddle.move_down, key= "Down")
screen.onkey(fun= l_paddle.move_up, key= "w")
screen.onkey(fun= l_paddle.move_down, key= "s")


while scoreboard.game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with walls
    ball.check_boundary()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_to_change_x()


    # detect paddle missing the ball
    elif ball.xcor() > 400:
        ball.home()
        ball.x_move *= -1
        ball.move_speed = 0.15
        scoreboard.left_point()


    elif ball.xcor() < -400:
        ball.home()
        ball.x_move *= -1
        ball.move_speed = 0.15
        scoreboard.right_point()









screen.exitonclick()