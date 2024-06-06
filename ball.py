from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.15



    def bounce_to_change_y(self):
        self.y_move *= -1

    def bounce_to_change_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def check_boundary(self):
        if self.ycor() == 290 or self.ycor() == -290:
            self.bounce_to_change_y()





