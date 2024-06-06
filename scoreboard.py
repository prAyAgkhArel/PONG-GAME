from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.max_score = 0
        self.goto(-10, 260)
        self.game_is_on = True
        self.display_score()



    def left_point(self):
        self.l_score += 1
        self.display_score()

    def right_point(self):
        self.r_score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{self.l_score}           {self.r_score}", align= "center", font=("Courier",25, "normal" ) )


    # def decide_winner(self):
    #     if self.l_score == self.max_score:
    #         self.goto(0,0)
    #         self.write(f" Left is the winner with score {self.l_score}", align="center", font=("Courier", 25, "normal"))
    #         self.game_is_on = False
    #
    #
    #     elif self.r_score == self.max_score:
    #         self.goto(0, 0)
    #         self.write(f" Right is the winner with score {self.r_score}", align="center", font=("Courier", 20, "normal"))
    #         self.game_is_on = False


