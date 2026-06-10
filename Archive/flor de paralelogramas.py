from turtle import *

def cube(n):
    for i in range(2):
        forward(n)
        right(60)
        forward(n/2)
        right(120)
def cube_circle(n):
    for i in range(12):
        cube(n)
        rt(30)

color('red')
width(5)
cube_circle(200)
