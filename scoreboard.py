from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("(っ◔◡◔)っ ♥ GAME OVER. ♥", align=ALIGNMENT, font=FONT)
