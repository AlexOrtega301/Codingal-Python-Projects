from turtle import *

Screen().bgcolor("black")
color("red")
width(3)
speed(0)

copo_de_nieve = 124
for yo in range(copo_de_nieve):
    fd(200)
    bk(200)
    rt(360/copo_de_nieve)
