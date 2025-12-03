import turtle

# creating canvas
turtle.Screen().bgcolor("White")

sc = turtle.Screen()
sc.setup(700, 800)
turtle.pencolor("red")
turtle.title("")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
	board.forward(100)
	board.left(90)
	i = i+1
