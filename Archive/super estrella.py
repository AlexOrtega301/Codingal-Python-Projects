from turtle import *

Screen().bgcolor("black")
shape("turtle")
color("black")
width(3)
speed(0)

copo_de_nieve = 12
color("green")
for yo in range(copo_de_nieve):
    fd(200)
    bk(200)
    rt(360/copo_de_nieve)

rt(10)
copo_de_nieve = 18
color("red")
for yo in range(copo_de_nieve):
    fd(200)
    bk(200)
    rt(360/copo_de_nieve)

rt(5)
copo_de_nieve = 12
color("blue")
for yo in range(copo_de_nieve):
    fd(200)
    bk(200)
    rt(360/copo_de_nieve)
a = input("BOOM")
print("©️Alex")
