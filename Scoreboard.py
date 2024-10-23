from turtle import  Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as data:
            self.high_score =int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score}   High Score: {self.high_score}", align="center", font=("New Times Roman", 20, "normal"))

    def refresh(self):
        self.score += 1
        self.update()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()










