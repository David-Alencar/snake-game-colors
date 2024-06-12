from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')
FONT_2 = ('Courier', 24, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f'Score: {self.score}', False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', False, align=ALIGNMENT, font=FONT_2)


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(-290, -290)
        self.setheading(90)
        self.pendown()
        self.forward(580)
        self.setheading(0)
        self.forward(580)
        self.setheading(270)
        self.forward(580)
        self.setheading(180)
        self.forward(580)
