from turtle import Turtle

class Paddle(Turtle):


    def __init__(self, pos):
        super().__init__()
        self.resizemode("user")
        #resizemode can be "auto" or "user" or "noresize"
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid= 5, stretch_len=1)
        # multiplies default 20*20 pixels turtle with stretch_wid and stretch_len
        self.goto(pos)
        self.score = 0


    def move_up(self):
        self.goto(self.xcor(), self.ycor()+20)


    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


