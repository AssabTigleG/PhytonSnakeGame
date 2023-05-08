from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.home()
        self.clear()
        self.write(f"GAME OVER: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 22, "normal"))
