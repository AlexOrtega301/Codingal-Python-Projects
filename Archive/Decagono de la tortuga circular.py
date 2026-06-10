from turtle import *
color("red")
Screen().bgcolor("black")
width(3)
shape("circle")
decagono = 10
for w in range(decagono):
    fd(100)
    rt(360/decagono)
    stamp()
