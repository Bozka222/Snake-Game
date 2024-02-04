from turtle import Turtle
FONT = ("Courier", 18, "bold")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    """Creates scoreboard counter with in game score and all-time high score"""
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as game_data:
            self.high_score = int(game_data.read())
        self.score_counter = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates score after each point"""
        self.clear()
        self.write(arg=f"Score: {self.score_counter} | HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases score counter by one and updates score count"""
        self.score_counter += 1
        self.update_scoreboard()

    def reset_score(self):
        """Resets score count and sets all-time high score count"""
        if self.score_counter > self.high_score:
            self.high_score = self.score_counter
            with open("data.txt", mode="w") as game_data:
                game_data.write(f"{self.high_score}")
        self.score_counter = 0
        self.update_scoreboard()
