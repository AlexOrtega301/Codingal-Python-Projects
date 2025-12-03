import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("")  # Empty title

# Create turtle
t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(5)  # Moderate speed

# Function to draw a regular polygon
def draw_polygon(sides, length, color, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.stamp()  # Stamp the turtle at the end

# List of shapes: (sides, length, color, position)
shapes = [
    (3, 100, "red", (-200, 200)),    # Triangle
    (4, 100, "green", (0, 200)),     # Square
    (4, 150, "blue", (200, 200)),    # Rectangle (drawn as a square and stretched)
    (5, 80, "yellow", (-200, 0)),    # Pentagon
    (6, 80, "cyan", (0, 0)),         # Hexagon
    (8, 60, "magenta", (200, 0)),    # Octagon
    (10, 50, "orange", (-100, -200)) # Decagon
]

# Draw all shapes
for sides, length, color, pos in shapes:
    draw_polygon(sides, length, color, pos)

# Hide turtle and finish
t.hideturtle()
turtle.done()
