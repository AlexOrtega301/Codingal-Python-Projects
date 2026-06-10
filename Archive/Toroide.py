from turtle import *

speed(0)
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

def rama(n, l):
    for i in range(n):
        patita(l)
        right(360/n)

def snowflake(m, n, l):
    for i in range(m):
        rama(n, l)
        right(360/m)
l = 20
n = 20
m = 60

snowflake(m, n, l)
