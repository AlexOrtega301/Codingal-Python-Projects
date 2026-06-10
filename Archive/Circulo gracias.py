from turtle import *
speed(0)
shape("turtle")
color("red")
def Tcircle():
    for i in range(12):
        goto(0,0)
        stamp()
        up()
        fd(100)
        stamp()
        rt(30)
Tcircle()
