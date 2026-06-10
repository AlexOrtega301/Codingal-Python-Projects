from turtle import *
from time import sleep


c = input("enter the color: ")
color(c)
s = input("enter the shape: ")
shape(s)
bc = input("enter the background color: ")
Screen().bgcolor(bc)
w = int(input("enter the width: "))  
width(w)

count = 0  
while True:
    print("insert command : w = forward, s = backward, a = left, d = right, q = to left, e to right, up = don't draw, down = draw, exit = EXIT, circle = CIRCLE, dot = DOT, stamp == STAMP")
    command = input()
    if command == "w":
        forward(100)

    elif command == "s":
        backward(100)

    elif command == "a":
        left(90)
        
    elif command == "d":
        right(90)

    elif command == "q":
        left(120)

    elif command == "e":
        right(120)  

    elif command == "up":
        up()

    elif command == "down":
        down()
        
    elif command == "circle":
        circle(100)
        
    elif command == "dot":
        dot()
    elif command == "stamp":
        stamp()
    
    elif command == "exit":
        print("Saliendo del juego")
        sleep(3)
        print("Gracias por jugar")
        sleep(3)
        a = input("©️Alex")
        break 
