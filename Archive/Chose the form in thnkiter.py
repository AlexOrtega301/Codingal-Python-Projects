from turtle import *
from tkinter import *
    
o = 10
lol = 20
shape("turtle") 
speed(0)
width(3)
title("TURTLE GAME ©️Alex")
print("There are only parallelograms (abbreviated as pg), circle, decagon, square, rectangle and triangle")
print("If you want to exit, type 'exit'")
print("If you want to clear the drawings, type 'cls'")
print("If you want to return to the starting point, type 'start point'")
print("the forms are: arrow, turtle, circle, square, triangle and classic (Add an ""s"" before the shape of the turtle")
print("If you want to enter a color, these are: red, blue, green, purple, violet, light grey, yellow, and orange")
print("The commands are w, s, a, d, up, down, dot, st")
print("If you want a toroid of these shapes, ask for toroid + shape")
print("Enter a shape, color, toroid, form or a command in the window")


def paralelogamo():
    for i in range(2):
        fd(100)
        rt(120)
        fd(50)
        rt(60)

def circulo():
    circle(30)

def triangulo():
    for i in range(3):
        rt(120)
        fd(100)

def decagono():
    for i in range(o):
        forward(30)
        right(360/o)

def square():
    for i in range(4):
        forward(100)
        right(90)

def rectangle():
    for i in range(2):
        forward(100)
        right(90)
        forward(50)
        right(90)

def toroide1():
    for i in range(lol):
        decagono()
        rt(360/lol)

def toroide2():
    for i in range(lol):
        circulo()
        rt(360/lol)

def toroide3():
    for i in range(lol):
        triangulo()
        rt(360/lol)

def toroide4():
    for i in range(lol):
        paralelogamo()
        rt(360/lol)

def toroide5():
    for i in range(lol):
        square()
        rt(360/lol)

def toroide6():
    for i in range(lol):
        rectangle()
        rt(360/lol)

def clicked():
    command = bla_bla_bla.get()
    if command == "exit":
        print("Closing The Game")
        print("Close ALL Python Windows to continue")
    elif command == "pg":
        paralelogamo()
    elif command == "circle":
        circulo()
    elif command == "triangle":
        triangulo()
    elif command == "decagon":
        decagono()
    elif command == "square":
        square()
    elif command == "rectangle":
        rectangle()
    elif command == "toroid + pg":
        toroide3()
    elif command == "toroid + circle":
        toroide2()
    elif command == "toroid + decagon":
        toroide1()
    elif command == "toroid + triangle":
        toroide4()
    elif command == "toroid + square":
        toroide5()
    elif command == "toroid + rectangle":
        toroide6()
    elif command == "cls":
        clear()
    elif command == "w":
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
    elif command == "dot":
        dot()
    elif command == "st":
        stamp()
    elif command == "red":
        color("red")
    elif command == "blue":
        color("blue")
    elif command == "green":
        color("green")
    elif command == "purple" or command == "violet":
        color("purple")
    elif command == "light grey":
        color("snow4")
    elif command == "yellow":
        color("yellow")
    elif command == "orange":
        color("orange")
    elif command == "sarrow":
        shape("arrow")
    elif command == "scircle":
        shape("circle")
    elif command == "sturtle":
        shape("turtle")
    elif command == ("ssquare"):
        shape("square")
    elif command == ("striangle"):
        shape("triangle")
    elif command == ("sclassic"):
        shape("classic")
    elif command == "start point":
        goto(0, 0)

window = Tk()
window.title("TURTLE GAME ©️Alex")
window.geometry("300x50")
bla_bla_bla = Entry(window,width=30)
bla_bla_bla.grid(column=1, row=0)
btn = Button(window, text="Press this Button when your Command is READY", command=clicked)
btn.grid(column=3, row=0)
window.mainloop()
