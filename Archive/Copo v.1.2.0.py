from turtle import *

speeed=int(input("cuanta velocidad quieres(0 es la más rapida)"))
shape("turtle")
speed(speeed)
width(3)
color("blue")
def patita(n):
    forward(n)    
    backward(n)
    left(30)
    forward(n)
    backward(n)
    right(60)
    forward(n)
    backward(n)
    left(30)
    forward(n)
def rama (n,l):
    for i in range (n):
        patita(l)
        stamp()
def snowflake (m,n,l):
    for i in range (m):
        rama(n,l)
        goto(0,0)
        rt(360/m)
l=int(input("que tan grande quieres que sea la patita"))
n=int(input("que tan larga quieres que sea la rama"))
m=int(input("cuantar ramas quieres"))
snowflake(m,n,l)
