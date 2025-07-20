from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)  # Position for score display
        self.hideturtle()
        self.update_score()  # Initial score display

    def update_score(self):
        self.clear()  # Clears previous score before writing the updated one
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "bold"))

    def upscore(self):
        self.score += 1
        self.update_score()  # Update display after incrementing score

    def game(self):
        self.goto(0,0)
        self.write("Game Over", align="center",font=("Courier", 18, "bold"))

# Example Usage: Ensure this method is triggered on collision
# scoreboard = Scoreboard()
# if collision_detected:  # Example condition for detecting collision
#     scoreboard.upscore()