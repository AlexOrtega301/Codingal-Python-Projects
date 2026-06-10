import random
from turtle import *

colors = ["cyan", "red", "purple", "orange", "tomato", "blue", "green"]
for i in range(7):
    alex = (random.choice(colors))
    colors.remove(alex)
    color(alex)
    begin_fill()
    circle(30)
    end_fill()
    fd(10)
    rt(53)
