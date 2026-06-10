ffrom turtle import *

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

def rama (n,largo):
    for i in range (n):
        patita (largo)

def snowflake (m,n,largo):
    for i in range (m):
        rama (n,largo)
        fd(n)
        left(n)
largo=int(input("Que tan grande quieres la patita?")) 
n=int(input("que tan larga quieres que sea la rama?"))
m=int(input("Cuantas ramas quieres?"))

snowflake(m,n,largo)
