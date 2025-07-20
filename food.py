from random import randint
from turtle import Turtle
class Food(Turtle):
     def __init__(self):
         super().__init__()
         self.shape("circle")
         self.penup()
         self.shapesize(0.5 , 0.5)
         self.color("yellow","red")
         self.speed("fastest")
         random_x=randint(-280,280)
         random_y=randint(-280,260)
         self.goto(random_x,random_y)
         self.refresh()

     def refresh(self):
         random_x = randint(-280, 280)
         random_y = randint(-280, 280)
         self.goto(random_x, random_y)
