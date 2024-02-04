from turtle import Turtle
import random

FRUIT_LIST = [r"pictures\dzban.gif", r"pictures\dzbanice.gif", r"pictures\stanley.gif"]


class Food(Turtle):
    """Class that handles food spawning at random locations"""
    def __init__(self):
        super().__init__()  # Inheriting from Turtle class
        self.random_fruit = random.choice(FRUIT_LIST)
        self.shape(self.random_fruit)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Spawn food at another random location"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.random_fruit = random.choice(FRUIT_LIST)
        self.shape(self.random_fruit)
        self.goto(random_x, random_y)
